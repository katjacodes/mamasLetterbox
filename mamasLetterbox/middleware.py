"""
Additional middleware
"""

from django.utils.deprecation import MiddlewareMixin


class FixForwardedHostMiddleware(MiddlewareMixin):
    """
    Middleware to fix a CSRF error when running
    the site locally. Code attribution: Benoit Blanchon.
    """

    def process_request(self, request):
        """
        Removes the hostname from the X-Forwarded-Host
        """

        forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST')
        if forwarded_host:
            # remove port from host:port
            forwarded_host = forwarded_host.split(':')[0]
            request.META['HTTP_X_FORWARDED_HOST'] = forwarded_host
