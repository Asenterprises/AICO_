```python
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        pass
```