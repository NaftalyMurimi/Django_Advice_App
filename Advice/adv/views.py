from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import Subscribers, loginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from reportlab.lib.units import inch
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages





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



#logout view
def logout(request): 
    auth.logout(request)
    return redirect('adv')

#user profile change
def userprofile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('UserDashboard')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'userprofile.html', {'form': form})

# password change view
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update the session
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': form})

# genarate pdf view
def generate_pdf(request):
    # Render your HTML template (replace 'my_template.html' with your actual template name)
    username = request.user.username
    html_content = render_to_string('UserDashboard.html', {'username':username} )
    # Create a PDF buffer
    pdf_buffer = io.BytesIO()
    # Generate the PDF
    pisa.CreatePDF(html_content, dest=pdf_buffer)
    # Set the response headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="advice.pdf"'
    # Write the PDF content to the response
    response.write(pdf_buffer.getvalue())
    return response














































# import pdfkit
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# import pdfkit
# from pdfkit.api import configuration

# wkhtml_path = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
# def generate_pdf(request):
#     pdf = pdfkit.from_url(request.build_absolute_uri(reverse('UserDashboard')), False, configuration=wkhtml_path)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition']= 'attachment; filename="file.pdf"'
#     return response
    # Render HTML template to string
    # username = request.user.username
    # html_content = render_to_string('UserDashboard.html', {'username': username})
    
    # # Define options for pdfkit (optional)
    # options = {
    #     'page-size': 'A4',
    #     'encoding': "UTF-8",
    # }
    
    # # Convert HTML content to PDF
    # pdf = pdfkit.from_string(html_content, False, options=options)
    
    # # Create HTTP response with PDF content
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="user_dashboard.pdf"'
    
    # return response
# import io
# from reportlab.lib.pagesizes import letter, inch
# from reportlab.pdfgen import canvas
# from django.http import FileResponse
# from django.template.loader import render_to_string

# def generate_pdf(request):
#     # Create a BytesIO buffer for PDF generation
#     buf = io.BytesIO()
#     # Create a canvas object for PDF
#     C = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # Example text to display in the PDF
#     textob = C.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont('Helvetica', 14)
#     lines = [
#         'a', 'b', 'c', 'd'
#     ]
#     for line in lines:
#         textob.textLine(line)
#     C.drawText(textob)
#     # Render HTML template including the image
#     username = request.user.username
#     html_content = render_to_string('UserDashboard.html', { 'username':username})
#     # Draw the HTML content to the PDF
#     C.drawString(100, 700, "This is the HTML content with an image:")
#     C.drawString(100, 680, html_content)
#     # Show and save the page
#     C.showPage()
#     C.save()
#     buf.seek(0)
#     # Return the PDF as a FileResponse
#     return FileResponse(buf, as_attachment=True, filename='advice.pdf')





















































































































# def generate_pdf(request):
#     # # Create a HttpResponse object with PDF content type
#     # response = HttpResponse(content_type='application/pdf')
#     # # Set the filename for download
#     # response['Content-Disposition'] = 'attachment; filename="data.pdf"'
#     # # Create a canvas
#     # p = canvas.Canvas(response, pagesize=letter)
#     #     # Write text or draw shapes on the canvas
#     # data = "This is the data you want to print in the PDF."
#     # p.drawString(100, 750, data)
#     # # Close the canvas
#     # p.showPage()
#     # p.save()
#     # return FileResponse
# def generate_pdf(request):
#     buf =io.BytesIO()
#     C = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob= C.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont('Helvetica', 14)
#     lines = [
#         'a', 'b', 'c', 'd'
#     ]
#     for line in lines:
#         textob.textLine(line)
#     C.drawText(textob)
#     C.showPage()
#     C.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='advice.pdf')