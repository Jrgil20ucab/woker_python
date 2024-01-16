def mostrar_menu():
    print("1. Nombre del archivo")
    print("2. Procesar datos del archivo")
    print("3. Resultados del archivo")
    print("4. Exportar resultados")
    print("0. Salir")

def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    return opcion

def procesar_opcion(opcion):
    if opcion == "1":
        nombre_archivo()
    elif opcion == "2":
        procesar_datos()
    elif opcion == "3":
        mostrar_resultados()
    elif opcion == "4":
        exportar_resultados()
    elif opcion == "0":
        salir()
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

def nombre_archivo():
    # Lógica para obtener el nombre del archivo
    print("Opción 1 seleccionada: Nombre del archivo")
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def procesar_datos():
    # Lógica para procesar los datos del archivo
    print("Opción 2 seleccionada: Procesar datos del archivo")
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def mostrar_resultados():
    # Lógica para mostrar los resultados del archivo
    print("Opción 3 seleccionada: Resultados del archivo")
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def exportar_resultados():
    # Lógica para exportar los resultados
    print("Opción 4 seleccionada: Exportar resultados")
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def salir():
    print("Saliendo del programa...")
    # Lógica para salir del programa

# Programa principal
while True:
    mostrar_menu()
    opcion = obtener_opcion()
    procesar_opcion(opcion)
    if opcion == "0":
        break
