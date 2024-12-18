from fromanosV2 import a_romanos, descomponer, traducir, a_arabigo, RomanNumberError, valida_repeticiones, Roman_Number
import pytest

def test_simbolos_sencillos():
    assert a_romanos(1) == 'I', "numero incorrecto"
    assert a_romanos(500) == 'D', "numero incorrecto"

def test_doble_repeticion():
    assert a_romanos(2) == 'II'
    assert a_romanos(200) == 'CC'

def test_descomponer():
    # voy a probar el numero 1939, cadena '9391'
    resultado = descomponer(0, '9')
    assert resultado == 9
    resultado = descomponer(1,'3')
    assert resultado == 30
    resultado = descomponer(2, '9')
    assert resultado == 900
    resultado = descomponer(3,'1')
    assert resultado == 1000

def test_traducir():
    assert traducir(9) == "IX"
    assert traducir(30) == "XXX"
    assert traducir(900) == "CM"
    assert traducir(1000) == "M"
    assert traducir(2) == "II"

    assert traducir(800) == "DCCC"

def test_romanos_varios():
    assert a_romanos(1939) == "MCMXXXIX"

def test_a_decimal_entradas_correctas():
    assert a_arabigo("MCMXXXIX") == 1939

    for n in range(1, 4000):
        assert a_arabigo(a_romanos(n)) == n

def test_validar_caracteres_romanos():
    with pytest.raises(RomanNumberError) as contexto:
        a_arabigo("ZTW")
    assert str(contexto.value).endswith("no es un simbolo romano")

def test_validar_no_repeticiones_de_mas_de_3():
    """
    I, X, C, M hasta 3 veces

    """
    assert valida_repeticiones("IIIII") == (False, "I", 4)
    assert valida_repeticiones("XXXX")  == (False, "X", 4)
    assert valida_repeticiones("CCCC") == (False, "C", 4)
    assert valida_repeticiones("MMMM") == (False, "M", 4)


def test_validar_romano_cuatro_repeticiones():
    with pytest.raises(RomanNumberError) as contexto:
        a_arabigo("MCCCCXXII")
    assert str(contexto.value) == "C solo puede repetirse tres veces"

    with pytest.raises(RomanNumberError) as contexto:
        a_arabigo("MMMMCXXII")
    assert str(contexto.value) == "M solo puede repetirse tres veces"

def test_validar_no_repeticiones_de_mas_de_3():
    """
    V, L, D no se pueden repetir
    """
    assert valida_repeticiones("VV") == (False, "V", 2)
    assert valida_repeticiones("DD")  == (False, "D", 2)
    assert valida_repeticiones("LL") == (False, "L", 2)


def test_validar_romano_sin_repeticiones():
    with pytest.raises(RomanNumberError) as ctx_error:
        a_arabigo("MCCVV")
    assert str(ctx_error.value) == "V no puede repetirse"


def test_restas_incorrectas():
    with pytest.raises(RomanNumberError):
        a_arabigo("IC")

    with pytest.raises(RomanNumberError):
        a_arabigo("VX")

def test_no_restas_repetidas():
    with pytest.raises(RomanNumberError):
        a_arabigo("XCXC")

def test_no_restas_repetidas_del_mismo_grupo_valor():
    with pytest.raises(RomanNumberError):
        a_arabigo("XCXL")

def test_no_sumar_mismo_grupo_despues_de_resta():
    with pytest.raises(RomanNumberError):
        a_arabigo("XCXXXIII")

def test_no_sumar_mismo_grupo_distinto_valor():
    with pytest.raises(RomanNumberError):
        a_arabigo("XCL")

def test_no_restas_contrapeadas():
    with pytest.raises(RomanNumberError):
        a_arabigo("IXC")

def test_constructor_entero_clase_romana():
    rn = Roman_Number(8)
    assert rn.valor == 8
    assert rn.representacion == "VIII"      

def test_constructor_cadena_clase_Romana():
    rn = Roman_Number("VIII") 
    assert rn.valor == 8
    assert rn.representacion == "VIII"

def test_str_romanos():
    rn = Roman_Number(9)
    assert str(rn) == "IX"

def test_suma_romanos():        
    assert Roman_Number(9) + Roman_Number(10) == Roman_Number(19)
    assert Roman_Number(9) + 10 == Roman_Number(19)

def test_suma_enteros_romanos():
    assert 9 + Roman_Number(10) == Roman_Number(19)

def test_resta_reversa():
    assert 9 - Roman_Number(6) == Roman_Number(3)  

def test_division_reversa():
    assert 9 // Roman_Number(3) == Roman_Number(3)