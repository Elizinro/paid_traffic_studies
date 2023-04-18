import json
import os
import requests
from django.conf import settings

class LibraryUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        imports_method = ["header_imports", "additional_imports"]
        for import_method in imports_method:
            with open(f'{os.path.dirname(__file__)}/{import_method}.json') as json_file:
                libraries = json.load(json_file)

            imports = []
            for library in libraries:
                try:
                    requests.head(library['href'], timeout=settings.URL_TIMEOUT)
                    library_url_valid = True
                except requests.exceptions.RequestException:
                    library_url_valid = False
                library['valid'] = library_url_valid
                imports.append(library)
            setattr(request, f"{import_method}", imports)
            #request.header_imports = imports

        response = self.get_response(request)
        return response