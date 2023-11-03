mi_lista = [1, 2, 3]
try:
    agregar_una_vez(mi_lista, 2)
except ValueError:
    print("El elemento ya se encuentra en la lista")
