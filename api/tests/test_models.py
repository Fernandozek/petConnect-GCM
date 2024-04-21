import setup_django
from django.test import TestCase
from api.models import Animal
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
### Teste do modelo Sala
class AnimalTestCase(TestCase):

    ### Configuração do teste
    def setUp(self):
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie = "Cachorro", 
            raca = "Pitbull", 
            idade = "1 mes",
            tamanho = "pequeno",
            sexo = "M",
            descricao = "Dócil",
            personalidade = "Faminto",
            user = self.usuario)
    ### Teste de criação do modelo
    def test_model_creation(self):
        self.assertIsInstance(self.animal, Animal)

    ### Teste de atributos do modelo
    def test_model_attributes(self):
        self.assertEqual(self.animal.especie, "Cachorro")
    
    def test_model_methods(self):
        self.assertEqual(self.animal.__str__(), "Cachorro")