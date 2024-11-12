# Code sous forme de chaîne de caractères (le code de ta fonction)
code = """
def ma_fonction(x, y):
    return x + y
"""

# Utilisation de exec() pour exécuter le code
exec(code)

# Maintenant la fonction est définie, tu peux l'utiliser
resultat = ma_fonction(5, 3)
print(resultat)  # Affiche 8
