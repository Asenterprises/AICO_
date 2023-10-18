```python
from django.contrib import admin
from .users.models import User
from .production.models import Production
from .quality.models import Quality
from .warehouse.models import Warehouse

# Register your models here.
admin.site.register(User)
admin.site.register(Production)
admin.site.register(Quality)
admin.site.register(Warehouse)
```