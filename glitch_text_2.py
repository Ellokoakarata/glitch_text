import random

def generate_glitch_text(input_text):
    glitched_text = ""
    for char in input_text:
        if random.random() < 0.6:  # Mayor probabilidad de glitch
            if random.random() < 0.5:  # 30% de probabilidad de modificar Unicode
                # Reemplazar con caracteres específicos
                glitched_text += ", †, (◕‿◕),Җ"# Puedes ajustar esto para diferentes caracteres
            else:
                continue  # Omitir el carácter actual para simular eliminación
        else:
            glitched_text += char

    # Agregar o eliminar caracteres al azar al final
    for _ in range(random.randint(0, 10)):
        # Reemplazar con caracteres específicos
        glitched_text += ""  # Puedes ajustar esto para diferentes caracteres

    return glitched_text

try:
    # Texto proporcionado directamente
    provided_text = "Esto es una locura de auto-complacencia..."

    # Generar glitch art
    glitched_text = generate_glitch_text(provided_text)

    # Mostrar el glitch art generado
    print("Texto original:")
    print(provided_text)
    print("\nGlitch art generado:")
    print(glitched_text)
except Exception as e:
    print("¡Hubo un error en la ejecución!\nError:", e)
