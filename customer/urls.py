from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    # Other URL patterns for your app
    path('index/', views.index, name='index'),
    path('logout_success/', views.logout_success, name='logout_success'),

    # Registration, login, and logout URLs

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]