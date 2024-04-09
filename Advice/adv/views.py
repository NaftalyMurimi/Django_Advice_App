from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Subscribers

# Create your views here.
def adv(request):
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "home.html")

def login(request):
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "login.html")

def signup(request):
   if request.method == 'POST':
       form = Subscribers(request.POST)
       if form.is_valid():
           form.save()
           return redirect("login")
   else:
      form = Subscribers()
   return render(request, "signup.html", {"form": form})