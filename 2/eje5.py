clave = "123"
intentos = 0
while intentos < 5:
    clave_ingresada = input("Digite la clave: ")
    if clave == clave_ingresada:
        print("Bienvenido al Sistema")
        break
    else:
        print("Clave Incorrecta")
        intentos += 1
        print(f"Intento {intentos} de 5")
