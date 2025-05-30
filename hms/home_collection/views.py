from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.decorators import role_required
from .models import CollectionRequest
from .forms import CollectionRequestForm  
from users.models import User

# Handle circular imports if necessary
def role_required(*allowed_roles):
    from django.http import HttpResponseForbidden
    from django.shortcuts import redirect
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.role in allowed_roles or request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
                return HttpResponseForbidden("You don't have permission to access this page.")
            return redirect('login')
        return wrapper
    return decorator

@login_required
@role_required('HOME_COLLECT')
def home_collection_dashboard(request):
    pending_requests = CollectionRequest.objects.filter(status='requested').count()
    scheduled_requests = CollectionRequest.objects.filter(status='scheduled').count()
    recent_requests = CollectionRequest.objects.order_by('-preferred_date')[:5]
    
    return render(request, 'home_collection/dashboard.html', {
        'pending_requests': pending_requests,
        'scheduled_requests': scheduled_requests,
        'recent_requests': recent_requests
    })

@login_required
@role_required('HOME_COLLECT')
def request_list(request):
    requests = CollectionRequest.objects.all().order_by('-preferred_date')
    return render(request, 'home_collection/request_list.html', {'requests': requests})

@login_required
@role_required('HOME_COLLECT')
def create_request(request):
    if request.method == 'POST':
        form = CollectionRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.save()
            form.save_m2m()  # Save many-to-many data
            return redirect('home_collection:request_detail', pk=request_obj.pk)
    else:
        form = CollectionRequestForm()
    
    return render(request, 'home_collection/request_form.html', {'form': form})

@login_required
@role_required('HOME_COLLECT')
def request_detail(request, pk):
    collection_request = get_object_or_404(CollectionRequest, pk=pk)
    return render(request, 'home_collection/request_detail.html', {'request': collection_request})

@login_required
@role_required('HOME_COLLECT')
def update_request(request, pk):
    collection_request = get_object_or_404(CollectionRequest, pk=pk)
    if request.method == 'POST':
        form = CollectionRequestForm(request.POST, instance=collection_request)
        if form.is_valid():
            form.save()
            return redirect('home_collection:request_detail', pk=pk)
    else:
        form = CollectionRequestForm(instance=collection_request)
    
    return render(request, 'home_collection/request_update.html', {
        'form': form,
        'request': collection_request
    })

@login_required
@role_required('HOME_COLLECT')
def collect_sample(request, pk):
    collection_request = get_object_or_404(CollectionRequest, pk=pk)
    if collection_request.status in ['requested', 'scheduled']:
        collection_request.status = 'collected'
        collection_request.collector = request.user
        collection_request.save()
    return redirect('home_collection:request_detail', pk=pk)