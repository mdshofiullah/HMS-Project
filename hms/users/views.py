from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from core.decorators import role_required
from django.contrib.auth import get_user_model

User = get_user_model()

@role_required('ADMIN')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = True
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            messages.success(request, f'Successfully created account for {user.get_full_name()}!')
            return redirect('users:profile')  # Redirect to profile instead of user_list
    else:
        form = UserRegistrationForm()
    
    # Only show roles that admins can assign
    form.fields['role'].choices = [
        ('RECEPTION', 'Reception Staff'),
        ('DOCTOR', 'Doctor'),
        ('LAB', 'Lab Technician'),
        ('FINANCE', 'Finance Staff'),
    ]
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

# Placeholder for user list (to be implemented later)
@login_required
@role_required('ADMIN')
def user_list(request):
    messages.info(request, 'User list feature will be implemented soon')
    return redirect('users:profile')

def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out.')
    return redirect('home')