import os # Importar módulo para manejo de rutas y archivos
from datos_almacenes import almacenes # Importar la lista de almacenes desde el archivo datos_almacenes.py

# Algoritmo Voraz (Greedy)
def calcular_carga_voraz(lista_almacenes, capacidad_max):
    
    # Calcular el factor de prioridad/peso para cada almacén
    for item in lista_almacenes:
        item["factor"] = (1 / item["prioridad"]) / item["peso_kg"]
    
    # Ordenar los almacenes por el factor calculado (de mayor a menor)
    ordenados = sorted(lista_almacenes, key=lambda x: x["factor"], reverse=True)
    
    seleccionados = []
    peso_actual = 0
    
    for almacen in ordenados:
        if peso_actual + almacen["peso_kg"] <= capacidad_max:
            seleccionados.append(almacen)
            peso_actual += almacen["peso_kg"]
    
    return seleccionados, peso_actual

def guardar_despacho(ruta, peso, despacho_num, file_path):
    """Escribe la información del despacho en `file_path` (añade al final)."""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"\nDESPACHO {despacho_num}\n")
        for sitio in ruta:
            f.write(f" - {sitio['nombre']}: {sitio['peso_kg']} kg\n")
        f.write(f"Total cargado: {peso} kg.\n")

# Guardar resultados en un archivo de texto
file_path = os.path.join(os.path.dirname(__file__), 'resultado_despachos.txt')

# Ejecución 
CAPACIDAD = 1000 # Capacidad máxima del camión (kg)
ids_procesados = set()
despacho = 1


# Inicializar/limpiar archivo de resultados
with open(file_path, 'w', encoding='utf-8') as _f:
    _f.write("INICIANDO PLANIFICACIÓN DE DESPACHOS\n")

# Bucle principal para procesar los almacenes
print("INICIANDO PLANIFICACIÓN DE DESPACHOS")

while len(ids_procesados) < len(almacenes):
    # Filtramos la lista para obtener solo los que NO han sido procesados
    pendientes = [a for a in almacenes if a['id'] not in ids_procesados]
    
    if not pendientes:
        break
        
    ruta, peso = calcular_carga_voraz(pendientes, CAPACIDAD)
    
    # Guardar los IDs de los almacenes procesados
    print(f"\nDESPACHO {despacho}")
    for sitio in ruta:
        print(f" - {sitio['nombre']}: {sitio['peso_kg']} kg")
        ids_procesados.add(sitio['id'])
        
    print(f"Total cargado: {peso} kg.")
    
    # Guardar el despacho en el archivo
    guardar_despacho(ruta, peso, despacho, file_path)
    despacho += 1

print("\nPROCESO FINALIZADO")