from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('reports/', views.reports, name='reports'),
    path('home-collection/', views.home_collection_request, name='home_collection_request'),
]