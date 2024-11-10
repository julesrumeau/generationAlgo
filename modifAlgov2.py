import ast
import random

# Mapping pour des suggestions de tokens en fonction de l'erreur
token_suggestions = {
    "unexpected EOF while parsing": ["0", "''", "()", "[]", "{}", "pass"],
    "invalid syntax": ["+", "-", "*", "/", "=", "==", "(", ")", "[", "]" , "5"]
    # Ajoute plus de modèles ici selon les besoins
}


def suggest_token_for_syntax_error(code_str, error_msg):
    # Teste chaque suggestion et vérifie si elle résout l'erreur de syntaxe
    for err_type, suggestions in token_suggestions.items():
        if err_type in error_msg:
            random.shuffle(suggestions)  # Mélange les suggestions pour tester au hasard
            for token in suggestions:
                # Essayer d'insérer le token et de voir si cela corrige l'erreur
                modified_code = code_str + token  # Essaye d'ajouter le token à la fin du code
                try:
                    ast.parse(modified_code)  # Teste la validité du code
                    print(f"Token valide trouvé : {token}")
                    return token  # Retourne un token valide
                except SyntaxError as e:
                    continue  # Si l'erreur persiste, teste le prochain token
    
    # Si aucun token ne fonctionne, retourne un message d'erreur
    return "Erreur : Aucun token valide trouvé."


def try_parsing_and_suggest_tokens(code_str):
    try:
        ast.parse(code_str)
        print("Code valide")
        return "ok"
    except SyntaxError as e:
        print(f"Erreur de syntaxe : {e}")
        suggested_token = suggest_token_for_syntax_error(code_str, e.msg)
        if suggested_token:
            print(f"Suggestion de token : {suggested_token}")
        return suggested_token

# Exemple
code = """
x = 
"""

suggested_token = try_parsing_and_suggest_tokens(code)
print("Token suggéré pour la correction :", suggested_token)
