from calculatum.roman_functions import a_romanos, a_arabigos, RomanNumberError
from typing import Union

class Roman_Number:
    def __init__(self, numero:Union[int | str]):
        if type(numero) == int:
            self.valor = numero
            self.representacion = a_romanos(numero)
        elif type(numero) == str:
            self.valor = a_arabigos(numero)             
            self.representacion = numero
        else:
            raise RomanNumberError("solo admitimos int o str")    

    def __str__(self):
        return self.representacion
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other: object):
        if not isinstance(other, (int, self.__class__)):
            raise TypeError(f"'+' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        return Roman_Number(self.valor + (other if isinstance(other, int) else other.valor))
    
    # hacer un reverse de los operandos
    def __radd__(self, other: object):
        #return self.__add__(other)
        return self + other

    def __sub__(self, other: object):
        if not isinstance(other, (int, self.__class__)):
            raise TypeError(f"'-' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        result = self.valor - (other if isinstance(other, int) else other.valor)
        if result < 0 or result > 3999:
            raise TypeError("El resultado de la resta no puede ser < 0 o > 3999")          
        
        return Roman_Number(result)
    
    def __rsub__(self, other: object):
        if isinstance(other, int):
            number_value = other
        else:
            raise TypeError(f"'-' no permitida entre {Roman_Number.__name__} y {other.__class__.__name__}")
                      
        return Roman_Number(number_value) - self
    
    def __mul__(self, other: object):
        if not isinstance(other, (int, self.__class__)):
            raise TypeError(f"'*' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        result = self.valor * (other if isinstance(other, int) else other.valor)
        if result < 0 or result > 3999:
            raise TypeError("El resultado de la multiplicacion no puede ser < 0 o > 3999")          
        
        return Roman_Number(result)
    
    def __rmul__(self, other: object):
        return self * other
    
    def __floordiv__(self, other: object):
        if not isinstance(other, (int, self.__class__)):
            raise TypeError(f"'/' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        otro_valor = (other if isinstance(other, int) else other.valor)
        if otro_valor == 0:
            raise TypeError("El valor no puede ser 0")          
        result = self.valor // otro_valor        
        if result <= 0 or result > 3999:
            raise TypeError("El resultado de la division no puede ser < 0 o > 3999")          
        
        return Roman_Number(result)
    
    def __rfloordiv__(self, other: object):
        if isinstance(other, int):
            number_value = other
        else:
            raise TypeError(f"'-' no permitida entre {Roman_Number.__name__} y {other.__class__.__name__}")
                      
        return Roman_Number(number_value) // self
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor == other.valor
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor < other.valor
    def __le__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor <= other.valor
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor > other.valor
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor >= other.valor
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor != other.valor

    def __hash__(self):
        return hash([self.valor])