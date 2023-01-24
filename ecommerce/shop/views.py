from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Order
from django.views.generic import ListView, DetailView
from .forms import OrderForm
from django.contrib import messages

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
    order, created = Order.objects.get_or_create(
        user=user, ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    # Redirigez l'utilisateur vers la page actuelle
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart.html', context={'orders': cart.orders.all()})


def delete_cart(request):
    # cart = request.user.cart
    if cart := request.user.cart:
        cart.delete()
    return redirect('shop')


def update_cart(request, product_slug):
    user = request.user
    product = get_object_or_404(Product, slug=product_slug)
    order, _ = Order.objects.get_or_create(
        user=user, product=product, ordered=False)
    order.quantity = request.POST['quantity']
    order.save()
    return redirect('cart')


def delete_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    Order.objects.filter(user=request.user, product=product,
                         ordered=False).delete()
    return redirect('cart')


def checkout(request):
    # Récupérez les informations de commande de l'utilisateur
    orders = Order.objects.filter(user=request.user, ordered=False)
    if request.method == 'POST':
        # Traitez les données du formulaire
        form = OrderForm(request.POST or None)
        if form.is_valid():
            # Enregistrez les informations de commande en base de données
            order = form.save(commit=False)
            order.user = request.user
            order.ordered = True
            order.save()
            # Réinitialisez le panier de l'utilisateur
            user_cart = Cart.objects.get(user=request.user)
            user_cart.orders.clear()
            user_cart.save()
            # Redirigez l'utilisateur vers la page de remerciement
            messages.success(
                request, "Your order has been successfully validated")
            return redirect('shop')
    else:
        # Affichez le formulaire de commande
        form = OrderForm()
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'checkout.html', context)
