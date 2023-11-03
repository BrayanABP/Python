def mostrar_pares(n, i=1):
    if i > n:
        return
    if i % 2 == 0:
        print(i)
    mostrar_pares(n, i + 1)

# Ejemplo de uso:
mostrar_pares(10)
