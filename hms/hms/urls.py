from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', include('core.urls')),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # App URLs with namespaces
    path('users/', include('users.urls', namespace='users')),
    path('reception/', include('reception.urls', namespace='reception')),
    path('doctor/', include('doctor.urls', namespace='doctor')),
    path('lab/', include('lab.urls', namespace='lab')),
    path('finance/', include('finance.urls', namespace='finance')),
    path('home-collection/', include('home_collection.urls', namespace='home_collection')),
    path('', include('website.urls', namespace='website')),
]