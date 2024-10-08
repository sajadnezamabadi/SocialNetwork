from django.urls import path

from .views import *

#############################
urlpatterns = [
    path("posts/", PostView.as_view(), name="post"),
    path("posts/<int:post_pk>/", PostView.as_view(), name="post"),
    path("posts-list/", PostListView.as_view(), name="posts-list")
    
]
