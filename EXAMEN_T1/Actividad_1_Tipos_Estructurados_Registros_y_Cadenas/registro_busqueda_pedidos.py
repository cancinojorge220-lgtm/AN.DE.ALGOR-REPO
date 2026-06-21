# Definir la lista de pedidos como una lista de diccionarios
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datos_pedidos import pedidos

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