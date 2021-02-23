from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.devhome,name='dev_home'),
    path('profile/', views.profile,name='dev_profile'),
]
