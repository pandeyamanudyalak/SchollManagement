from django.urls import path,include
from accounts import views


urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('cretae_user',views.createUser),
    
]
