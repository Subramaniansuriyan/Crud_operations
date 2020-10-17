from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Member

class MemberTest(APITestCase):
    def test_positive_member_create(self):

        url = reverse('add_member')
        data = {'firstname': 'John','lastname':'Doe','phonenumber':"1234567890","email":"test@testing.com","role":"true"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 1)
        self.assertEqual(Member.objects.get().firstname, 'John')
    
    def test_negative_member_create(self):

        url = reverse('add_member')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)