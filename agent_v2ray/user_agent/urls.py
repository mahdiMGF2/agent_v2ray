from django.urls import path
from .views import *
app_name = 'user_agent'
urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('login/', Login, name='login'),
    path('register/', register, name='registerpage'),
]