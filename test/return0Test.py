# test_mon_module.py

import unittest

# Méthode pour définir une fonction à partir d'une chaîne de caractères
def define_function(functionString):
    # Exécuter la chaîne de caractères pour définir la fonction dans le contexte global passé
    exec(functionString, globals())


# Classe de test qui va vérifier le comportement de return0()
class TestReturn0(unittest.TestCase):
    
    def test_return0(self):
        # Assurer que la fonction est définie avant de la tester
        self.assertEqual(return0(), 0)  # Vérifie que return0() renvoie bien 0
        
    def test_return_not_1(self):
        self.assertNotEqual(return0(), 1)  # Vérifie que return0() ne renvoie pas 1

# Point d'entrée pour lancer les tests
if __name__ == '__main__':
    unittest.main()
