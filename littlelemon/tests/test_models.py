from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name='Ice', price=80, menu_item_description='A dessert')
        self.assertEqual(str(item), 'Ice : 80')
