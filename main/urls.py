from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_view, name='products'),
    path('product/<int:id>/', views.product_view, name='product'),
    path(
        'product/<int:id>/add/',
        views.basket_add_view,
        name='add_to_basket'
    ),
    path(
        'product/<int:id>/quantity/',
        views.basket_quantity_change_view,
        name='basket_quantity_change'
    ),
    path('basket/', views.basket_view, name='basket'),
    path('basket/clear/', views.basket_clear_view, name='basket_clear'),
    path('order/', views.order_view, name='make_order'),
    path('order/<int:id>/', views.get_order_view, name='get_order'),
    path(
        'order/<int:id>/cancel',
        views.cancel_order_view,
        name='cancel_order'
    ),
]
