import ast
import random

def getRandomToken():
    allToken = [
        "5", "toto",
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in",
        "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
        "+", "-", "*", "/", "//", "%", "**",
        "==", "!=", "<", "<=", ">", ">=",
        "and", "or", "not",
        "&", "|", "^", "~", ">>", "<<",
        "(", ")", "[", "]", "{", "}", ":", ",", ".",
        "\'", "\"",
        ]
    return random.choice(allToken)

def insert_char_at_position(code_str, line_num, col_num, char_to_insert):
    # Convertit le texte en une liste de lignes
    lines = code_str.splitlines()
    
    # Vérifie que la ligne demandée existe
    if line_num < 1 or line_num > len(lines):
        return "Numéro de ligne en dehors des limites du code"
    
    # Récupère la ligne spécifiée
    line = lines[line_num - 1]
    
    # Vérifie que la colonne demandée est valide pour cette ligne
    if col_num < 1 or col_num > len(line) + 1:
        return "Numéro de colonne en dehors des limites de la ligne"
    
    # Insère le caractère à la position spécifiée
    lines[line_num - 1] = line[:col_num - 1] + char_to_insert + line[col_num - 1:]
    
    # Recombine les lignes en une seule chaîne avec des sauts de ligne
    return "\n".join(lines)


def verifieAlgo(string):
    print(string)
    
    try:
        ast.parse(string)  # Parse le code sans l'exécuter
        print("Pas d'erreur de syntaxe détectée.")
        return "ok"
    except SyntaxError as e:
        print(f"Erreur de syntaxe détectée : ligne {e.lineno}, colonne {e.offset} - {e.msg}")
        return (e.lineno, e.offset)
    except IndentationError as e:
        print(f"Erreur d'indentation détectée : ligne {e.lineno} - {e.msg}")
        return "indentation"
    except Exception as e:
        print(f"Autre erreur détectée : {e}")
        return "Autre erreur"

    

def modifyAlgo(string):
    res = verifieAlgo(string)
    if res == "ok":
        print("vamos")
        print(string)
        return string
    

    if isinstance(res, tuple):
        newToken = getRandomToken()
        string = insert_char_at_position(string, res[0], res[1], newToken)
        # modifyAlgo(string)
        print("isinstance")
        print(string)

    return string

algoVide = """
x =
"""

modifyAlgo(algoVide)