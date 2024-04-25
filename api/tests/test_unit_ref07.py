from api.models import Animal, Interesse
from django.test import TestCase
from django.contrib.auth.models import User

class AdocaoTestCase(TestCase):
    def setUp(self):
        # Create a user and an animal for testing
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie="Gato",
            raca="Siamês",
            idade="2 meses",
            tamanho="médio",
            sexo="F",
            descricao="Brincalhão",
            personalidade="Curioso",
            user=self.usuario
        )
  
    def test_solicitacao_adocao(self):
        adocao = Interesse.objects.create(animal=self.animal, user=self.usuario)
        self.assertIsInstance(adocao, Interesse)