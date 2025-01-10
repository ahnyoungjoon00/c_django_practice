from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def sign_in(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
    return render(request, "users_app/sign_in.html", {"form":form})

def sign_out(request):
    logout(request)
    return redirect("index")