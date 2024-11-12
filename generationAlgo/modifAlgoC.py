import random

# Liste de types de données en C
types = ["int", "float", "char", "double", "long"]

# Liste de noms de variables génériques
variable_names = ["var", "x", "y", "z", "a", "b", "i", "j", "k", "n"]

# Liste d'opérateurs
operators = ["+", "-", "*", "/", "%"]

# Liste de structures de contrôle en C
control_structures = [
    "if", "else", "while", "for", "switch", "case", "return"
]

# Liste de valeurs possibles (pour les int, float, etc.)
values = [10, 25, 50, 100, 3.14, 0.25, -5, 42]

# Fonction pour générer une déclaration de variable aléatoire
def generate_declaration():
    var_type = random.choice(types)
    var_name = random.choice(variable_names)
    return f"{var_type} {var_name} = {random.choice(values)};"

# Fonction pour générer une opération mathématique aléatoire
def generate_operation():
    var1 = random.choice(variable_names)
    var2 = random.choice(variable_names)
    operator = random.choice(operators)
    return f"{var1} = {var1} {operator} {var2};"

# Fonction pour générer une structure de contrôle aléatoire
def generate_control_structure():
    control = random.choice(control_structures)
    
    if control == "if":
        condition = f"{random.choice(variable_names)} > {random.choice(values)}"
        return f"if ({condition}) {{\n    // Do something\n}}"
    
    elif control == "else":
        return "else {\n    // Do something else\n}"
    
    elif control == "while":
        condition = f"{random.choice(variable_names)} < {random.choice(values)}"
        return f"while ({condition}) {{\n    // Loop body\n}}"
    
    elif control == "for":
        init = f"{random.choice(variable_names)} = 0"
        condition = f"{random.choice(variable_names)} < {random.choice(values)}"
        increment = f"{random.choice(variable_names)}++"
        return f"for ({init}; {condition}; {increment}) {{\n    // Loop body\n}}"
    
    elif control == "switch":
        var = random.choice(variable_names)
        case_value = random.choice(values)
        return f"switch ({var}) {{\n    case {case_value}:\n        // Do something\n        break;\n}}"
    
    elif control == "return":
        return f"return {random.choice(values)};"

# Fonction pour générer un programme en C aléatoire
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
    return f"#include <stdio.h>\n\nint main() {{\n" + "\n".join(program) + "\n    return 0;\n}}"

# Générer un programme de 15 instructions aléatoires
random_program = generate_program(15)
print(random_program)
