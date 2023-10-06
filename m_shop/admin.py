from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'product_price')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')
    # Add more customizations as needed

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
    # Add more customizations as needed
