from django.http import HttpResponseRedirect
from django.urls import reverse

#redirects admin to dashboard upon attempting to configure urls to login page
class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info == reverse('authlogin') and request.user.is_authenticated and request.user.is_staff:
            return HttpResponseRedirect(reverse('authdashboard'))
        
        return self.get_response(request)