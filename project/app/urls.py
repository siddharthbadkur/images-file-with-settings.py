

from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show/',views.show,name='show')
]