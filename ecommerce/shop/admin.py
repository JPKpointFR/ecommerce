from django.contrib import admin
from .models import Category, Product, Order, Cart


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added', )


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity', 'date_added',)


class AdminOrder(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'ordered_date',)


class AdminCart(admin.ModelAdmin):
    list_display = ('user',)


# Register your models here.
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(Cart, AdminCart)
