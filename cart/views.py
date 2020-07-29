from django.views.generic import DetailView
from .models import Cart


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart/shopping_cart.html"
