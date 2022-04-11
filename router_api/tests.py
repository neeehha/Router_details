from django.test import TestCase

# Create your tests here.
from router_api.models import router_details
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .views import *
from rest_framework.test import APIClient


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('create-router')
        data = {"sapid": "33744", "hostname":"test_system11", "loopback":"127.0.0.1", "macaddress":"test_addretttss"}
        client = APIClient()
        response = client.post(url, data, format='json')
        client.credentials(HTTP_AUTHORIZATION='Token 5763d5854df9a3348c5e1c0907e0f3aff01c73b2')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieveDetails_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('router-details')
        client = APIClient()
        response=client.get(url)
        client.credentials(HTTP_AUTHORIZATION='Token 5763d5854df9a3348c5e1c0907e0f3aff01c73b2')
        #print("11",response,"22")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(response.objects.count(), 1)