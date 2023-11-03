def contar_letras(palabra):
    diccionario = {}
    for letra in palabra:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

# Ejemplo de uso:
palabra = "manzana"
print("El conteo de letras en la palabra '", palabra, "' es: ", contar_letras(palabra))
