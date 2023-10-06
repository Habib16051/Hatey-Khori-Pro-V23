from django.db import models
from django.contrib.auth.models import User  # You may need to import the User model if you plan to associate products with users.

# Define the ProductCategory model
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

# Define the Product model
class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Assumes you have a 'media' directory for storing images.

    # Add a foreign key to link the product to the user who created it (optional).
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    # Add any other fields or methods you need for your product model.

    def __str__(self):
        return self.product_name
