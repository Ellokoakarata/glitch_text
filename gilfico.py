import datetime

def create_gothic_text(text):
    """
    Generate text with gothic embellishments and strike-through effect using Unicode characters.
    """
    gothic_decorations = {
        'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊',
        'f': '𝖋', 'g': '𝖌', 'h': '𝖍', 'i': '𝖎', 'j': '𝖏',
        'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓', 'o': '𝖔',
        'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙',
        'u': '𝖚', 'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟'
    }
    strike_through_combining = '\u0336'
    # Decorate each character if it's a letter
    gothic_text = ""
    for char in text.lower():
        if char in gothic_decorations:
            gothic_text += gothic_decorations[char] + strike_through_combining
        else:
            gothic_text += char
    return gothic_text

def frame_and_save_text(text_blocks, file_name):
    """
    Frame the text, save to a file, and print to the console with a single separator for each run.
    """
    separator = '-' * 60  # Line separator for different script executions
    framed_text = ""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_name, "a", encoding='utf-8') as file:
            file.write(f"Timestamp: {timestamp}\n")
            for text in text_blocks:
                embellished_text = create_gothic_text(text)
                framed_text += f"{embellished_text}\n"
            file.write(f"{framed_text}{separator}\n\n")
        print("Text has been successfully saved to", file_name)
    except Exception as e:
        print("An error occurred while saving the file:", e)


    # Print the decorative text to the console
    print("Generated Decorative Text:")
    print(framed_text)

# List of phrases to be transformed and saved
text_blocks = ["Psycho",
                "Way",
                "No-return"]

# Example usage
file_name = "outputs_gothic_text.txt"
frame_and_save_text(text_blocks, file_name)
