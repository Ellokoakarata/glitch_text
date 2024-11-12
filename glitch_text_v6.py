import random

def glitch_text(text):
    glitch_chars = "̵̶̷̸̴̧̨̛̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎͓͔͕͖͙͚͜͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢͢"
    glitched_text = ""
    for char in text:
        if random.random() < 0.9:
            glitched_text += random.choice(glitch_chars)
        glitched_text += char
        if random.random() < 0.8:
            glitched_text += random.choice(glitch_chars)
    return glitched_text

# Ejemplo de uso
original_text = "Misticos que nunca volveran."
glitched_text = glitch_text(original_text)
print("Texto original:")
print(original_text)
print("\nTexto con efecto glitch:")
print(glitched_text)