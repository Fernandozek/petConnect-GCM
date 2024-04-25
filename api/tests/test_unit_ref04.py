# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

# class LogoutTestCase(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='fernando', password='12345678')
#         self.client.login(username='fernando', password='12345678')

#     def test_logout(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 200)
#         self.assertFalse('_auth_user_id' in self.client.session)