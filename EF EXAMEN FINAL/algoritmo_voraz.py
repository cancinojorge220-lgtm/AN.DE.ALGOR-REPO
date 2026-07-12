from datos_almacenes import almacenes

# Algoritmo Voraz (Greedy)
def calcular_carga_voraz(lista_almacenes, capacidad_max):
    # Definir heurística: Factor de eficiencia
    for item in lista_almacenes:
        item["factor"] = (1 / item["prioridad"]) / item["peso_kg"]
    
    # Ordenar por factor (Greedy choice: O(n log n))
    ordenados = sorted(lista_almacenes, key=lambda x: x["factor"], reverse=True)
    
    seleccionados = []
    peso_actual = 0
    
    for almacen in ordenados:
        if peso_actual + almacen["peso_kg"] <= capacidad_max:
            seleccionados.append(almacen)
            peso_actual += almacen["peso_kg"]
    
    return seleccionados, peso_actual

# Ejecución 
CAPACIDAD = 1000
ids_procesados = set()
viaje = 1

print("--- INICIANDO PLANIFICACIÓN DE DESPACHOS ---")

while len(ids_procesados) < len(almacenes):
    # Filtramos la lista para obtener solo los que NO han sido procesados
    pendientes = [a for a in almacenes if a['id'] not in ids_procesados]
    
    if not pendientes:
        break
        
    ruta, peso = calcular_carga_voraz(pendientes, CAPACIDAD)
    
    print(f"\n>>> CAMIÓN {viaje} <<<")
    for sitio in ruta:
        print(f" - {sitio['nombre']}: {sitio['peso_kg']} kg")
        ids_procesados.add(sitio['id'])
        
    print(f"Total cargado: {peso} kg.")
    viaje += 1

print("\n--- PROCESO FINALIZADO ---")