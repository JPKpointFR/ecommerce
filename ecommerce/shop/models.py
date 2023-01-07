from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from ecommerce.settings import AUTH_USER_MODEL

# Create your models here.


class Category(models.Model):
    """ Modèle représentant une catégorie de produits sur le site e-commerce. """
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Modèle de produit représentant un produit disponible à la vente. """
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
        return f"{self.name} - {self.quantity}"

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'product_slug': self.slug})


"""
Article(Order):
- Utilisateur
- Produit
- Quantité
- Commandé ou non
"""


class Order(models.Model):
    """ Modèle représentant une commande passée par un client sur le site """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


"""
Panier(Cart):
- Utilisateur
- Commandé ou non 
- Date de la commande
"""


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}'
