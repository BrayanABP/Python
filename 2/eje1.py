sumatoria = 0
numeros_pares = 0
numeros_impares = 0
sw=False
while True:
    numero = float(input("Ingrese un número (negativo para salir): "))
    if numero < 0:
        break

    sumatoria += numero  #sumatoria = sumatoria + numero
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

    if sw:
        if numero < numero_menor:
            numero_menor = numero
        if numero > numero_mayor:
            numero_mayor = numero
    else:
        numero_menor = numero
        numero_mayor = numero
        sw = True

print(f"Sumatoria de los números: {sumatoria}")
print(f"Cantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")
if sw:
    print(f"Número menor: {numero_menor}")
    print(f"Número mayor: {numero_mayor}")
else:
    print(f"Número menor: {0}")
    print(f"Número mayor: {0}")