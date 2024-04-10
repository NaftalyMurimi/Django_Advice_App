from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import Subscribers, loginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Create your views here.
def adv(request):
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "home.html")


# registration / signup view
def signup(request):
   if request.method == "POST":
       form = Subscribers(request.POST)
       if form.is_valid():
           form.save()
           return redirect("login")
   else:
      form = Subscribers()
   return render(request, "signup.html", {"form": form})

# login/ singIn view
def login(request):
    form = loginForm()
    if request.method =="POST":
        form = loginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('UserDashboard')
                
    return render(request, "login.html", {"form": form})


@login_required(login_url='login')
def UserDashboard(request):
    username = request.user.username
    email = request.user.email
    # return HttpResponse("<h1>My advice app</h1>")
    return render(request, "UserDashboard.html", {'username':username, 'email':email})




def logout(request): 
    auth.logout(request)
    return redirect('adv')





def generate_pdf(request):
    # Create a HttpResponse object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    # Set the filename for download
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    # Create a canvas
    p = canvas.Canvas(response, pagesize=letter)
        # Write text or draw shapes on the canvas
    data = "This is the data you want to print in the PDF."
    p.drawString(100, 750, data)
    # Close the canvas
    p.showPage()
    p.save()
    return FileResponse
