from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:pk>', views.CartDetailView.as_view(), name='detail'),
]
