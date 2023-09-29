from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
# Create your views here.
def dashboard(request):
    return render (request, "users/dashboard.html")



def register(request):
    if request.method == "GET":
        context = {
            "form": CustomUserCreationForm()
        }
        return render(request, "users/register.html", context)
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))