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
    path('client/<str:id>',views.client_controller, name='client_controller'),
    path('show-client/<str:id>',views.client_view, name='client_view'),
    path('show-order/<str:id>',views.order_view, name='order_view'),
    path('reports',views.show_reports, name='show_reports'),
    path('product/<str:id>', views.product_controller, name='product_controller'),
]