from django.test import TestCase
from ..models import Perfume
import datetime

# Create your tests here.
class TestPerfumeModel(TestCase):
    def test_perfume_okay(self):
        Perfume.objects.create(
            name = 'Dior',
            description = 'this is a description',
            image = 'this is a link',
            released = datetime.datetime.year(2005)
        )
        self.assertTrue(Perfume.objects.get(name='Dior'))

    def test_perfume_empty_fields(self):
        pass