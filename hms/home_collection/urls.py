from django.urls import path
from . import views

app_name = 'home_collection'

urlpatterns = [
    path('dashboard/', views.home_collection_dashboard, name='home_collection_dashboard'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/new/', views.create_request, name='create_request'),
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),
    path('requests/<int:pk>/update/', views.update_request, name='update_request'),
    path('requests/<int:pk>/collect/', views.collect_sample, name='collect_sample'),
]