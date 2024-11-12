import datetime
import random
import unicodedata

def zalgo_text(text):
    """
    This function takes in text and returns it in a 'zalgo' style.
    Zalgo text is typically generated with combining characters - Unicode characters
    that combine with the previous character to modify its appearance.
    """
    # Characters to add zalgo effect
    zalgo_chars = [chr(i) for i in range(768, 879)]

    def add_zalgo_chars(char):
        """
        Adds a random number of zalgo characters to a single character.
        """
        num_chars = random.randint(5, 15)  # Number of zalgo chars to add
        for _ in range(num_chars):
            char += random.choice(zalgo_chars)
        return char

    # Add zalgo chars to each character in the input text
    zalgo_text = ""
    for char in text:
        if char != " " and unicodedata.category(char) != 'Cc':
            zalgo_text += add_zalgo_chars(char)
        else:
            zalgo_text += char

    return zalgo_text

def save_zalgo_output(text):
    """
    Saves the zalgo text to a file with a timestamp, using UTF-8 encoding,
    with a separator line between entries. Handles errors and prints the result.
    """
    try:
        zalgo_text_result = zalgo_text(text)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        separator = "-" * 60  # 60 dashes as a separator
        with open("outputs_zalgo_text.txt", "a", encoding='utf-8') as file:
            file.write(f"{timestamp}\n{zalgo_text_result}\n{separator}\n\n")
        print("Text saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Example text
original_text = """Low-vomitiv.style.gif"""
save_zalgo_output(original_text)
