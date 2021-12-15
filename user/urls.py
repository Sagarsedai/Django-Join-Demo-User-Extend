from django.urls import path
from .views import UserDetail, UserList
urlpatterns = [
    path("users/<pk>/", UserDetail.as_view(), name="Get UserDetails By Uid "),
    path("users/", UserList.as_view(), name="Retrive Users"),
]