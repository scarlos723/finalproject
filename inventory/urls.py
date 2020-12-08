from django.urls import path
from . import views # "." del directorio actual improte views

urlpatterns = [

    path('', views.index ,  name='index'), #si no se pone "/" arroja un error de que no encuentra la ruta
    path('login',views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path('register',views.register, name='register'),
    path('orders',views.orders_view, name='orders'),
]