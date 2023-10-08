from django.urls import path
from . import views

app_name = 'm_shop'  # Replace 'your_app_name' with the actual name of your app

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', views.ManageCategoriesView.as_view(), name='manage_categories'),
    # Add more URLs as needed for your app's views
    # About Urls
    path('about/', views.About.as_view(), name='about'),
    
    # Contacts Urls
    
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.SuccessView.as_view(), name='success'),
]
