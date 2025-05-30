import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

def home(request):
    # For authenticated users, redirect to dashboard
    if request.user.is_authenticated:
        # Use the namespaced URL: 'core:dashboard'
        return redirect('core:dashboard')
    # For anonymous users, show the home page
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    role = request.user.role.lower()
    template_name = f'core/dashboards/{role}_dashboard.html'
    
    # Check if the template exists
    template_path = os.path.join(settings.BASE_DIR, 'templates', template_name)
    
    if not os.path.exists(template_path):
        # Use default dashboard if role-specific template doesn't exist
        template_name = 'core/dashboards/default_dashboard.html'
    
    return render(request, template_name)