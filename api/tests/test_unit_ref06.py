from api.models import Animal
from django.test import TestCase
from django.contrib.auth.models import User

class AnimalTestCase(TestCase):
    def setUp(self):
        # Create some animals for testing
        self.usuario = User.objects.create_user(username='fernando', password='12345678', is_staff=False, is_superuser=False)
        self.animal = Animal.objects.create(
            especie = "Gato", 
            raca = "Siamês", 
            idade = "2 meses",
            tamanho = "médio",
            sexo = "F",
            descricao = "Brincalhão",
            personalidade = "Curioso",
            user = self.usuario)
        self.animal2 = Animal.objects.create(
            especie = "Cachorro", 
            raca = "Labrador", 
            idade = "1 ano",
            tamanho = "grande",
            sexo = "M",
            descricao = "Amigável",
            personalidade = "Leal",
            user = self.usuario)


    def test_animal_listing(self):
        animals = Animal.objects.all()
        self.assertEqual(len(animals), 2)
        self.assertEqual(animals[0].especie, 'Gato')
        self.assertEqual(animals[0].raca, 'Siamês')
        self.assertEqual(animals[1].especie, 'Cachorro')
        self.assertEqual(animals[1].raca, 'Labrador')