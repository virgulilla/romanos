from calculatum.entities import RomanNumberError, Roman_Number

def tratar_valor_entrado(numero: str):
    if numero.isdigit():
        return int(numero)
    else:
        return numero

def calcular_resultado(num1: str, num2: str, opcion: str):
    try:
        num1 = tratar_valor_entrado(num1)
        num1 = Roman_Number(num1)
        num2 = tratar_valor_entrado(num2)
        num2 = Roman_Number(num2)

        if opcion == "1":
            resultado = num1 + num2
            operador = "+"
        elif opcion == "2":
            resultado = num1 - num2
            operador = "-"
        elif opcion == "3":
            resultado = num1 * num2
            operador = "x"
        elif opcion == "4":            
            resultado = num1 // num2
            operador = "/"
        else:
            return "Opción incorrecta"
    
        return f"{num1.valor} {operador} {num2.valor} = {resultado.representacion}"
    
    except TypeError as error:
        return str(error)
    except RomanNumberError as rnerror:
        return str(rnerror)

def menu():
    while True:
        print("\nCALCULATUM")
        print("*" * 10)
        print("1: Sumar")
        print("2: Restar")
        print("3: Multiplicar")
        print("4: Dividir")

        opcion = input("Elige operación (1 a 4): ")

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción incorrecta")
            continue

        num1 = input("Primer número (romano o entero): ")
        num2 = input("Segundo número (romano o entero): ")

        resultado = calcular_resultado(num1, num2, opcion)
        print(f"Resultado: {resultado}")

        continuar = input("Otra S/N [S]: ")
        if continuar == "N":
            print("Saliendo de la aplicación.")
            break