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
values = [1, -1, 10, 25, 50, 100, 3.14, 0.25, -5, 42, "True", "False", "'Hello'"]
variable_names_used = []
# Fonction pour générer une déclaration de variable aléatoire
def generate_declaration():
    global variable_names_used
    var_name = random.choice(variable_names)
    variable_names_used.append(var_name)
    var_type = random.choice(types)
    if var_type == "str":
        value = random.choice(values)
        return f"    {var_name} = {value}"
    elif var_type == "bool":
        value = random.choice(["True", "False"])
        return f"    {var_name} = {value}"
    else:
        value = random.choice(values)
        return f"    {var_name} = {value}"

# Fonction pour générer une opération mathématique aléatoire
def generate_operation():
    var1 = random.choice(variable_names)
    var2 = random.choice(variable_names)
    operator = random.choice(operators)
    return f"    {var1} = {var1} {operator} {var2}"

# Fonction pour générer une structure de contrôle aléatoire
def generate_control_structure():
    control = random.choice(control_structures)
    
    if control == "if" or control == "elif":
        condition = f"{random.choice(variable_names)} {random.choice(['>', '<', '==', '!='])} {random.choice(values)}"
        return f"    if ({condition}):\n        {generate_operation()}"
    
    elif control == "else":
        return f"    else:\n        {generate_operation()}"
    
    # TODO gérer les boucles
    # elif control == "while":
    #     condition = f"{random.choice(variable_names)} < {random.choice(values)}"
    #     return f"while ({condition}):\n    # Loop body"
    
    # elif control == "for":
    #     var = random.choice(variable_names)
    #     range_val = random.choice(range(1, 10))
    #     return f"for {var} in range({range_val}):\n    # Loop body"
    
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
    return program

# Fonction pour modifier un programme Python existant
def modify_program(program, num_modifications= 5):
    program_lines = program.split("\n")
    
    for _ in range(num_modifications):
        # Choisir une modification aléatoire à effectuer
        action = random.choice(["add", "modify", "remove"])
        
        if action == "add":
            # Ajouter une nouvelle ligne de code (déclaration, opération ou structure de contrôle)
            new_statement = random.choice([generate_declaration(), generate_operation(), generate_control_structure()])
            program_lines.append(new_statement)
        
        elif action == "modify" and program_lines:
            # Modifier une ligne existante
            line_index = random.randint(0, len(program_lines) - 1)
            line = program_lines[line_index]
            
            # Modifier une déclaration de variable
            if "=" in line:
                parts = line.split("=")
                variable = parts[0].strip()
                new_value = random.choice(values)
                program_lines[line_index] = f"{variable} = {new_value}"
            
            # Modifier une opération mathématique
            elif any(op in line for op in operators):
                parts = line.split("=")
                variable = parts[0].strip()
                operator = random.choice(operators)
                new_operand = random.choice(variable_names)
                program_lines[line_index] = f"{variable} = {variable} {operator} {new_operand}"
        
        elif action == "remove" and program_lines:
            # Supprimer une ligne aléatoire
            line_index = random.randint(1, len(program_lines) - 1)
            program_lines.pop(line_index)
    
    if len(variable_names_used) == 0:
        program_lines.append(f"    return {random.choice(values)}")
    else :
        program_lines.append(f"    return {random.choice(variable_names_used)}")
    # Recréer le programme après modifications
    return "\n".join(program_lines)

# # Exemple : générer un programme aléatoire
# random_program = "return 0"
# print("Programme initial :\n", random_program)

# # Modifier le programme existant
# modified_program = modify_program(random_program, 5)
# print("\nProgramme modifié :\n", modified_program)
