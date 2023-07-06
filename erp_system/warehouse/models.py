from django.db import models
from erp_system.users.models import User

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()

class WarehouseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_inventory", "Can view inventory"),
            ("manage_inventory", "Can manage inventory"),
        ]