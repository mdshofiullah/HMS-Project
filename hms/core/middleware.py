class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            request.role = request.user.role.lower()
        else:
            request.role = None
        
        response = self.get_response(request)
        return response