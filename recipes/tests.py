from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    # def test_um_nao_eh_igual_a_dois(self):
    #     assert 1 == 2 , 'Um não é igual a dois'
    
    # def test_um_igual_a_um(self):
    #     assert 1 == 1 , 'Um é igual a um'

    # o nome do test deve sempre começar com test_
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/'), 'A URL de home deve ser a /'