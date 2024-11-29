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

def save_to_file(output_text, style, variation_number, file_name="glitch_output.txt"):
    """
    Guarda el texto generado en un archivo con un timestamp, estilo y número de variación.
    
    :param output_text: El texto a guardar.
    :param style: Estilo de caracteres utilizado.
    :param variation_number: Número de variación para diferenciar las salidas.
    :param file_name: El nombre del archivo donde se guardará.
    """
    with open(file_name, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"--- Variación {variation_number} | Estilo: {style} | Generado en {timestamp} ---\n")
        file.write(output_text + "\n")
        file.write("\n" + "="*50 + "\n\n")  # Separación entre salidas

# Ejemplo de uso con múltiples estilos y variaciones
if __name__ == "__main__":
    text = "VⰲⰮⱙetⱈrⱍaⱞⰤntⱀⰬcaⰴⱑⱂⰿo"  # Texto base personalizado
    styles = ["glagolítico", "etíope", "runas"]  # Diferentes estilos
    intensity = 4  # Alta distorsión
    variations = 3  # Número de variaciones por estilo

    for style in styles:
        for variation in range(1, variations + 1):
            glitch_text = generate_glitch_text(text, style, intensity)
            print(f"Texto glitch generado (Variación {variation}, Estilo '{style}'):")
            print(glitch_text)
            
            # Guardar en archivo
            save_to_file(glitch_text, style, variation)
