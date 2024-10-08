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
    



# class Comeent(models.Model):
#     pass


# class Like(models.Model):
#     pass