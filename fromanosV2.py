numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def descomponer(posicion: int, cifra: str) -> int:
    return int(cifra) * 10 ** posicion

def traducir(valor: int) -> str:
    pass

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
