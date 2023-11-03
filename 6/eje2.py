import random

palabras = []
equivocaciones_permitidas = 0

def agregar_palabra():
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)

def configurar():
    global equivocaciones_permitidas
    equivocaciones_permitidas = int(input("Ingresa el número de equivocaciones permitidas: "))

def jugar():
    palabra = random.choice(palabras)
    adivinadas = ['_' for _ in palabra]
    equivocaciones = 0

    while equivocaciones < equivocaciones_permitidas and '_' in adivinadas:
        print(' '.join(adivinadas))
        letra = input("Ingresa una letra: ")

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    adivinadas[i] = letra
        else:
            equivocaciones += 1
            print(f"Error! Te quedan {equivocaciones_permitidas - equivocaciones} oportunidades")

    if '_' in adivinadas:
        print(f"Perdiste! La palabra era {palabra}")
    else:
        print(f"Ganaste! La palabra era {palabra}")

def menu():
    while True:
        print("1. Agregar Palabra")
        print("2. Configurar")
        print("3. Jugar")
        print("4. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            agregar_palabra()
        elif opcion == 2:
            configurar()
        elif opcion == 3:
            jugar()
        elif opcion == 4:
            break

menu()
