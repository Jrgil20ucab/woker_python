import csv
import os # importar libreria os para limpar la pantalla
from datetime import datetime
from collections import defaultdict

# Leer el archivo de productos
def cargar_productos(ruta_archivo):
    productos = {}
    with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nombre, codigo, descripcion, precio = row
            productos[codigo] = {
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': float(precio)
            }
    return productos

# Leer el archivo de ventas
def cargar_ventas(ruta_archivo):
    ventas = {}
    fechas = []
    with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fecha = row['fecha']
            fechas.append(fecha)
            for codigo, cantidad in row.items():
                if codigo != 'fecha':
                    if codigo not in ventas:
                        ventas[codigo] = {}
                    ventas[codigo][fecha] = int(cantidad)
    return ventas, fechas

# Procesar las ventas trimestrales y calcular totales
def calcular_ventas_trimestrales(ventas, productos):
    trimestre_ventas = defaultdict(float)
    for codigo, ventas_producto in ventas.items():
        for fecha, cantidad in ventas_producto.items():
            trimestre = (datetime.strptime(fecha, '%d/%m/%y').month - 1) // 3 + 1
            trimestre_ventas[trimestre] += cantidad * productos[codigo]['precio']
    return trimestre_ventas

# Generar informe
def calcular_ventas_totales(trimestre_ventas, ventas):
    total_ventas_empresa = sum(trimestre_ventas.values())
    producto_mas_vendido = max(ventas, key=lambda x: sum(ventas[x].values()))
    producto_menos_vendido = min(ventas, key=lambda x: sum(ventas[x].values()))

    print(f"Ventas totales de la compañía: ${total_ventas_empresa:.2f}\n")
    return total_ventas_empresa, producto_mas_vendido, producto_menos_vendido

# Ventas totales de cada producto
def calcular_ventas_totales_por_producto(ventas, productos):
    for codigo, info_producto in productos.items():
        ventas_producto = sum(ventas[codigo].values()) * info_producto['precio']
        print(f"Ventas totales de {info_producto['nombre']}: ${ventas_producto:.2f}")

# Ventas totales diarias
def calcular_ventas_totales_diarias(ventas, productos, fechas):
    ventas_diarias_totales = defaultdict(float)
    for fecha in fechas:
        for codigo, cantidad in ventas.items():
            ventas_diarias_totales[fecha] += cantidad[fecha] * productos[codigo]['precio']
    print("\nVentas totales diarias:")
    for fecha, total_diario in ventas_diarias_totales.items():
        print(f"{fecha}: ${total_diario:.2f}")
    return ventas_diarias_totales

# Ventas mensuales totales
def calcular_ventas_mensuales_totales(ventas_diarias_totales, fechas):
    ventas_mensuales_totales = defaultdict(float)
    for fecha in fechas:
        mes = datetime.strptime(fecha, '%d/%m/%y').strftime('%B')
        ventas_mensuales_totales[mes] += ventas_diarias_totales[fecha]
    print("\nVentas mensuales totales:")
    for mes, total_mensual in ventas_mensuales_totales.items():
        print(f"{mes}: ${total_mensual:.2f}")
    return ventas_mensuales_totales

# Ventas mensuales por cada producto
def calcular_ventas_mensuales_productos(ventas, productos):
    ventas_mensuales_productos = defaultdict(lambda: defaultdict(float))
    
    for codigo, ventas_producto in ventas.items():
        for fecha, cantidad in ventas_producto.items():
            mes = datetime.strptime(fecha, '%d/%m/%y').strftime('%B')
            ventas_mensuales_productos[mes][codigo] += cantidad * productos[codigo]['precio']
    print("\nVentas mensuales por cada producto:")
    for mes, ventas_mes in ventas_mensuales_productos.items():
        print(f"{mes}:")
        for codigo, total_mes_producto in ventas_mes.items():
            print(f"  {productos.get(codigo, {'nombre': 'Producto Desconocido'})['nombre']}: ${total_mes_producto:.2f}")
    return ventas_mensuales_productos

