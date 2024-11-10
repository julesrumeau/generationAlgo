import random

# Liste d'instructions assembleur de base (pour x86 dans cet exemple)
instructions = [
    "mov",  # Déplacer des données
    "add",  # Additionner
    "sub",  # Soustraire
    "mul",  # Multiplier
    "div",  # Diviser
    "jmp",  # Sauter à une autre instruction
    "cmp",  # Comparer
    "je",   # Sauter si égal
    "jne",  # Sauter si non égal
    "push", # Pousser une valeur sur la pile
    "pop",  # Retirer une valeur de la pile
    "inc",  # Incrémenter une valeur
    "dec",  # Décrémenter une valeur
    "and",  # Opération ET logique
    "or",   # Opération OU logique
    "xor",  # Opération XOR
]

# Liste de registres pour x86
registres = [
    "eax", "ebx", "ecx", "edx", "esi", "edi", "esp", "ebp"
]

# Liste de valeurs immédiates
immediates = [f"{random.randint(1, 255)}", "0xFF", "0x80", "0x00"]

def generate_instruction():
    # Sélectionner une instruction aléatoire
    instr = random.choice(instructions)

    # Si l'instruction nécessite des opérandes
    if instr in ["mov", "add", "sub", "mul", "div", "cmp", "and", "or", "xor"]:
        reg = random.choice(registres)
        value = random.choice(registres + immediates)
        return f"{instr} {reg}, {value}"
    elif instr in ["jmp", "je", "jne"]:
        # Les sauts utilisent une adresse ou un label
        label = f"label_{random.randint(1, 100)}"
        return f"{instr} {label}"
    elif instr in ["push", "pop"]:
        reg = random.choice(registres)
        return f"{instr} {reg}"
    elif instr in ["inc", "dec"]:
        reg = random.choice(registres)
        return f"{instr} {reg}"

    return instr

def generate_program(num_instructions=10):
    program = []
    for _ in range(num_instructions):
        program.append(generate_instruction())
    return "\n".join(program)

# Générer un programme de 10 instructions aléatoires
random_program = generate_program(10)
print(random_program)
