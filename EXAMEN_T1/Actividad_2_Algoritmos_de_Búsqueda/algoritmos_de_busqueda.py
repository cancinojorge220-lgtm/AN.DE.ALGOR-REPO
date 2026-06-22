
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

# 1. BÚSQUEDA LINEAL
def busqueda_lineal(pedidos, codigo_buscado):
    # Recorrer la lista de pedidos y verificar si el código coincide con el código buscado
    for i in range(len(pedidos)):
        if pedidos[i]["codigo"] == codigo_buscado:
            return pedidos[i]
    return "Pedido no encontrado"


# 2. BÚSQUEDA LINEAL ACOTADA (Con Centinela)
def busqueda_lineal_acotada(pedidos, codigo_buscado):
    # Crear una copia de la lista de pedidos y agregar un centinela al final
    pedidos_copia = pedidos.copy()
    pedidos_copia.append({"codigo": codigo_buscado}) 
    
    # Recorrer la lista de pedidos hasta encontrar el código buscado o el centinela
    i = 0
    while pedidos_copia[i]["codigo"] != codigo_buscado:
        i += 1
    
    # Si encontramos el código buscado antes del centinela, lo retornamos; de lo contrario, retornamos None
    if i < len(pedidos):
        return pedidos[i]
    return "Pedido no encontrado"


# 3. BÚSQUEDA BINARIA ITERATIVA
def busqueda_binaria_iterativa(pedidos, codigo_buscado):
    izquierda = 0
    derecha = len(pedidos) - 1
    
    # La lista de pedidos debe estar ordenada por código para que la búsqueda binaria funcione correctamente
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if pedidos[medio]["codigo"] == codigo_buscado:
            return pedidos[medio]
        elif pedidos[medio]["codigo"] < codigo_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return "Pedido no encontrado"


# 4. BÚSQUEDA BINARIA RECURSIVA
def busqueda_binaria_recursiva(pedidos, codigo_buscado, izquierda, derecha):
    # La lista de pedidos debe estar ordenada por código para que la búsqueda binaria funcione correctamente
    if izquierda > derecha:
        return "Pedido no encontrado"
        
    medio = (izquierda + derecha) // 2
    
    if pedidos[medio]["codigo"] == codigo_buscado:
        return pedidos[medio]
    elif pedidos[medio]["codigo"] < codigo_buscado:
        return busqueda_binaria_recursiva(pedidos, codigo_buscado, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(pedidos, codigo_buscado, izquierda, medio - 1)

# Probando la Búsqueda Lineal
r1 = busqueda_lineal(pedidos, "P001")
print("\nResultado Busqueda Lineal :")
print(r1)
print("================================")

# Probando la Búsqueda Lineal Acotada
r2 = busqueda_lineal_acotada(pedidos, "P005")
print("\nResultado Busqueda Lineal Acotada :")
print(r2)
print("================================")

# Probando la Búsqueda Binaria Iterativa
r3 = busqueda_binaria_iterativa(pedidos, "P003")
print("\nResultado Busqueda Binaria Iterativa :")
print(r3)
print("================================")

# Probando la Búsqueda Binaria Recursiva
r4 = busqueda_binaria_recursiva(pedidos, "P002", 0, len(pedidos) - 1)
print("\nResultado Busqueda Binaria Recursiva :")
print(r4)
print("================================")