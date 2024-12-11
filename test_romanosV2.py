from fromanosV2 import a_romanos, descomponer, traducir, a_decimal

def _test_simbolos_sencillos():
    assert a_romanos(1) == 'I'
    assert a_romanos(500) == 'D'

def _test_doble_repeticion():
    assert a_romanos(2) == 'II'    
    assert a_romanos(200) == 'CC'

def test_descomponer():
    resultado = descomponer(0,'9')
    assert resultado == 9
    resultado = descomponer(1,'3')
    assert resultado == 30
    resultado = descomponer(2,'9')
    assert resultado == 900        
    resultado = descomponer(3,'1')
    assert resultado == 1000

def test_traducir_a_romano():
    assert traducir(9, False) == 'IX'
    assert traducir(30, False) == 'XXX'
    assert traducir(900, False) == 'CM'
    assert traducir(1000, False) == 'M'
    assert traducir(2, False) == 'II'

    assert traducir(800, False) == 'DCCC'

def test_pasar_a_romano():
    assert a_romanos(1939) == 'MCMXXXIX'

def test_pasar_a_decimal():
    assert a_decimal('MMMCMXCIX') == 3999        
    assert a_decimal('MMCDXXIV') == 2424

