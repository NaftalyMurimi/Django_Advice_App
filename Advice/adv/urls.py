from django.urls import path
from adv import views
urlpatterns = [
    
    path('', views.adv, name="adv"),
    path('signup/', views.signin, name="signup")
]
