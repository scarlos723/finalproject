from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Client, Order, Product


# Create your views here.
def index (request):

    if request.user.is_authenticated:
        products =  Product.objects.all()
        return render(request,"inventory/index.html",{"products":products})

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
    
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "inventory/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "inventory/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "inventory/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "inventory/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "inventory/register.html")


def orders_view(request):
    products =  Product.objects.all()
    return render(request,"inventory/orders_view.html",{"products":products})


def create_order(request):

    products =  Product.objects.all()

    if request.method == "POST":
        
        clientName = request.POST["name"]
        clientLastname = request.POST["lastname"]
        clientIdentification = int(request.POST["identification"])
        clientTelephone = int (request.POST["telephone"])
        orderTotal = int(request.POST["total"])
        typeOrder = request.POST["type_order"]
        user_id = request.POST["user_id"]
        descript = request.POST["description"]

        cant_list=eval(request.POST["cant_list"])
        if (typeOrder =="Sale"):
            for tp in cant_list:
                productAux = Product.objects.get(pk=tp[0])
                productAux.stock = productAux.stock - tp[1]
                productAux.sold_number = productAux.sold_number + tp[1]
                productAux.save()

        
        
        try:
            clientAux=Client.objects.get(id_number=clientIdentification)
        except:
            print("No se encontro el cliente")
            clientAux = Client.objects.create(name=clientName, lastname=clientLastname, id_number=clientIdentification, tel=clientTelephone)
            clientAux.save()
          

        userAux = User.objects.get(pk=user_id);

        order = Order.objects.create(kind=typeOrder, value=orderTotal, client=clientAux, user=userAux, description=descript)
        order.save()



    return render(request, "inventory/orders_view.html",{"products":products , "message":"Orden Creada"})


def show_orders(request, kind):
    
    orders = Order.objects.filter(kind = kind)
    return render(request, "inventory/order-list.html",{"orders":orders ,"order_type":kind})


def show_clients(request):

    clients = Client.objects.all()
    return render(request, "inventory/client-list.html",{"clients":clients })

def client_controller(request,id):
    
    if request.method == "POST":  #investigate because the PUT method show error:  Forbidden (CSRF token missing or incorrect.): 
        client=Client.objects.get(pk=id)
        client.name = request.POST["name"]
        client.lastname = request.POST["lastname"]
        client.id_number = request.POST["identification"]
        client.tel = request.POST["telephone"]
        client.save()

        print("cliente actualizado")
    else:
        client = Client.objects.get(pk=id)
        client.delete()
        print('cliente eliminado')

    return show_clients(request)

def client_view(request,id):

    client = Client.objects.get(pk=id)
    if request.method == "POST":
        
        client.name = request.POST["name"]
        client.lastname = request.POST["lastname"]
        client.id_number = request.POST["identification"]
        client.tel = request.POST["telephone"]
        client.save()

        print("cliente actualizado")

    orders = Order.objects.filter(client = client)
    
    return render(request, "inventory/show-client.html",{"client":client,"orders":orders})


def order_view(request,id):

    order = Order.objects.get(pk=id)

    if request.method == "POST":

        order.kind = request.POST["order_type"]
        order.value = request.POST["value"]
        order.description = request.POST["description"]
        order.save()

        print("Orden actualizado")
    
    return render(request, "inventory/show-order.html",{"order":order})

def show_reports(request):

    orders=Order.objects.filter(kind="Sale")
    total_sales = 0
    for order in orders:
        total_sales = total_sales + int(order.value)
    
    total_clients = Client.objects.all().count()
    total_quotes = Order.objects.filter(kind="Quote").count()

    products = Product.objects.all()
    stock_prod=0
    sold_prod=0
    for product in products:
        stock_prod = stock_prod + int(product.stock)
        sold_prod = sold_prod + int(product.sold_number)

    return render(request, "inventory/reports.html",{"total_sales":total_sales, "total_clients":total_clients, "total_quotes":total_quotes, "stock_prod":stock_prod, "sold_prod":sold_prod})


def product_controller(request,id):
    
    if request.method == "POST":
        product = Product.objects.get(pk=id)

        product.name = request.POST['name']
        product.model = request.POST['model']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        print("product update")

        product.save()


    return index(request)