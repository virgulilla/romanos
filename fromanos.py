numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def a_romanos(valor: int) -> str:
    for romano, decimal in numeros_romanos.items():
        if decimal == valor:
            return romano

assert a_romanos(1) == 'I', "numero incorrecto"
assert a_romanos(500) == 'D', "numero incorrecto"

assert a_romanos(2) == 'II'
assert a_romanos(200) == 'CC'