from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('register/', views.RegisterView, name='register'),
    path('login/',  LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/',  LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
  
    
]
