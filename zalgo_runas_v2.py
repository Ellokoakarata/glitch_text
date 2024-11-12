import random
import datetime
import os
import unicodedata

def transformar_poema_estilo_gotico(poema_entrada):
    # Define caracteres Zalgo para arriba y abajo
    zalgo_arriba = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
        '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B'
    ]
    zalgo_abajo = [
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B',
        '\u0320', '\u0321', '\u0323', '\u0324', '\u0325', '\u0326'
    ]
    
    # Carácteres góticos que reemplazarán algunas letras
    caracteres_goticos = {
        'A': '𝕬', 'B': '𝕭', 'C': '𝕮', 'D': '𝕯', 'E': '𝕰', 'F': '𝕱', 'G': '𝕲',
        'H': '𝕳', 'I': '𝕴', 'J': '𝕵', 'K': '𝕶', 'L': '𝕷', 'M': '𝕸', 'N': '𝕹',
        'O': '𝕺', 'P': '𝕻', 'Q': '𝕼', 'R': '𝕽', 'S': '𝕾', 'T': '𝕿', 'U': '𝖀',
        'V': '𝖁', 'W': '𝖂', 'X': '𝖃', 'Y': '𝖄', 'Z': '𝖅',
        'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊', 'f': '𝖋', 'g': '𝖌',
        'h': '𝖍', 'i': '𝖎', 'j': '𝖏', 'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓',
        'o': '𝖔', 'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙', 'u': '𝖚',
        'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟'
    }
    
    # Función para aplicar efectos aleatorios
    def aplicar_estilo_gotico(char):
        if char in caracteres_goticos:
            char = caracteres_goticos[char]  # Reemplaza por el carácter gótico
        
        # Aplica caracteres Zalgo arriba y abajo en base a una variación aleatoria
        parte_arriba = ''.join(random.choice(zalgo_arriba) for _ in range(random.randint(1, 3)))
        parte_abajo = ''.join(random.choice(zalgo_abajo) for _ in range(random.randint(1, 3)))
        return f"{parte_arriba}{char}{parte_abajo}"

    # Transforma cada carácter en el poema
    poema_transformado = ""
    for char in poema_entrada:
        poema_transformado += aplicar_estilo_gotico(char) if char.isalnum() else char

    return poema_transformado

def guardar_poema_transformado(poema_entrada):
    # Transforma el poema
    poema_transformado = transformar_poema_estilo_gotico(poema_entrada)
    
    # Prepara el contenido a guardar con fecha y hora
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separador = '-' * 70
    contenido_a_guardar = f"{fecha_hora}\n{poema_transformado}\n{separador}\n\n"
    
    # Verificar si el archivo existe, si no, crearlo
    archivo_path = "poema_transformado_gotico.txt"
    if not os.path.exists(archivo_path):
        open(archivo_path, 'w', encoding='utf-8').close()  # Crea el archivo vacío si no existe
    
    # Escribir el poema en el archivo
    with open(archivo_path, "a", encoding='utf-8') as archivo:
        archivo.write(contenido_a_guardar)

    return poema_transformado

# Ejemplo de uso
poema_entrada = """En la penumbra de mis pensamientos,
las sombras se retuercen y caen.
El caos murmura su verdad,
mientras la razón se desvanece."""

# Guardar y mostrar el poema transformado
poema_estilo_gotico = guardar_poema_transformado(poema_entrada)
print(poema_estilo_gotico)
