def decrypt_mysterious_text(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

# Uso del código de descifrado
ciphertext = " ⏕⤼ⓞ⬒℅⟴⃡ⲯ⹸⪧␓∃⳦┒⧂⁵⍅ⶖ⿋☄₶⩸⭍ⴇ⢷₌⼑⾊⚔☇⻥⚯⽊⣕⋰⃔⨄␽✹⅙⟑ⓛⷣ↼⨍⌲⛜⾓∖␙⼊⅏⠟Ⲳ⛜⺏≙┷✢⏖⎳⢸⯣⑭┓〈⡗⚯➴⩉⋮Ⲟⶶ⓳⁮ⲱ⧾ⶠ≁∭℡⯥ⲁ⨸⋗╎◑⼖"
key = 24
decrypted_text = decrypt_mysterious_text(ciphertext, key)

print("Texto descifrado:\n", decrypted_text)
