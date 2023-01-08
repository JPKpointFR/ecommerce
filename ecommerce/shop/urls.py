from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.ProductListView.as_view(), name='shop'),
    path('product/<str:product_slug>/',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<str:product_slug>/add-to-cart/',
         views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('update-cart/<slug:product_slug>/',
         views.update_cart, name='update_cart'),
    path('delete-from-cart/<slug:product_slug>/',
         views.delete_from_cart, name='delete_from_cart'),
    path('cart/delete/', views.delete_cart, name='delete_cart'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
