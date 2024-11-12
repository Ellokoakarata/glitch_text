import random

def zalgo_generator(texto_entrada):
    # Caracteres para superposición, medio y subposición
    zalgo_chars_super = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
        '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B',
        '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311',
        '\u0312', '\u0313', '\u0314'
    ]
    zalgo_chars_medio = [
        '\u0315', '\u0316', '\u0317', '\u0318', '\u0319'
    ]
    zalgo_chars_sub = [
        '\u031A', '\u031B', '\u031C', '\u031D', '\u031E', '\u031F',
        '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325',
        '\u0326', '\u0327', '\u0328', '\u0329', '\u032A', '\u032B',
        '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331',
        '\u0332', '\u0333', '\u0334', '\u0335', '\u0336', '\u0337',
        '\u0338', '\u0339', '\u033A', '\u033B', '\u033C', '\u033D',
        '\u033E', '\u033F', '\u0340', '\u0341', '\u0342', '\u0343',
        '\u0344', '\u0345', '\u0346', '\u0347', '\u0348', '\u0349',
        '\u034A', '\u034B', '\u034C', '\u034D', '\u034E', '\u034F',
        '\u0350', '\u0351', '\u0352', '\u0353', '\u0354', '\u0355',
        '\u0356', '\u0357', '\u0358', '\u0359', '\u035A', '\u035B',
        '\u035C', '\u035D', '\u035E', '\u035F', '\u0360', '\u0361', '\u0362'
    ]

    # Función para agregar caracteres Zalgo a un caracter
    def agregar_zalgo_caracter(char):
        num_chars_super = random.randint(5, 12)  # Más caracteres en la parte superior
        num_chars_medio = random.randint(3, 5)  # Pocos caracteres en el medio
        num_chars_sub = random.randint(6, 12)    # Más caracteres en la parte inferior

        # Añadir caracteres Zalgo
        for _ in range(num_chars_super):
            char += random.choice(zalgo_chars_super)
        for _ in range(num_chars_medio):
            char += random.choice(zalgo_chars_medio)
        for _ in range(num_chars_sub):
            char += random.choice(zalgo_chars_sub)

        return char

    # Generar texto Zalgo
    salida_zalgo = ''.join([agregar_zalgo_caracter(char) for char in texto_entrada])

    return salida_zalgo

# Ejemplo de uso
entrada_usuario = """
Elevado
"""
salida_zalgo_mejorado = zalgo_generator(entrada_usuario)
print(salida_zalgo_mejorado)
