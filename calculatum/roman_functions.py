class RomanNumberError(Exception):
    pass

numeros_romanos = {
    'I': 1,
    'V': 5, 
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

"""
A_romanos(int)

lista_traducciones = []
- Para cada posicion, cifra de int, de atras a delante
    - valor = descomponer(posicion, cifra)
    - valor_traducio = traducir(valor)
    - añadir valor_traducio a lista_traducciones

- lista_traducciones_ordenada = darle la vuelta a lista_traducciones
- concatenar lista_traducciones
"""
def descomponer(posicion: int, cifra: str) -> int:
    """
    - pasar cifra a entero
    - devolver cifra * 10 ** posicion
    """
    return int(cifra) * 10 ** posicion

def traducir(valor: int) -> str:
    simbolos = {
        0: '', 1: 'I', 2:'II', 3:'III', 4: 'IV', 5: 'V', 6:'VI', 7: 'VII', 8: 'VIII', 9:'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100: 'C', 200: 'CC', 300: 'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
        1000:'M', 2000:'MM', 3000:'MMM'
    }
    return simbolos[valor]

def a_romanos(numero: int)-> str:
    numero_str = str(numero)
    
    # Aseguramos que sea múltiplo de 3
    resto = len(numero_str) % 3
    if resto != 0:
        numero_str = '0' * (3 - resto) + numero_str    

    tripletas = []
    i = 0
    
    while i < len(numero_str):
        # Obtenemos la tripleta actual
        start = max(0, len(numero_str) - (i + 3))
        end = len(numero_str) - i
        tripleta_actual = numero_str[start:end]
        
        # Evaluamos el siguiente valor si existe
        siguiente_indice = start - 1
        if siguiente_indice >= 0 and int(numero_str[siguiente_indice]) < 4:
            # Añadimos el siguiente valor a la tripleta actual
            tripleta_actual = numero_str[siguiente_indice] + tripleta_actual
            i += 1  # Saltamos este dígito adicional
        
        romano = a_romano(tripleta_actual)
        if romano == '':
            break
        tripletas.append(romano +"*" * (len(tripletas)))
        
        # Avanzamos al siguiente bloque
        i += 3

    return ''.join(reversed(tripletas))



def a_romano(numero: int) -> str:
    lista_traducciones = []

    numero_str = str(numero)
    reves = numero_str[::-1]
    for posicion, cifra in enumerate(reves):
        valor = descomponer(posicion, cifra)
        # valor = lambda p, c: int(c) * 10 ** p
        valor_traducio = traducir(valor)
        lista_traducciones.append(valor_traducio)
    
    lista_traducciones_inversa = lista_traducciones[::-1]
    num_romano = ""
    for simbolo in lista_traducciones_inversa:
        num_romano += simbolo
    return num_romano

def puede_restar(lista_restas: list, resta: int) -> bool:
    try:
        ultima_resta = str(lista_restas[-1])
    except IndexError:
        return True
    
    resta_actual = str(resta)
    result = True
    if len(ultima_resta) <= len(resta_actual):
        result = False
    return result
    

def puede_sumar(valor: int, last: int) -> bool:
    return len(str(valor)) < len(str(last))

def to_components(roman: str) -> list:
    order = 0
    number = ""
    numbers = []
    for car in roman:
        if car != "*":
            if order > 0:
                numbers.append((number, order))
                order = 0
                number = ""
            number += car
        else:
            order += 1
    numbers.append((number, order))
    return numbers



def a_arabigos(roman: str) -> int:
    result = 0
    components = to_components(roman)
    for romano, orden in components:
        result += (a_arabigo(romano) * (1000 ** orden))
    return result    

def a_arabigo(num_roman: str) -> int:
    valida, char, limit = valida_repeticiones(num_roman)
    if not valida:
        raise RomanNumberError(f"{char} {'solo' if limit == 4 else 'no'} puede repetirse{' tres veces' if limit == 4 else ''}")


    """
    Recibe un numero romano y tiene que convertirlo a numero entero.
    """
    result = 0
    p_value = 1001
    substract = lambda x: x - (2 * p_value)
    restas_validas = ((1, 5), (1, 10), (10, 50), (10, 100), (100, 500), (100, 1000))
    restas_realizadas = []
    ha_restado = False
    ultima_resta = 0


    for char in num_roman:
        # El simbolo char existe en romano
        value = numeros_romanos.get(char, 0)
        if value == 0:
            raise RomanNumberError(f"{char} no es un simbolo romano")
        
        if ha_restado and value > p_value:
            # Resta contrapeado
            raise RomanNumberError("Restas anidadas")
        elif ha_restado:
            # suma inmediatamente posterior a una resta
            if puede_sumar(value, ultima_resta):
                result += value
                ha_restado = False
            else:
                raise RomanNumberError("Suma despues de resta no permitida")
        elif value > p_value: 
            # Resta normal
            if (p_value, value) in restas_validas:
                ultima_resta = value - p_value
                # if not puede_restar(restas_realizadas, ultima_resta):
                #    raise RomanNumberError("No se permiten restas duplicadas")
                # restas_realizadas.append(ultima_resta)
                result += substract(value)
                ha_restado = True
            else:
                raise RomanNumberError(f"{p_value}, {value} resta no permitida")
        else:
            # Suma normal 
            result += value
        p_value = value

    return result

def esta_en_racha(haystack, neddle:str, racha:int)->bool:
    cont = 0
    if len(haystack) >= racha:
        for el in haystack:
            if el == neddle:
                cont += 1
                if cont == racha:
                    break
            else:
                cont = 0
    else:
        cont = 0
    return cont == racha

def valida_repeticiones(num_roman: str) -> bool:
    """
    return not (esta_en_racha(num_roman, "I", 4) or \
                esta_en_racha(num_roman, "X", 4) or \
                esta_en_racha(num_roman, "C", 4) or \
                esta_en_racha(num_roman, "M", 4))
    """
    no_repeat = [("I", 4), ("X", 4), ("C", 4), ("M", 4),
                 ("V", 2), ("L", 2), ("D", 2)]
    result = True

    for char, limit in no_repeat:
        if esta_en_racha(num_roman, char, limit):
            result = False
            break
    return result, char, limit