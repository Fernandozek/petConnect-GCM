from django.test import TestCase
from django.contrib.auth.models import User

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.usuario.email= 'fernando@example.com'  
        self.usuario.save()          
        
    def test_model_creation(self):
        self.assertIsInstance(self.usuario, User)

    def test_required_fields(self):
        self.assertIsNotNone(self.usuario.username)
        self.assertIsNotNone(self.usuario.email)
        self.assertIsNotNone(self.usuario.password)

    def test_password_length(self):
        self.assertGreaterEqual(len(self.usuario.password), 8)

    def test_email_format(self):
        self.assertTrue('@' in self.usuario.email)
        self.assertTrue('.' in self.usuario.email)