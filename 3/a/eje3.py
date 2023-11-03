lista = []

salir = 1

numeros_repetidos = 0

while salir != 5:

  print("Aplicaciones Con Listas\n")

  print("1. Ingresar Lista Nueva")

  print("2. Ordenar Lista")

  print("3. Promedio Lista")

  print("4. Buscar Elemento")

  print("5. Salir")

  opcion = int(input("Escoja Una Opción: "))

  if opcion < 1 or opcion > 5:

    print("Debe Ingresar Un Número Entero Entre 1 y 5")

  elif opcion == 1:

    m = 1

    while m==1:

      lista.append(int((input("ingrese un elemento númerico: "))))

      x = len(lista)

      indice = x - 1

      if lista[indice] < 0:

          del(lista[indice])

          m = 2

    print("La Lista Ingresada Es: ", lista, "\n")

  elif opcion == 2:

    lista.sort()  

    print("La Lista Ordena Queda: ",lista, "\n")

  elif opcion == 3:

    print("El Promedio De Los Valores De La Lista Es: ", sum(lista)/len(lista), "\n")

  elif opcion == 4:

    buscar = int(input("Ingrese Un Número Que Quiera Buscar En La Lista: "))
    cantidad_veces = lista.count(buscar)
    if cantidad_veces > 0:
      print ("si está y está ", cantidad_veces)

    else:

      print("El Número No Está En La Lista\n")

  elif opcion == 5:

    salir = 5
