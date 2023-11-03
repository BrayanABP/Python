def numero_a_cadena(n):
    diccionario_numeros = {
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve',
        '0': 'cero'
    }
    return " - ".join(diccionario_numeros[i] for i in str(n))

# Ejemplo de uso:
print(numero_a_cadena(134))
