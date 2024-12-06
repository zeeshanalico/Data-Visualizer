from django.urls import path
from .views import AuthView 


urlpatterns = [
        path('get', AuthView.as_view(), name='auth'), 
]
