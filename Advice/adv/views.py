from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adv(request):
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "index.html")