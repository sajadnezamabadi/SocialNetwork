from django.contrib import admin

from .models import *

# Register your models here.

class PostFileInLineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 0
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','is_active','create_time']
    inlines = (PostFileInLineAdmin,)