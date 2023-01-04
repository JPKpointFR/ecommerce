from django.db import models

# Create your models here.


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
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/')
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name