# Producto más vendido y menos vendido
def generar_informe_ventas(ventas, productos, producto_mas_vendido, producto_menos_vendido):
    cantidad_mas_vendida = sum(ventas[producto_mas_vendido].values())
    cantidad_menos_vendida = sum(ventas[producto_menos_vendido].values())
    total_mas_vendido = cantidad_mas_vendida * productos[producto_mas_vendido]['precio']
    total_menos_vendido = cantidad_menos_vendida * productos[producto_menos_vendido]['precio']

    print(f"\nProducto más vendido: {productos.get(producto_mas_vendido, {'nombre': 'Producto Desconocido'})['nombre']}")
    print(f"  Cantidad vendida: {cantidad_mas_vendida}")
    print(f"  Total vendido: ${total_mas_vendido:.2f}")

    print(f"\nProducto menos vendido: {productos.get(producto_menos_vendido, {'nombre': 'Producto Desconocido'})['nombre']}")
    print(f"  Cantidad vendida: {cantidad_menos_vendida}")
    print(f"  Total vendido: ${total_menos_vendido:.2f}")
    
    return cantidad_mas_vendida, cantidad_menos_vendida, total_mas_vendido, total_menos_vendido

# Histograma de porcentajes de ventas por producto en el trimestre
def generar_histograma_ventas(ventas, productos, total_ventas_empresa):
    porcentajes_ventas = {codigo: (sum(ventas_producto.values()) * productos[codigo]['precio']) / total_ventas_empresa * 100 for codigo, ventas_producto in ventas.items()}

    print("\nHistograma de porcentajes de ventas por producto en el trimestre:")
    for codigo, porcentaje in porcentajes_ventas.items():
        if codigo in productos:
            nombre_producto = productos[codigo]['nombre']
            print(f"{nombre_producto} ({porcentaje:.2f}%): {'*' * int(porcentaje)}")
    
    return porcentajes_ventas

