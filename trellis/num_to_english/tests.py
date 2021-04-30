from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class NumToEnglishTest(APITestCase):
    def test_bad_request(self):
        """
        test handling of bad format
        """
        url = reverse('num_to_english')
        url_params1 = url + '?number=asdf'
        url_params2 = url + '?1234=asdf'
        user = User.objects.create_user(username = 'test_user',
                                        email = 'test_user@test.com',
                                        password = 'test')
        self.client.force_authenticate(user=user)
        response1 = self.client.get(url_params1)
        response2 = self.client.get(url_params2)
        self.assertEqual(response1.json().get('status'), 'fail')
        self.assertEqual(response2.json().get('status'), 'fail')
