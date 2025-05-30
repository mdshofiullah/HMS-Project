from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'core' 

urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
]