# Generar informe y escribir en el archivo resultados.txt
    
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
    archivos_precios = input("Ingrese nombre del archivo de precios:")
    archivos_ventas = input("Ingrese el nombre del archivo de ventas:")
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def procesar_datos():
    global ventas, productos, fechas
    # Lógica para procesar los datos del archivo
    print("Opción 2 seleccionada: Procesar datos del archivo")
    productos = cargar_productos(archivos_precios)
    ventas, fechas = cargar_ventas(archivos_ventas)
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def mostrar_resultados():
    # Lógica para mostrar los resultados del archivo
    global total_ventas_empresa, ventas_diarias_totales, ventas_mensuales_totales, ventas_mensuales_productos, producto_mas_vendido, cantidad_mas_vendida, total_mas_vendido, producto_menos_vendido, cantidad_menos_vendida, total_menos_vendido, porcentajes_ventas
    print("Opción 3 seleccionada: Resultados del archivo")
    ventas_trimestrales = calcular_ventas_trimestrales(ventas, productos)
    calcular_ventas_totales_por_producto(ventas, productos)
    total_ventas_empresa, producto_mas_vendido, producto_menos_vendido = calcular_ventas_totales(ventas_trimestrales, ventas)
    ventas_diarias_totales = calcular_ventas_totales_diarias(ventas, productos, fechas)
    ventas_mensuales_totales = calcular_ventas_mensuales_totales(ventas_diarias_totales, fechas)
    ventas_mensuales_productos = calcular_ventas_mensuales_productos(ventas, productos)
    cantidad_mas_vendida, cantidad_menos_vendida, total_mas_vendido, total_menos_vendido = generar_informe_ventas(ventas, productos, producto_mas_vendido, producto_menos_vendido)
    porcentajes_ventas =generar_histograma_ventas(ventas, productos, total_ventas_empresa)
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def exportar_resultados():
    # Lógica para exportar los resultados
    print("Opción 4 seleccionada: Exportar resultados")
    with open('resultados.txt', 'w', encoding='utf-8') as resultados_file:
        resultados_file.write(f"Ventas totales de la compañía: ${total_ventas_empresa:.2f}\n\n")

        # Ventas totales de cada producto
        for codigo, info_producto in productos.items():
            ventas_producto = sum(ventas[codigo].values()) * info_producto['precio']
            resultados_file.write(f"Ventas totales de {info_producto['nombre']}: ${ventas_producto:.2f}\n")

        resultados_file.write("\n")

        # Ventas totales diarias
        resultados_file.write("Ventas totales diarias:\n")
        for fecha, total_diario in ventas_diarias_totales.items():
            resultados_file.write(f"{fecha}: ${total_diario:.2f}\n")

        resultados_file.write("\n")

        # Ventas mensuales totales
        resultados_file.write("Ventas mensuales totales:\n")
        for mes, total_mensual in ventas_mensuales_totales.items():
            resultados_file.write(f"{mes}: ${total_mensual:.2f}\n")

        resultados_file.write("\n")

        # Ventas mensuales por cada producto
        resultados_file.write("Ventas mensuales por cada producto:\n")
        for mes, ventas_mes in ventas_mensuales_productos.items():
            resultados_file.write(f"{mes}:\n")
            for codigo, total_mes_producto in ventas_mes.items():
                nombre_producto = productos.get(codigo, {'nombre': 'Producto Desconocido'})['nombre']
                resultados_file.write(f"  {nombre_producto}: ${total_mes_producto:.2f}\n")

        resultados_file.write("\n")

        # Producto más vendido y menos vendido
        resultados_file.write(f"Producto más vendido: {productos.get(producto_mas_vendido, {'nombre': 'Producto Desconocido'})['nombre']}\n")
        resultados_file.write(f"  Cantidad vendida: {cantidad_mas_vendida}\n")
        resultados_file.write(f"  Total vendido: ${total_mas_vendido:.2f}\n\n")

        resultados_file.write(f"Producto menos vendido: {productos.get(producto_menos_vendido, {'nombre': 'Producto Desconocido'})['nombre']}\n")
        resultados_file.write(f"  Cantidad vendida: {cantidad_menos_vendida}\n")
        resultados_file.write(f"  Total vendido: ${total_menos_vendido:.2f}\n\n")

        # Histograma de porcentajes de ventas por producto en el trimestre
        resultados_file.write("Histograma de porcentajes de ventas por producto en el trimestre:\n")
        for codigo, porcentaje in porcentajes_ventas.items():
            if codigo in productos:
                nombre_producto = productos[codigo]['nombre']
                resultados_file.write(f"{nombre_producto} ({porcentaje:.2f}%): {'*' * int(porcentaje)}\n")
           

    # Agregar información del equipo al final del archivo resultados.txt
    with open('resultados.txt', 'a', encoding='utf-8') as resultados_file:
        resultados_file.write("\n--- Integrantes del Equipo ---\n")
        resultados_file.write("Nombre1 - CI: xxxxxxx\n")  # Reemplaza con el nombre y CI del primer integrante
        resultados_file.write("Nombre2 - CI: xxxxxxx\n")  # Reemplaza con el nombre y CI del segundo integrante
        # Agrega más líneas según sea necesario para cada integrante del equipo
        
    eleccion = input("¿Desea salir del programa? (y/n): ")
    if eleccion.lower() == "y":
        salir()

def salir():
    print("Saliendo del programa...")
    # Lógica para salir del programa

# Programa principal
archivos_precios="productos_ferreteria_precios.csv"
archivos_ventas="productos_ferreteria_ventas.csv"
while True:   
    archivos_salida="resultados_file"
    os.system("cls")
    mostrar_menu()
    opcion = obtener_opcion()
    procesar_opcion(opcion)
    if opcion == "0":
        break
