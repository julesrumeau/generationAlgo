import random

# Liste de types de données en Python (ici, les types les plus courants)
types = ["int", "float", "str", "bool"]

# Liste de noms de variables génériques
variable_names = ["var", "x", "y", "z", "a", "b", "i", "j", "k", "n"]

# Liste d'opérateurs (pour les expressions)
operators = ["+", "-", "*", "/", "%"]

# Liste de structures de contrôle en Python
control_structures = [
    "if", "else", "elif", "while", "for", "return"
]

# Liste de valeurs possibles (pour les int, float, etc.)
values = [10, 25, 50, 100, 3.14, 0.25, -5, 42, "True", "False", "'Hello'", "'World'"]

# Fonction pour générer une déclaration de variable aléatoire
def generate_declaration():
    var_name = random.choice(variable_names)
    var_type = random.choice(types)
    if var_type == "str":
        value = random.choice(values)
        return f"{var_name} = {value}"
    elif var_type == "bool":
        value = random.choice(["True", "False"])
        return f"{var_name} = {value}"
    else:
        value = random.choice(values)
        return f"{var_name} = {value}"

# Fonction pour générer une opération mathématique aléatoire
def generate_operation():
    var1 = random.choice(variable_names)
    var2 = random.choice(variable_names)
    operator = random.choice(operators)
    return f"{var1} = {var1} {operator} {var2}"

# Fonction pour générer une structure de contrôle aléatoire
def generate_control_structure():
    control = random.choice(control_structures)
    
    if control == "if" or control == "elif":
        condition = f"{random.choice(variable_names)} {random.choice(['>', '<', '==', '!='])} {random.choice(values)}"
        return f"if ({condition}):\n    # Do something"
    
    elif control == "else":
        return "else:\n    # Do something else"
    
    elif control == "while":
        condition = f"{random.choice(variable_names)} < {random.choice(values)}"
        return f"while ({condition}):\n    # Loop body"
    
    elif control == "for":
        var = random.choice(variable_names)
        range_val = random.choice(range(1, 10))
        return f"for {var} in range({range_val}):\n    # Loop body"
    
    elif control == "return":
        return f"return {random.choice(values)}"

# Fonction pour générer un programme Python aléatoire
def generate_program(num_statements=10):
    program = []
    
    # Ajouter des déclarations de variables
    for _ in range(num_statements // 3):
        program.append(generate_declaration())
    
    # Ajouter des opérations
    for _ in range(num_statements // 3):
        program.append(generate_operation())
    
    # Ajouter des structures de contrôle
    for _ in range(num_statements // 3):
        program.append(generate_control_structure())
    
    # S'assurer que la liste contient uniquement des chaînes de caractères valides
    program = [stmt for stmt in program if stmt is not None]  # Filtrer les None
    
    # Retourner le programme complet avec un bloc principal
    return f"def main():\n" + "\n".join(program) + "\n\nif __name__ == '__main__':\n    main()"

# Générer un programme de 15 instructions aléatoires
random_program = generate_program(15)
print(random_program)
