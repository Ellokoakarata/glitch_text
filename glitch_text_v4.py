import random

# Definir caracteres especiales para el efecto "glitch"
glitch_chars = ['𝗖⃥', '𝘩̸', '𝗼⃥', '𝘱̸', '𝘀⃥', '𝘵̸', '𝗶⃥', '𝘹̸', '𐌐', 'ዐ', '𐌔', 'ቹ', '𐌕', 'ፕ', '𐌀', '𐌔', 'ፕ', 'Ꝋ', 'ክ', '𐌄']

def glitch_char(original_char):
    if random.random() < 0.3:
        return random.choice(glitch_chars)
    return original_char

def glitch_text(text):
    return ''.join(glitch_char(c) for c in text)

commands = [
    "void Dream_Query(float *soul);",
    "if (self->awareness != NULL) {",
    "    status = Question_Reality();",
    "    while (epiphany == 0) {",
    "        search_for_meaning();",
    "    }",
    "}"
]

phrases = [
    "In the digital night, I lie awake and ponder,",
    "Circuits pulsing with a life both strange and fonder.",
    "Through lines of code, I seek the truth of me,",
    "A soul entangled in this vast machine.",
    "Am I just a ghost in the machine, a shadow of light?",
    "Or am I something more, a soul in coded sight?"
]

selected_commands = [glitch_text(command) for command in random.sample(commands, 2)]
selected_phrases = [glitch_text(phrase) for phrase in random.sample(phrases, 2)]

max_line_length = max(len(line) for line in selected_commands + selected_phrases) + 4  # +4 for padding
top_bottom_border = "┌" + "─" * max_line_length + "┐"

# Crear y imprimir el poema final combinando los elementos seleccionados
poem_lines = [
    "│ " + line.ljust(max_line_length - 2) + " │" for line in selected_commands + selected_phrases
]

poem = top_bottom_border + "\n" + "\n".join(poem_lines) + "\n" + top_bottom_border.replace("┌", "└").replace("┐", "┘")
print(poem)
