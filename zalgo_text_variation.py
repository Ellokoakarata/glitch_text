import random
import unicodedata
import datetime

def expanded_zalgo_chars():
    """
    Generate a list of zalgo characters from various Unicode ranges,
    excluding specific characters that do not display correctly.
    """
    # Define the ranges and exclude specific characters
    excluded_chars = {0x1ABE}  # Agrega los códigos Unicode de los caracteres a excluir
    zalgo_chars = [chr(i) for i in range(0x0300, 0x036F) if i not in excluded_chars] + \
                  [chr(i) for i in range(0x1AB0, 0x1AFF) if i not in excluded_chars] + \
                  [chr(i) for i in range(0x1DC0, 0x1DFF) if i not in excluded_chars]
    return zalgo_chars

def add_zalgo_chars(char, intensity=1):
    """
    Adds a minimal number of zalgo characters to a single character, focusing on visual clarity.
    """
    num_chars = random.randint(0, 1)  # Minimal characters for clarity
    zalgo_chars = expanded_zalgo_chars()
    tachado = '\u0336'  # Combining Long Stroke Overlay for strike-through effect
    modified_char = char + tachado
    for _ in range(num_chars):
        modified_char += random.choice(zalgo_chars)
    return modified_char

def zalgo_text(text, intensity=1):
    """
    Generate zalgo text with an emphasis on readability and aesthetic balance.
    """
    zalgo_text = ""
    for char in text:
        if char != " " and unicodedata.category(char) != 'Cc':
            zalgo_text += add_zalgo_chars(char, intensity)
        else:
            zalgo_text += char
    return zalgo_text

def create_artistic_text(text_blocks):
    """
    Creates an artistic text output combining readable zalgo text with ASCII blocks.
    """
    intensity_levels = [1]  # Consistent low intensity for all text
    ascii_blocks = ["░▒▒▓▓", "▓▓▒▒░"]
    artistic_text = ""

    for i, text in enumerate(text_blocks):
        # Apply consistent zalgo with low intensity
        zalgoed_text = zalgo_text(text, intensity_levels[0])
        # Add ASCII blocks around the text
        artistic_text += f"{ascii_blocks[i % len(ascii_blocks)]} {zalgoed_text} {ascii_blocks[i % len(ascii_blocks)]}\n"

    return artistic_text

def save_zalgo_output(text_blocks):
    """
    Saves and prints the zalgo text to a file with a timestamp, using UTF-8 encoding,
    with a separator line between entries. Handles errors and prints the result.
    """
    try:
        artistic_text = create_artistic_text(text_blocks)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        separator = "-" * 60  # 60 dashes as a separator
        with open("outputs_zalgo_text.txt", "a", encoding='utf-8') as file:
            file_content = f"{timestamp}\n{artistic_text}\n{separator}\n\n"
            file.write(file_content)
            print("Text saved successfully.")
        # Print the artistic text to the console
        print("Generated Artistic Text:")
        print(artistic_text)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")



# List of phrases to be transformed
text_blocks = [
    "Psycho Dreams",
    "Spirtual chaos",
    "Destruction and love"
  
]

# Example usage
save_zalgo_output(text_blocks)
