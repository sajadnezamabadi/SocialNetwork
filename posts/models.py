from django.db import models

from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.title
    

class PostFile(models.Model):
    post= models.ForeignKey(to='posts.Post' , on_delete=models.CASCADE)
    image = models.ImageField()
    file = models.FileField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post File'
        verbose_name_plural = 'Post Files'
    


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'