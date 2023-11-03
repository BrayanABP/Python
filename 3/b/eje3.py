def traductor_frutas():
    diccionario_frutas = {
        'manzana': 'apple',
        'banana': 'banana',
        'cereza': 'cherry',
        'naranja': 'orange',
        'pera': 'pear',
        # Puede agregar más frutas aquí
    }

    while True:
        fruta = input("Ingrese el nombre de una fruta en español (o 'salir' para terminar): ")
        if fruta.lower() == 'salir':
            break

        if fruta in diccionario_frutas:
            print("La traducción al inglés de", fruta, "es", diccionario_frutas[fruta])
        else:
            print("La fruta", fruta, "no se encuentra en el diccionario.")
            agregar = input("¿Desea agregarla al diccionario? (s/n): ")
            if agregar.lower() == 's':
                traduccion = input("Ingrese la traducción al inglés de la fruta: ")
                diccionario_frutas[fruta] = traduccion
                print("La fruta", fruta, "ha sido agregada al diccionario con la traducción", traduccion)

traductor_frutas()
