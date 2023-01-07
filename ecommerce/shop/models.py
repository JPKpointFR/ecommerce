from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
"""
models:
- Produit
- Quantité
- Com

"""


class Category(models.Model):
    """
  Modèle de catégorie de produit représentant une catégorie de produits sur le site e-commerce.
    """
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Modèle de produit représentant un produit disponible à la vente sur le site e-commerce.
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(default="description")
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='products/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'product_slug': self.slug})


# class Order(models.Model):
#     """ Modèle représentant une commande passée par un client sur le site """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, default='pending')
#     total_price = models.FloatField()
#     shipping_address = models.TextField()

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f'Order {self.id}'
