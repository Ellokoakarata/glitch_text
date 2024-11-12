import random
import datetime

def expanded_zalgo_chars():
    """
    Generate a list of zalgo characters from various Unicode ranges, focusing on a minimal effect.
    """
    zalgo_chars = [chr(i) for i in range(0x0300, 0x0350)]  # Reduced range for less visual clutter
    return zalgo_chars

def create_gothic_zalgo_text(text):
    """
    Generate text with gothic embellishments, a minimal zalgo effect, and a strike-through effect.
    """
    gothic_decorations = {
        'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊',
        'f': '𝖋', 'g': '𝖌', 'h': '𝖍', 'i': '𝖎', 'j': '𝖏',
        'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓', 'o': '𝖔',
        'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙',
        'u': '𝖚', 'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟'
    }
    strike_through_combining = '\u0336'  # Combining Long Stroke Overlay
    zalgo_chars = expanded_zalgo_chars()
    gothic_text = ""
    for char in text.lower():
        decorated_char = gothic_decorations.get(char, char)  # Get gothic or the char itself
        if char != ' ':
            # Add minimal zalgo effect randomly and always add strike-through
            decorated_char += (random.choice(zalgo_chars) if random.random() < 0.5 else '') + strike_through_combining
        gothic_text += decorated_char
    return gothic_text

def frame_and_save_text(text_blocks, file_name):
    """
    Frame the text, save to a file, and print to the console with a single separator for each run.
    """
    separator = '-' * 60  # Line separator for different script executions
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_name, "a", encoding='utf-8') as file:
            file.write(f"Timestamp: {timestamp}\n")
            for text in text_blocks:
                embellished_text = create_gothic_zalgo_text(text)
                file.write(f"{embellished_text}\n")
            file.write(f"{separator}\n\n")  # Separator after each execution, not each text entry
        print("Text has been successfully saved to", file_name)
    except Exception as e:
        print("An error occurred while saving the file:", e)

    # Print the decorative text to the console
    print("Generated Decorative Text:")

# List of phrases to be transformed and saved
text_blocks = ["𒌸𒑥𒐹𒐸𒑥𒌸𒌸𒑥𒐹𒐸𒑥𒌸𒌸𒑥", "𒌸𒑥𒐹𒐸𒑥𒌸𒌸𒑥𒐹𒐸𒑥𒌸𒌸𒑥"]

# Example usage
file_name = "outputs_gothic_zalgo_text.txt"
frame_and_save_text(text_blocks, file_name)
