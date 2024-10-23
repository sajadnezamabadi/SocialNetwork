from django.db import models
from django.conf import settings

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        # db_table = 'ac_country'
        
    
class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True,null=True,unique=True)
    country = models.ForeignKey(to=Country , on_delete=models.CASCADE)   
    avatar = models.ImageField(blank=True, upload_to='profile_avatar/')
    
    
class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB,'web'),
        (DEVICE_IOS,'ios'),
        (DEVICE_ANDROID,'android'),
        (DEVICE_PC,'pc'),
    )
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID',null=True)
    last_login = models.DateTimeField(null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    device_os = models.CharField('device os',max_length=2 , blank=True)
    device_model = models.CharField('device model',null=True,max_length=20)
    app_version = models.CharField('app version',max_length=20 , null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    