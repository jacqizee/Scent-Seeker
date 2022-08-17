from django.test import TestCase
from ..models import Accord
# Create your tests here.

class TestAccords(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Accord.objects.create(name = 'Floral')

    def test_model(self):
        self.assertTrue(Accord.objects.get(name='Floral'))