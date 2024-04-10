from django.urls import path
from adv import views
urlpatterns = [
    
    path('', views.adv, name="adv"),
    path('signup/', views.signup, name="signup"), 
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('UserDashboard/', views.UserDashboard, name="UserDashboard"),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf')

]
