import random

def generate_mysterious_characters(num_characters):
    mysterious_text = ""
    key = random.randint(1, 25)  # Clave para el cifrado Caesar
    for _ in range(num_characters):
        random_unicode = chr(random.randint(0x2000, 0x2fff))
        mysterious_text += chr(ord(random_unicode) + key)

    mysterious_text += f"\n ~ Descifra el misterio (Clave: {key}) ~ "
    return mysterious_text

try:
    num_characters = int(input("Ingresa la cantidad de caracteres misteriosos que deseas generar: "))
    mysterious_text = generate_mysterious_characters(num_characters)
    print("Texto misterioso:\n", mysterious_text)
except ValueError:
    print("Por favor, ingresa un número válido.")
except Exception as e:
    print("¡Hubo un error en la ejecución!\nError:", e)
