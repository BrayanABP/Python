def separar_pares_impares(numeros):
    pares = [numero for numero in numeros if numero % 2 == 0]
    impares = [numero for numero in numeros if numero % 2 != 0]
    return sorted(pares), sorted(impares)

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = separar_pares_impares(numeros)
print("Pares: ", pares)
print("Impares: ", impares)
