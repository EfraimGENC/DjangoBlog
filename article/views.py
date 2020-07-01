from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, get_list_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

@login_required(login_url = 'user:login')
def dashboard(request):
    articles = Article.objects.filter(author = request.user).order_by('created_date').reverse()
    return render(request,'dashboard.html',{'articles':articles})

@login_required(login_url = 'user:login')
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,'Makale başarıyla eklendi.')
        return redirect('index')
    return render(request,'addarticle.html',{'form':form})

def detail(request,id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all().order_by('comment_date').reverse()
    return render(request,'detail.html',{'article':article , 'comments':comments})

def authorsArticles(request,author):
    kullanici = get_object_or_404(User, username=author)
    articles = Article.objects.filter(author=kullanici)
    return render(request,'authordetail.html',{'articles':articles})

@login_required(login_url = 'user:login')
def articleUpdate(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,'Makale başarıyla güncellendi.')
        return redirect('article:dashboard')
    return render(request,'update.html',{'form':form})

@login_required(login_url = 'user:login')
def articleDelete(request,id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request,'Makale başarıyla silindi.')
    return redirect('article:dashboard')

def allArticles(request):
    keyword = request.GET.get('keyword')

    if keyword:
        articles = Article.objects.filter(title__contains = keyword).order_by('created_date').reverse()
        return render(request,'articles.html',{'articles':articles})

    articles = Article.objects.all().order_by('created_date').reverse()
    return render(request,'articles.html',{'articles':articles})

def addComments(request,id):
    article = get_object_or_404(Article, id = id)

    if request.method == 'POST':
        cauthor = request.POST.get('cauthor')
        ccontent = request.POST.get('ccontent')

        newComment = Comment(comments_author=cauthor, comments_content=ccontent)
        newComment.article = article
        newComment.save()

    return redirect(reverse('article:detail',kwargs={'id':id}))