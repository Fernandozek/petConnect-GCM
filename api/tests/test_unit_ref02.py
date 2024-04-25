from api.models import Profile
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.profile = Profile.objects.create(
            user=self.user,
            tipo_usuario='1',
            nome='Fernando',
            endereco='123 Main St',
            cnpj='123456789',
            contato='123-456-7890',
            historico='Lorem ipsum dolor sit amet',
            foto='path/to/image.jpg'
        )

    def test_required_fields(self):
        self.assertIsNotNone(self.profile.user)
        self.assertIsNotNone(self.profile.tipo_usuario)
        self.assertIsNotNone(self.profile.nome)
        self.assertIsNotNone(self.profile.endereco)
        self.assertIsNotNone(self.profile.cnpj)
        self.assertIsNotNone(self.profile.contato)

    def test_password_length(self):
        self.assertGreaterEqual(len(self.profile.user.password), 8)