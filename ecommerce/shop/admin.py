from django.contrib import admin
from .models import Category, Product


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_added',)


# Register your models here.
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
