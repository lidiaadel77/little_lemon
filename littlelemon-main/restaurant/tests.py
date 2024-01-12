from django.test import TestCase
from .models import *
# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.price, 80)