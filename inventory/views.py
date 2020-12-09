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
    return render(request, "inventory/order-list.html",{"orders":orders , "message":"Cargando ordenes..."})


def show_clients(request):

    clients = Client.objects.all()
    return render(request, "inventory/client-list.html",{"clients":clients })