lista = [1, 2, 3, 4, 5]

while True:
    try:
        posicion = int(input("Ingrese una posición de la lista: "))
        print("El valor en la posición", posicion, "es", lista[posicion])
        break
    except IndexError:
        print("La posición ingresada no existe en la lista. Por favor, intente de nuevo.")
    except ValueError:
        print("Debe ingresar un número entero como posición. Por favor, intente de nuevo.")
