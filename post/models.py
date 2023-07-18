from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(max_length=20)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='post/%Y/%m/%d',blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated=models.DateTimeField(auto_now=True,blank=True,null=True)
    type_1=models.CharField(max_length=250,blank=True,null=True)
    status=models.CharField(max_length=40,blank=True,null=True)
    video=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Films'
        verbose_name = 'Films'

class Comment(models.Model):
    post = models.OneToOneField(to=Post, on_delete=models.CASCADE, verbose_name='Пост',null=True,blank=True)
    user = models.CharField('name', max_length=20)
    text = models.TextField('Text')
    date = models.DateField( auto_now_add=True,null=True,blank=True)
    active = models.BooleanField('is_active', default=False)
    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comments'
    def __str__(self):
        return self.user


