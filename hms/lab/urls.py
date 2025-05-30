from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('dashboard/', views.lab_dashboard, name='lab_dashboard'),
    path('tests/', views.test_list, name='test_list'),
    path('tests/new/', views.create_test, name='create_test'),
    path('tests/<int:pk>/', views.test_detail, name='test_detail'),
    path('results/<int:pk>/', views.result_detail, name='result_detail'),
    path('results/<int:pk>/verify/', views.verify_result, name='verify_result'),
]