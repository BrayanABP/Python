import random

def obtener_opcion_usuario():
    return input("Elige una opción (piedra, papel, tijera): ")

def obtener_opcion_computadora():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "tijera" and computadora == "papel") or \
       (usuario == "papel" and computadora == "piedra"):
        return "Usuario gana"
    else:
        return "Computadora gana"

def jugar():
    while True:
        usuario = obtener_opcion_usuario()
        computadora = obtener_opcion_computadora()
        print(f"Usuario eligió {usuario}, Computadora eligió {computadora}")
        resultado = determinar_ganador(usuario, computadora)
        print(resultado)
        if resultado != "Empate":
            break

jugar()
