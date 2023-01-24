from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
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


class Order(models.Model):
    """ Modèle représentant une commande passée par un client sur le site """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    country = models.CharField(max_length=100)
    billing_address = models.CharField(
        max_length=201)
    shipping_address = models.CharField(
        max_length=200)
    ordered_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-ordered_date']

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

    def price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, )

    def __str__(self):
        return f'{self.user.username}'

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)
