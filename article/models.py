from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=50, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True,null=True,verbose_name='Kapak Fotoğrafı')

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='Makale',related_name='comments')
    comments_author = models.CharField(max_length=50,verbose_name='Yorumcu')
    comments_content = models.CharField(max_length=250,verbose_name='Yarum')
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comments_content
    