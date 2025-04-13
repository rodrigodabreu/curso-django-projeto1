from django.test import TestCase


class RecipeURLsTest(TestCase):
    def test_um_nao_eh_igual_a_dois(self):
        assert 1 == 2 , 'Um não é igual a dois'
    
    def test_um_igual_a_um(self):
        assert 1 == 1 , 'Um é igual a um'