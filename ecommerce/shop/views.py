from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.


class ProductListView(ListView):
    """ Vue affichant une liste de tous les produits disponibles """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'shop_products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_name'] = self.request.GET.get('item-name')
        return context
