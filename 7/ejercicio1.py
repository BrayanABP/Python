def sumar(*args):
    try:
        return sum(args)
    except TypeError:
        return "Error: Ingresa números válidos."

def restar(num1, num2):
    try:
        return num1 - num2
    except TypeError:
        return "Error: Ingresa números válidos."

def multiplicar(*args):
    try:
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    except TypeError:
        return "Error: Ingresa números válidos."

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Ingresa números válidos."

def operacion(num1, oper, num2):
    try:
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        elif oper == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: No se puede dividir entre cero."
        else:
            return "Error: Operador no válido."
    except TypeError:
        return "Error: Ingresa números válidos."

def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Operación")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción (1/2/3/4/5/6): ")

        if opcion == "1":
            numeros = input("Ingresa los números separados por espacio: ").split()
            resultado = sumar(*map(float, numeros))
            print("Resultado:", resultado)
        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = restar(num1, num2)
            print("Resultado:", resultado)
        elif opcion == "3":
            numeros = input("Ingresa los números separados por espacio: ").split()
            resultado = multiplicar(*map(float, numeros))
            print("Resultado:", resultado)
        elif opcion == "4":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
            print("Resultado:", resultado)
        elif opcion == "5":
            num1 = float(input("Ingresa el primer número: "))
            oper = input("Ingresa el operador (+, -, *, /): ")
            num2 = float(input("Ingresa el segundo número: "))
            resultado = operacion(num1, oper, num2)
            print("Resultado:", resultado)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
