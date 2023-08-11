from django.test import TestCase

from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Tiramisu", price=70, inventory=15)
        self.asertEqual(item, "Tiramisu: 70")