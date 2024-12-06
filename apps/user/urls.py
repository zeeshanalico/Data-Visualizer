from django.urls import path
from .views import CreateUserView, GetUsersView

urlpatterns = [
    path("create", CreateUserView.as_view()),  
    path("list", GetUsersView.as_view()),  
]
