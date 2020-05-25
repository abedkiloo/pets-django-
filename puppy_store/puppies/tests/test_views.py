import json
from pprint import pprint
from unittest import TestCase

from django.test import Client
from django.urls import reverse
from rest_framework import status

from ..models import Puppies
from ..serializer import PuppySerializer

# initialize the APIClient app
client = Client()


class GetAllPuppies(TestCase):
    def setUp(self):
        Puppies.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppies.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppies.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        Puppies.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse("get_post_puppies"))
        # get data from db
        puppies = Puppies.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppy(TestCase):
    def setUp(self):
        self.casper = Puppies.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppies.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        self.rambo = Puppies.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        self.ricky = Puppies.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_valid_single_puppy(self):
        response = client.get(reverse("get_delete_update_puppy", kwargs={'pk': self.rambo.pk}))
        pprint(self.rambo.pk)

        puppy = Puppies.objects.get(pk=self.rambo.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def get_invalid_first_puppy(self):
        response = client.get(
            reverse("get_delete_update_puppy", kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPuppyTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': '4',
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePuppy(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppy.objects.create(
            name='Muffy', age=1, breed='Gradane', color='Brown')
        self.valid_payload = {
            'name': 'Muffy',
            'age': 2,
            'breed': 'Labrador',
            'color': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_update_single_valid_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_single_invalid_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppy(TestCase):

    def setUp(self):
        self.casper = Puppies.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppies.objects.create(
            name='Muffy', age=1, breed='Gradane', color='Brown')

    def test_valid_delete_single_puppy(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={"pk": self.muffin.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_puupy_delete(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={"pk": 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
