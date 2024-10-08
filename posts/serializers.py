from rest_framework import serializers

from .models import *

######################################

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ('user','title','caption','is_active','is_public')
        extra_kwargs = {
            'user':{'read_only':True}
        }   