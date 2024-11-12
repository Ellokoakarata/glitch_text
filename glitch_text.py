import os
import random

def generate_glitch_text(input_text):
    glitched_text = ""
    for char in input_text:
        if random.random() < 0.6:  # Mayor probabilidad de glitch
            if random.random() < 0.6:  # 50% de probabilidad de modificar Unicode
                # Reemplazar con caracteres específicos
                glitched_text += ", †, (◕‿◕),Җ,��,؀"  # Puedes ajustar esto para diferentes caracteres
                glitched_text += " ~ Un secreto oculto ~ "  # ¡Añadido algo enigmático!
            else:
                continue  # Omitir el carácter actual para simular eliminación
        else:
            glitched_text += char

    # Agregar o eliminar caracteres al azar al final
    for _ in range(random.randint(0, 10)):
        # Reemplazar con caracteres específicos
        glitched_text += ""  # Puedes ajustar esto para diferentes caracteres

    glitched_text += "\n ~ Descifra el misterio ~ "  # ¡Añadido un mensaje intrigante!

    return glitched_text

try:
    # Obtén el directorio actual
    current_directory = os.getcwd()

    # Rutas de los archivos
    input_file_path = os.path.join(current_directory, "respuestas_v5.txt")
    output_file_path = os.path.join(current_directory, "glitched_text.txt")

    # Leer el texto desde el archivo de entrada
    with open(input_file_path, "r", encoding="utf-8") as file:
        original_text = file.read()

    # Generar glitch art
    glitched_text = generate_glitch_text(original_text)

    # Guardar el resultado en un nuevo archivo en el mismo directorio
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(glitched_text)

    print("¡El glitch art se generó con éxito y se guardó en", output_file_path, "!")
except Exception as e:
    print("¡Hubo un error en la ejecución!\nError:", e)
