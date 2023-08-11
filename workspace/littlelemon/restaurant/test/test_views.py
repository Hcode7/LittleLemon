from django.test import TestCase
from .models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(title="Tiramisu", price=70, inventory=15)

    def test_getall(self):
        item = Menu.objects.all()