from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adv(request):
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "home.html")

def signin(request):
   return render(request, "signin.html")