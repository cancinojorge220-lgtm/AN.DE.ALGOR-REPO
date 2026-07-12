# Algoritmo voraz para seleccionar almacenes a cargar en un camión
def calcular_carga_voraz(lista_almacenes, capacidad_max):
    # Calculamos el factor de eficiencia
    for item in lista_almacenes:
        # Prioridad 1 es la más alta, peso_kg es el costo de capacidad
        # Factor = (1/prioridad) / peso_kg
        item["factor"] = (1 / item["prioridad"]) / item["peso_kg"]
    
    # Ordenamos de mayor a menor factor (Greedy choice)
    ordenados = sorted(lista_almacenes, key=lambda x: x["factor"], reverse=True)
    
    seleccionados = []
    peso_actual = 0
    
    for almacen in ordenados:
        if peso_actual + almacen["peso_kg"] <= capacidad_max:
            seleccionados.append(almacen)
            peso_actual += almacen["peso_kg"]
            
    return seleccionados, peso_actual

# Ejemplo de uso
from datos_almacenes import almacenes
from algoritmo_voraz import calcular_carga_voraz

# Definimos la capacidad máxima del camión
CAPACIDAD = 1000   # kg
seleccionados, peso_total = calcular_carga_voraz(almacenes, CAPACIDAD)

# Mostramos los resultados
print("Almacenes seleccionados para cargar en el camión:")
for almacen in seleccionados:
    print(f" - {almacen['nombre']}: {almacen['peso_kg']} kg")
print(f"Capacidad utilizada: {peso_total} kg de {CAPACIDAD} kg.")