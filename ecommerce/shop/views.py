from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Order
from django.views.generic import ListView, DetailView


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'shop_products'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


def add_to_cart(request, product_slug):
    user = request.user
    product = get_object_or_404(Product, slug=product_slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    # Redirigez l'utilisateur vers la page actuelle
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)
