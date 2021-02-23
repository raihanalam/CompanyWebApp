from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.devlogin, name='login'),
    path('registration/', views.devregistration, name='registration'),
    path('recovery/', views.devrecovery, name='recovery'),
    path('logout/',views.devlogout, name='logout')
]