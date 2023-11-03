import random

numero = random.randint(0, 10)

oportunidades = 3

while oportunidades > 0:
    adivinanza = int(input("Adivina el número (entre 0 y 10): "))

    if adivinanza == numero:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        print("Lo siento, esa no es la respuesta correcta.")

    oportunidades -= 1

if oportunidades == 0:
    print("Lo siento, no adivinaste el número. El número correcto era", numero)
    
input("Presiona enter para salir...")

# para poder ejecutar el .exe se debe colocar pyinstaller nombre del archivo a ejecutar(main.py) --onefile y de alli ir a la carpeta dist quedara el
# punto exe(main.exe)
