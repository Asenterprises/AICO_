```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('erp_system.users.urls')),
    path('production/', include('erp_system.production.urls')),
    path('quality/', include('erp_system.quality.urls')),
    path('warehouse/', include('erp_system.warehouse.urls')),
]
```