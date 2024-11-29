import random
import datetime

# Definir estilos de caracteres (rango Unicode)
CHARACTER_STYLES = {
    "etíope": (0x1200, 0x137F),  # Bloque Etíope
    "glagolítico": (0x2C00, 0x2C5F),  # Bloque Glagolítico
    "runas": (0x16A0, 0x16FF),  # Bloque de Runas
    "latín_moderno": (0x1D400, 0x1D7FF),  # Letras latinas matemáticas
    "antiguo": (0x10300, 0x1032F),  # Escritura Itálica Antigua
}

def generate_glitch_text(text, style="etíope", intensity=1):
    """
    Genera texto glitch personalizado.
    
    :param text: El texto base.
    :param style: El estilo de caracteres (clave del diccionario CHARACTER_STYLES).
    :param intensity: Nivel de distorsión (1-5), controla la cantidad de caracteres reemplazados.
    :return: Texto con efecto glitch.
    """
    if style not in CHARACTER_STYLES:
        raise ValueError(f"Estilo '{style}' no está definido. Usa: {list(CHARACTER_STYLES.keys())}")
    
    char_range = CHARACTER_STYLES[style]
    glitch_text = ""
    
    for char in text:
        if random.random() < intensity / 5:  # Intensidad controla el % de caracteres alterados
            glitch_char = chr(random.randint(*char_range))
            glitch_text += glitch_char
        else:
            glitch_text += char

    return glitch_text

def save_to_file(output_text, file_name="glitch_output.txt"):
    """
    Guarda el texto generado en un archivo con un timestamp y separación.
    
    :param output_text: El texto a guardar.
    :param file_name: El nombre del archivo donde se guardará.
    """
    with open(file_name, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"--- Generado en {timestamp} ---\n")
        file.write(output_text + "\n")
        file.write("\n" + "="*40 + "\n\n")  # Separación entre salidas

# Ejemplo de uso
if __name__ == "__main__":
    text = "Voy eternamente cayendo"
    style = "glagolítico"  # Cambia a "etíope", "runas", etc.
    intensity = 3  # Nivel de distorsión (1 mínimo, 5 máximo)
    
    glitch_text = generate_glitch_text(text, style, intensity)
    print("Texto glitch generado:")
    print(glitch_text)
    
    # Guardar en archivo
    save_to_file(glitch_text)
