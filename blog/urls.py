from django.urls import path
from . import views

urlpatterns = [
    path("dealer/", views.car_inventory, name="dealer"),
    path("dealer/add_car/", views.add_car, name="add_car"),
    path("dealer/edit_car/<int:car_id>/",
         views.edit_car, name="edit_car"),
    path("dealer/delete_car/<int:car_id>/",
         views.delete_car, name="delete_car"),
    path("cart/add/<int:car_id>/", 
         views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
#     path("cart/remove/<int:car_id>/",
#          views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("checkout/complete/", views.checkout_complete, name="checkout_complete"),
    path("", views.home, name="home"),
]

