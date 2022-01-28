from django.utils.deprecation import MiddlewareMixin

class FixForwardedHostMiddleware(MiddlewareMixin):
    def process_request(self, request):
        forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST')
        print("forwarded host", forwarded_host)
        if forwarded_host:
            # remove port from host:port
            forwarded_host = forwarded_host.split(':')[0]
            request.META['HTTP_X_FORWARDED_HOST'] = forwarded_host