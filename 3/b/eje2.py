def inscripcion_estudiantes():
    estudiantes_futbol = set()
    estudiantes_baloncesto = set()

    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        deporte = input("Ingrese el deporte al que se inscribe el estudiante (f para futbol, b para baloncesto, fb para ambos): ")
        if 'f' in deporte:
            estudiantes_futbol.add(nombre)
        if 'b' in deporte:
            estudiantes_baloncesto.add(nombre)

    print("Estudiantes inscritos en futbol: ", estudiantes_futbol)
    print("Estudiantes inscritos en baloncesto: ", estudiantes_baloncesto)
    print("Estudiantes inscritos en ambos deportes: ", estudiantes_futbol & estudiantes_baloncesto)
    print("Todos los estudiantes inscritos en algún deporte: ", estudiantes_futbol | estudiantes_baloncesto)
    print("Estudiantes inscritos en solo un deporte: ", (estudiantes_futbol | estudiantes_baloncesto) - (estudiantes_futbol & estudiantes_baloncesto))

inscripcion_estudiantes()
