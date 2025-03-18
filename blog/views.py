from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Car, Cart, CartItem
from django.contrib.auth import logout

# Create your views here.
def car_inventory(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(make__icontains=query)
    else:
        cars = Car.objects.all()
    
    paginator = Paginator(cars, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'dealer.html', {'page_obj': page_obj})

def home(request):
    return render(request, 'home.html')

def logout_and_redirect(request):
    logout(request)
    return redirect("home")

def is_owner(user) :
    return user.is_authenticated and user.is_staff

@user_passes_test(is_owner)
def add_car(request):
    if request.method == 'POST':
        register = request.POST['register']
        make = request.POST['make']
        model = request.POST['model']
        price = request.POST['price']
        year = request.POST['year']
        vin = request.POST['vin']
        Car.objects.create(register=register, make=make, model=model, price=price, year=year, vin=vin)
        return redirect('dealer')
    return render(request, 'add_car.html')

@user_passes_test(is_owner)
def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.register = request.POST['register']
        car.make = request.POST['make']
        car.model = request.POST['model']
        car.price = request.POST['price']
        car.year = request.POST['year']
        car.vin = request.POST['vin']
        car.quantity = request.POST['quantity']
        car.save()
        return redirect('dealer')
    return render(request, 'edit_car.html', {'car': car})

@user_passes_test(is_owner)
def delete_car(request, car_id):
    if request.method == 'POST':
        car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('dealer')

@login_required
def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, car=car)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum([item.car.price * item.quantity for item in cart_items])
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum([item.car.price * item.quantity for item in cart_items])
    if request.method == 'POST':
        # Decrease quantity of cars in inventory
        for item in cart_items:
            item.car.quantity -= item.quantity
            item.car.save()
        # Process payment
        cart_items.delete()
        return redirect('checkout_complete')
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total}) 

def checkout_complete(request):
   return render(request, 'checkout_complete.html')