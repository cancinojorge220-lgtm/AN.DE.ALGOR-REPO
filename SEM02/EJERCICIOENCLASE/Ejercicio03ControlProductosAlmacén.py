#03.Control de Productos en un Almacén

productos = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

try:
    buscar = int(input("\nIngrese el código del producto a buscar: "))
    inicio = int(input("\nIngresa la posición de Incio de la Busqueda : "))
    fin = int(input("\nIngresa la posición de Fin de la Busqueda : "))
except ValueError:
    print("\nError: Por favor, ingresa un número entero válido.")
    exit()

encontrado = False

for i in range(inicio, fin + 1):
    if productos[i] == buscar:
        print(f"\nProducto encontrado en la posición: {i}")
        encontrado = True
        break

if encontrado == False:
    print("\nProducto no encontrado en el rango especificado.")

