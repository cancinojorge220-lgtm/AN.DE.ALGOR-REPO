#Diccionario con 15 pedidos de ejemplo
pedidos = [
    {"codigo": "P001", "cliente": "Juan Perez", "ciudad": "Lima", "peso": 4.5, "prioridad": "Alta", "costo": 25.0},
    {"codigo": "P002", "cliente": "Maria Rogers", "ciudad": "Trujillo", "peso": 12.0, "prioridad": "Media", "costo": 50.0},
    {"codigo": "P003", "cliente": "Carlos Mendoza", "ciudad": "Arequipa", "peso": 1.2, "prioridad": "Baja", "costo": 15.0},
    {"codigo": "P004", "cliente": "Ana Delgado", "ciudad": "Chiclayo", "peso": 8.5, "prioridad": "Alta", "costo": 40.0},
    {"codigo": "P005", "cliente": "Luis Rodriguez", "ciudad": "Lima", "peso": 3.0, "prioridad": "Baja", "costo": 20.0},
    {"codigo": "P006", "cliente": "Diana Flores", "ciudad": "Cusco", "peso": 15.5, "prioridad": "Alta", "costo": 75.0},
    {"codigo": "P007", "cliente": "Jorge Cancino", "ciudad": "Trujillo", "peso": 2.5, "prioridad": "Media", "costo": 18.0},
    {"codigo": "P008", "cliente": "Elena Beltran", "ciudad": "Piura", "peso": 6.0, "prioridad": "Baja", "costo": 30.0},
    {"codigo": "P009", "cliente": "Roberto Carlos", "ciudad": "Lima", "peso": 10.0, "prioridad": "Alta", "costo": 55.0},
    {"codigo": "P010", "cliente": "Sofia Castro", "ciudad": "Ica", "peso": 0.8, "prioridad": "Media", "costo": 12.0},
    {"codigo": "P011", "cliente": "Ricardo Gareca", "ciudad": "Tacna", "peso": 14.0, "prioridad": "Alta", "costo": 65.0},
    {"codigo": "P012", "cliente": "Lucia Mendez", "ciudad": "Chimbote", "peso": 5.2, "prioridad": "Baja", "costo": 22.0},
    {"codigo": "P013", "cliente": "Pedro Suarez", "ciudad": "Huancayo", "peso": 9.3, "prioridad": "Media", "costo": 42.0},
    {"codigo": "P014", "cliente": "Patricia Luna", "ciudad": "Lima", "peso": 11.1, "prioridad": "Alta", "costo": 48.0},
    {"codigo": "P015", "cliente": "Miguel Grau", "ciudad": "Piura", "peso": 7.4, "prioridad": "Media", "costo": 33.0}
]

# Función para buscar pedidos por cliente
def buscar_pedidos_por_cliente(lista_pedidos):
    # Solicitar al usuario que ingrese una cadena de búsqueda para el nombre del cliente
    cadena_busqueda = input("Ingrese el nombre (o parte del nombre) del cliente a buscar: ").strip().lower()    
    resultados = []
    
    # Recorrer la lista de pedidos y verificar si el nombre del cliente contiene la cadena de búsqueda
    for pedido in lista_pedidos:

        if cadena_busqueda in pedido["cliente"].lower():
            resultados.append(pedido)
            
    # Mostrar los resultados de la búsqueda
    if resultados:
        print(f"\nSe encontraron {len(resultados)} pedido(s) :")
        for p in resultados:
            print(f"Código: {p['codigo']} | Cliente: {p['cliente']} | Ciudad: {p['ciudad']} | Peso: {p['peso']}kg | Prioridad: {p['prioridad']} | Costo: S/.{p['costo']}")
    else:
        print(f"\nNo se encontraron que coincidan con: '{cadena_busqueda}'")

# Llamar a la función para buscar pedidos por cliente
buscar_pedidos_por_cliente(pedidos)