from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("/admin/")
            
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("home")
            
            else:
                return redirect("home")
        
        else:
            return render(request, "registration/login.html", {"error": "username or password is incorrect"})
    else:
        return render(request, "registration/login.html")
    
def logout_and_redirect(request):
    logout(request)
    return redirect("home")

def back_to_home (request):
    return redirect("home")