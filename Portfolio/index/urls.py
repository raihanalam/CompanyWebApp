from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('authentication/',include('authentication.urls')),
    path('developer/',include('developer.urls'))
]
