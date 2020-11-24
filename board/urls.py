from django.urls import path, re_path
from .views import home
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'board'

urlpatterns = [
    path('',home,name='home'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)