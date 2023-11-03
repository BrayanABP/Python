def almacenar_informacion_estudiantes():
    estudiantes = {}

    for i in range(5):
        id = input("Ingrese el id del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")
        nota = input("Ingrese la nota del estudiante: ")
        estudiantes[id] = {'nombre': nombre, 'edad': edad, 'nota': nota}

    print("\n(a) Información de todos los estudiantes:")
    for id, info in estudiantes.items():
        print("ID:", id)
        print("Nombre:", info['nombre'])
        print("Edad:", info['edad'])
        print("Nota:", info['nota'], "\n")

    print("(b) Información de un estudiante específico:")
    id_buscar = input("Ingrese el id del estudiante a buscar: ")
    if id_buscar in estudiantes:
        print("ID:", id_buscar)
        print("Nombre:", estudiantes[id_buscar]['nombre'])
        print("Edad:", estudiantes[id_buscar]['edad'])
        print("Nota:", estudiantes[id_buscar]['nota'], "\n")
    else:
        print("No se encontró un estudiante con el id", id_buscar)

almacenar_informacion_estudiantes()
