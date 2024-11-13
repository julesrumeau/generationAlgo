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


seed = "def return0():"

NOMBRE_POPULATION = 10

def generate_population(seed):
    population = []
    for i in range (NOMBRE_POPULATION):
        code = modify_program(seed, 1)
        population.append(code)
    print(population)


generate_population(seed)
# res = modify_program(program_base,1)
# print(res)
# lancer_tests(res)
