# Create your tests here.
from unittest import TestCase

from ..models import Puppies


class PuppyTest(TestCase):
    def setUp(self):
        Puppies.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppies.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown'
        )

    def test_puppy_breed(self):
        puppy_casper = Puppies.objects.get(name="Casper")
        puppy_muffin = Puppies.objects.get(name="Muffin")
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
