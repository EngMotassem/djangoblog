from django.urls import path, re_path
from .views import home

app_name = AppName

urlpatterns = [
    path('',home,name='home'),
    
]