# Diccionario de valores romanos
valores_romanos = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}

def validar_romano(romano):
    if not romano:
        return False
    
    repetibles = {'I', 'X', 'C', 'M'}
    no_repetibles = {'V', 'L', 'D'}
    contador = {}
    anterior = ''
    valor_anterior = 0
    restas_realizadas = set()

    for i, simbolo in enumerate(romano):
        if simbolo not in valores_romanos.values():
            return False
        
        valor_actual = valores_romanos[simbolo]

        if simbolo in contador:
            contador[simbolo] += 1
        else:
            contador[simbolo] = 1

        if simbolo in no_repetibles and contador[simbolo] > 1:
            return False

        if simbolo in repetibles and contador[simbolo] > 3:
            return False
        
        if i > 0 and valor_actual > valor_anterior:
            if (anterior, simbolo) not in [('I', 'V'), ('I', 'X'), 
                                           ('X', 'L'), ('X', 'C'), 
                                           ('C', 'D'), ('C', 'M')]:
                return False

            if anterior in restas_realizadas:
                return False

            restas_realizadas.add(anterior)

            if contador[anterior] > 1:
                return False

        anterior = simbolo
        valor_anterior = valor_actual

    return True

def a_romanos(numero):
    if not (1 <= numero <= 3999):
        return "Número fuera de rango (1-3999)"

    resultado = ""
    for valor, simbolo in valores_romanos.items():
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

def a_entero(romano):
    if not validar_romano(romano):
        return "Número romano inválido"

    total = 0
    valor_anterior = 0

    for simbolo in reversed(romano):
        valor_actual = valores_romanos[simbolo]
        if valor_actual < valor_anterior:
            total -= valor_actual
        else:
            total += valor_actual
        valor_anterior = valor_actual

    return total