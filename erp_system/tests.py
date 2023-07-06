```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from erp_system.production.models import Production
from erp_system.quality.models import Quality
from erp_system.warehouse.models import Warehouse

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

class ProductionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')

    def test_create_production(self):
        production = Production.objects.create(user=self.user, product_name='Noodles', quantity=100)
        self.assertEqual(production.user, self.user)
        self.assertEqual(production.product_name, 'Noodles')
        self.assertEqual(production.quantity, 100)

class QualityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')

    def test_create_quality(self):
        quality = Quality.objects.create(user=self.user, product_name='Noodles', quality_score=8)
        self.assertEqual(quality.user, self.user)
        self.assertEqual(quality.product_name, 'Noodles')
        self.assertEqual(quality.quality_score, 8)

class WarehouseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')

    def test_create_warehouse(self):
        warehouse = Warehouse.objects.create(user=self.user, product_name='Noodles', stock=1000)
        self.assertEqual(warehouse.user, self.user)
        self.assertEqual(warehouse.product_name, 'Noodles')
        self.assertEqual(warehouse.stock, 1000)
```