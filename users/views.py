from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
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
            if not User.objects.filter(username=form.cleaned_data['username']).exists() and \
            not User.objects.filter(email=form.cleaned_data['email']).exists():
                user = form.save()
                login(request, user)
                return redirect(reverse("dashboard"))
        
        return render(request, "users/register.html",  {"form": CustomUserCreationForm(), "error_message": "Email or Username is not unique"})