from django.conf import settings

class ColorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.mw_colors = settings.COLORS
        response = self.get_response(request)
        return response