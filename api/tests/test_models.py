from api.models.interesse import Interesse
import setup_django
from django.test import TestCase
from api.models import Animal, Foto
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from api.models import Profile

class AnimalTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie = "Cachorro",         
            idade = "1 mes",
            tamanho = "pequeno",
            sexo = "M",
            descricao = "Dócil",
            personalidade = "Faminto",
            user = self.usuario)

    def test_model_creation(self):
        self.assertIsInstance(self.animal, Animal)

    def test_model_attributes(self):
        self.assertEqual(self.animal.especie, "Cachorro")
    
    def test_model_methods(self):
        self.assertEqual(self.animal.__str__(), "Cachorro")

class FotoTestCase(TestCase):
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
        self.foto = Foto.objects.create(
            arquivo = 'path/to/image.jpg',
            animal = self.animal
        )

    def test_model_creation(self):
        self.assertIsInstance(self.foto, Foto)

    def test_model_attributes(self):
        self.assertEqual(self.foto.arquivo, 'path/to/image.jpg')
        self.assertEqual(self.foto.animal, self.animal)


class InteresseTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie="Cachorro",
            raca="Pitbull",
            idade="1 mes",
            tamanho="pequeno",
            sexo="M",
            descricao="Dócil",
            personalidade="Faminto",
            user=self.usuario)
        self.interesse = Interesse.objects.create(
            user=self.usuario,
            animal=self.animal
        )
    
    def test_model_creation(self):
        self.assertIsInstance(self.interesse, Interesse)
    
    def test_model_attributes(self):
        self.assertEqual(self.interesse.user, self.usuario)
        self.assertEqual(self.interesse.animal, self.animal)
    
  



class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie="Cachorro",
            raca="Pitbull",
            idade="1 mes",
            tamanho="pequeno",
            sexo="M",
            descricao="Dócil",
            personalidade="Faminto",
            user=self.user
            )
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
        self.interesse = Interesse.objects.create(
            user=self.user,
            animal=self.animal
        )

    def test_model_creation(self):
        self.assertIsInstance(self.profile, Profile)

    def test_model_attributes(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.tipo_usuario, '1')
        self.assertEqual(self.profile.nome, 'Fernando')
        self.assertEqual(self.profile.endereco, '123 Main St')
        self.assertEqual(self.profile.cnpj, '123456789')
        self.assertEqual(self.profile.contato, '123-456-7890')
        self.assertEqual(self.profile.historico, 'Lorem ipsum dolor sit amet')
        self.assertEqual(self.profile.foto, 'path/to/image.jpg')

    def test_model_methods(self):
        self.assertEqual(str(self.profile), 'Fernando')
        self.assertEqual(str(self.interesse), str(self.interesse.id))




