```python
from django.db import models
from erp_system.users.models import User

class Production(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noodle_type = models.CharField(max_length=200)
    quantity = models.IntegerField()
    production_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.noodle_type
```