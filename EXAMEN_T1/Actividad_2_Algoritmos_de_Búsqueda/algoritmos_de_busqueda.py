# Actividad 2: Algoritmos de Búsqueda
import sys
import os
# Agregar el directorio padre al sys.path para importar datos_pedidos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datos_pedidos import pedidos

# 1. BÚSQUEDA LINEAL
def busqueda_lineal(pedidos, codigo_buscado):
    # Recorrer la lista de pedidos y verificar si el código coincide con el código buscado
    for i in range(len(pedidos)):
        if pedidos[i]["codigo"] == codigo_buscado:
            return pedidos[i]
    return None


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
    return None


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
    return None


# 4. BÚSQUEDA BINARIA RECURSIVA
def busqueda_binaria_recursiva(pedidos, codigo_buscado, izquierda=0, derecha=None):
    # La lista de pedidos debe estar ordenada por código para que la búsqueda binaria funcione correctamente
    if derecha is None:
        derecha = len(pedidos) - 1
    
    # Caso base: si el rango de búsqueda es inválido, retornar None
    if izquierda > derecha:
        return None
    
    medio = (izquierda + derecha) // 2
    
    # Verificar si el código del pedido en la posición media coincide con el código buscado
    if pedidos[medio]["codigo"] == codigo_buscado:
        return pedidos[medio]
    elif pedidos[medio]["codigo"] < codigo_buscado:
        # Si el código del pedido en la posición media es menor que el código buscado, buscar en la mitad derecha
        return busqueda_binaria_recursiva(pedidos, codigo_buscado, medio + 1, derecha)
    else:
        # Si el código del pedido en la posición media es mayor que el código buscado, buscar en la mitad izquierda
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
r4 = busqueda_binaria_recursiva(pedidos, "P004")
print("\nResultado Busqueda Binaria Recursiva :")
print(r4)
print("================================")