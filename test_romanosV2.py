from fromanosV2 import a_romanos, descomponer

def test_sencillo():
    assert a_romanos(1) == 'I'
    assert a_romanos(500) == 'D'

def test_descomponer():
    resultado = descomponer(0,'9')
    assert resultado == 9
    resultado = descomponer(1,'3')
    assert resultado == 30
    resultado = descomponer(2,'9')
    assert resultado == 900        
    resultado = descomponer(3,'1')
    assert resultado == 1000        

