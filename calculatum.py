from fromanosV2 import a_arabigo, a_romanos, RomanNumberError

def convertir_a_entero(numero):
    try:
        if numero.isdigit():
            return int(numero)
        else:
            return a_arabigo(numero)
    except RomanNumberError:
        raise ValueError("Entrada incorrecta")

def calcular_resultado(num1, num2, opcion):
    try:
        valor1 = convertir_a_entero(num1)
        valor2 = convertir_a_entero(num2)

        if opcion == "1":
            resultado = valor1 + valor2
            operador = "+"
        elif opcion == "2":
            resultado = valor1 - valor2
            operador = "-"
        elif opcion == "3":
            resultado = valor1 * valor2
            operador = "x"
        elif opcion == "4":
            if valor2 == 0:
                return "División por cero no permitida"
            resultado = valor1 // valor2
            operador = "÷"
        else:
            return "Opción incorrecta"

        if resultado <= 0 or resultado > 3999:
            return "Resultado inválido"
        
        resultado_romano = a_romanos(resultado)
        return f"{num1} {operador} {num2} = {resultado_romano}"
    
    except ValueError as error:
        return str(error)

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

menu()
