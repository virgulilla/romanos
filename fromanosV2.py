def descomponer(posicion: int, cifra: str) -> int:
    return int(cifra) * 10 ** posicion

def traducir(valor: int) -> str:      
    simbolos = {
        1: 'L', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
        100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
        900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'
    }

    return simbolos[valor]

def a_romanos(numero: int) -> str:
    lista_traducciones = []
    numero_str = str(numero)
    for posicion, cifra in enumerate(numero_str[::-1]):
        valor = descomponer(posicion, cifra)
        # valor = lambda p, c: int(c) * 10 ** p
        valor_traducido = traducir(valor)   
        lista_traducciones.append(valor_traducido)     
    
    lista_traducciones_inverso = lista_traducciones[::-1]
    num_romano = ""
    for simbolo in lista_traducciones_inverso:
        num_romano += simbolo
    
    return num_romano
