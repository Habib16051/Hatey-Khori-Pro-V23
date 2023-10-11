from django.contrib import admin
from django.urls import path, include
from m_shop import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('m_shop.urls')),
    path('', include('customer.urls')),
    
    # path('login/',  LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/',  LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    