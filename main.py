from generationAlgo.modifAlgov3 import modify_program

import unittest
from test.return0Test import TestReturn0, define_function


def lancer_tests(functionString):

    define_function(functionString)


    # Créer une suite de tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReturn0)
    
    # Exécuter la suite de tests et afficher les résultats
    result = unittest.TextTestRunner().run(suite)
    
    # Vérifier le résultat des tests et renvoyer un statut (optionnel)
    if result.wasSuccessful():
        print("Tous les tests ont réussi.")
    else:
        print(f"Certains tests ont échoué. Nombre d'échecs : {result}")


program_base = """
def return0():
"""
res = modify_program(program_base,1)
exec(res)

print(res)
lancer_tests(res)
