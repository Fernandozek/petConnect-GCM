from api.models import Profile, Animal
from django.contrib.auth.models import User
from django.test import TestCase
import requests


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='fernando', password='12345678', is_staff=True, is_superuser=True)
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
        # Test if required fields are not None
        self.assertIsNotNone(self.profile.user)
        self.assertIsNotNone(self.profile.tipo_usuario)
        self.assertIsNotNone(self.profile.nome)
        self.assertIsNotNone(self.profile.endereco)
        self.assertIsNotNone(self.profile.cnpj)
        self.assertIsNotNone(self.profile.contato)

    def test_password_length(self):
        # Test if password length is greater than or equal to 8
        self.assertGreaterEqual(len(self.profile.user.password), 8)

    def test_animal_registration(self):
    # Test if animal registration returns positive result with required data
        animal_data = { 
            "especie":"Cachorro", 
            "raca":"Pitbull", 
            "idade": "1 mes",
            "tamanho":"pequeno",
            "sexo":"M",
            "descricao":"Dócil",
            "personalidade":"Faminto",
            "user": self.user
        }       
        animal= Animal.objects.create(
            especie=animal_data['especie'],
            raca=animal_data['raca'],
            idade=animal_data['idade'],
            tamanho=animal_data['tamanho'],
            sexo=animal_data['sexo'],
            descricao=animal_data['descricao'],
            personalidade=animal_data['personalidade'],
            user=animal_data['user']
        )

        # headers = {'Authorization': f'Token {self.token}'}
        # response = self.client.post('/api/animais/', animal_data, **headers)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(animal.especie, animal_data['especie'])
        self.assertEqual(animal.raca, animal_data['raca'])
        self.assertEqual(animal.idade, animal_data['idade'])
        self.assertEqual(animal.sexo, animal_data['sexo'])
        self.assertEqual(animal.descricao, animal_data['descricao'])
        self.assertEqual(animal.personalidade, animal_data['personalidade'])
        self.assertEqual(animal.user, animal_data['user'])