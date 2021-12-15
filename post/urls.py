from django.urls import path
from .views import PostDetail, PostList
urlpatterns = [
    path("posts/<pk>/", PostDetail.as_view(), name="Get PostDetails By Uid "),
    path("posts/", PostList.as_view(), name="Retrive Posts"),
]