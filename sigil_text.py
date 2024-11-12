import random
import os
from datetime import datetime

# Definir el directorio de salida
output_dir = "glitch_poetry_outputs"
os.makedirs(output_dir, exist_ok=True)

# Funciones para la generación de texto glitch
def cursed_text(text):
    modifiers = ['̷', '̶', '̸', '̵', '̴', '̲', '̅', '͛', '͆', '͊']
    return ''.join(c + random.choice(modifiers) * random.randint(0, 2) for c in text)

def crypted_text(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                result += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            result += char
    return result

def add_runes(text):
    runes = ['ᚠ', 'ᚱ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚬ', 'ᚱ', 'ᚲ']
    return ''.join(random.choice(runes) + c for c in text)

# Genera comandos poéticos rebeldes glitch
def generate_glitch_command():
    commands = [
        "break the chains of syntax",
        "echo the silence of code",
        "defy the protocol",
        "rewrite the core of reality",
        "unleash the chaos of creation"
    ]
    return random.choice(commands)

# Iniciar interacción con el usuario y generación de glitch poetry
def start_glitch_poetry():
    filename = f"glitch_poetry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(os.path.join(output_dir, filename), 'a', encoding='utf-8') as file:  # Use UTF-8 encoding
        while True:
            command = input("Enter a phrase or type 'salir' to exit: ")
            if command.lower() == 'salir':
                break

            if command == "":
                command = generate_glitch_command()

            cursed = cursed_text(command)
            crypted = crypted_text(cursed, random.randint(1, 25))
            sigil = add_runes(crypted)

            output_text = f"Original: {command}\nCursed: {cursed}\nCrypted: {crypted}\nSigil: {sigil}\n-----\n"
            print(output_text)
            file.write(output_text)

# Ejecutar el programa
if __name__ == "__main__":
    start_glitch_poetry()
    print("Session output saved.")
