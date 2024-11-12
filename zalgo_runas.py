import random
import datetime

def zalgo_runico_extenso(texto_entrada):
    zalgo_chars = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
        '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B',
        '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311',
        '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317',
        '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D',
        '\u031E', '\u031F', '\u0320', '\u0321', '\u0322', '\u0323',
        '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329',
        '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F',
        '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335',
        '\u0336', '\u0337', '\u0338', '\u0339', '\u033A', '\u033B',
        '\u033C', '\u033D', '\u033E', '\u033F', '\u0340', '\u0341',
        '\u0342', '\u0343', '\u0344', '\u0345', '\u0346', '\u0347',
        '\u0348', '\u0349', '\u034A', '\u034B', '\u034C', '\u034D',
        '\u034E', '\u034F', '\u0350', '\u0351', '\u0352', '\u0353',
        '\u0354', '\u0355', '\u0356', '\u0357', '\u0358', '\u0359',
        '\u035A', '\u035B', '\u035C', '\u035D', '\u035E', '\u035F',
        '\u0360', '\u0361', '\u0362'
    ]

    def agregar_zalgo(char, chars, count_range):
        return char + ''.join(random.choice(chars) for _ in range(random.randint(*count_range)))

    salida_zalgo = ''
    for char in texto_entrada.strip():
        char = agregar_zalgo(char, zalgo_chars, (18, 25))
        salida_zalgo += char

    return salida_zalgo

def guardar_salida(texto_entrada):
    salida_zalgo = zalgo_runico_extenso(texto_entrada)
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separador = '-' * 70  # Crea una línea de guiones

    with open("salida_zalgo.txt", "a", encoding='utf-8') as archivo:
        archivo.write(f"{fecha_hora}\n{salida_zalgo}\n{separador}\n\n")

    return salida_zalgo

# Ejemplo de uso
entrada_usuario = """
𝖕̶𝖘̶𝖞̶𝖈̶𝖍̶𝖔̶̭-̶𝖜̶𝖆̶̫𝖞̶
𝖓̶𝖔̶̍-̶̈́𝖗̶̬𝖊̶𝖙̶́𝖚̶̄𝖗̶𝖓̶̀
        """
print(guardar_salida(entrada_usuario))