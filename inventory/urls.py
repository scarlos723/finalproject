from django.urls import path
from . import views # "." del directorio actual improte views

urlpatterns = [

    path('', views.index ,  name='index'), #si no se pone "/" arroja un error de que no encuentra la ruta
    path('login',views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path('register',views.register, name='register'),
    path('orders',views.orders_view, name='orders'),
    path('create-order',views.create_order, name='create_order'),
    path('order-list/<str:kind>',views.show_orders, name='show_orders'),
    path('client-list',views.show_clients, name='show_clients'),
    path('order-list',views.show_orders, name='show_orders'),
]