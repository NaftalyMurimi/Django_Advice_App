from django.urls import path
from adv import views
urlpatterns = [
    
    path('', views.adv, name="adv"),
    path('signup/', views.signup, name="signup"), 
    path('login/', views.login, name="login")

]
