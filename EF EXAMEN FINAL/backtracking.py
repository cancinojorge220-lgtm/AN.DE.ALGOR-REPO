# ==============================================================================
# ALGORITMO DE BACKTRACKING - PLANIFICACIÓN DE RUTAS
# Caso de Estudio: Logística Andina S.A.C.
# ==============================================================================

import os
from generador_visualizacion import generar_html_interactivo

# Estructura para registrar los pasos lógicos del algoritmo (Traza de ejecución)
historial_pasos = []

def registrar_evento(tipo, origen, destino, visitados, mensaje):
    """Registra un evento en el historial para posterior renderizado visual."""
    historial_pasos.append({
        "tipo": tipo,
        "origen": origen,
        "destino": destino,
        "visitados": list(visitados),
        "mensaje": mensaje
    })

def es_movimiento_valido(origen, destino, visitados, conexiones, bloqueos):
    """Evalúa las restricciones logísticas en base al modelo del grafo y las reglas de backtracking."""
    # Regla 1: Debe existir una conexión vial directa en el grafo
    if destino not in conexiones.get(origen, []):
        registrar_evento("rechazado", origen, destino, visitados, f"Rechazado: No hay conexión vial directa entre {origen} y {destino}.")
        return False
        
    # Regla 2: La carretera no debe estar bloqueada por derrumbes o mantenimiento
    if (origen, destino) in bloqueos or (destino, origen) in bloqueos:
        registrar_evento("rechazado", origen, destino, visitados, f"RESTRICCIÓN: Vía {origen} - {destino} bloqueada permanentemente.")
        return False
        
    # Regla 3: No pasar dos veces por el mismo almacén (Camino Hamiltoniano simple)
    if destino in visitados:
        registrar_evento("rechazado", origen, destino, visitados, f"Rechazado: {destino} ya fue visitado en esta ruta.")
        return False
        
    return True

def buscar_ruta(actual, almacenes_objetivo, visitados, conexiones, bloqueos, paso=1):
    """
    Algoritmo recursivo en profundidad (DFS) para resolver el Camino Hamiltoniano
    utilizando Backtracking y podas dinámicas de estados inviables.
    """
    # CASO BASE: Si se han visitado todos los almacenes objetivos, la ruta es exitosa.
    if len(visitados) == len(almacenes_objetivo):
        registrar_evento("exito", actual, None, visitados, f"¡Ruta hamiltoniana de {len(visitados)} almacenes completada con éxito!")
        return list(visitados)
    
    # Explorar recursivamente cada vecino disponible (ramas de estados)
    for siguiente in conexiones.get(actual, []):
        registrar_evento("evaluar", actual, siguiente, visitados, f"Evaluando paso: {actual} -> {siguiente}...")
        
        # Validación de restricciones logísticas (Propiedad de viabilidad)
        if es_movimiento_valido(actual, siguiente, visitados, conexiones, bloqueos):
            # Aceptar decisión (Avanzar en el árbol de estados)
            visitados.append(siguiente)
            registrar_evento("avanzar", actual, siguiente, visitados, f"Vía libre. Avanzando hacia {siguiente}.")
            
            # Llamada recursiva en profundidad
            resultado = buscar_ruta(siguiente, almacenes_objetivo, visitados, conexiones, bloqueos, paso + 1)
            if resultado:
                return resultado
                
            # retroceso (BACKTRACKING): Deshacer la decisión en el retorno de la recursión
            visitados.pop()
            registrar_evento("backtrack", siguiente, actual, visitados, f"Callejón sin salida desde {siguiente}. Retrocediendo a {actual}...")
            
    return None

def leer_almacenes_desde_despachos():
    """Lee el archivo resultado_despachos.txt y extrae la lista de almacenes despachados por el voraz."""
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_txt = os.path.join(dir_actual, "resultado_despachos.txt")
    almacenes_leidos = []
    
    if os.path.exists(ruta_txt):
        with open(ruta_txt, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("- A."):
                    # Extraer nombre, ej: " - A.Puno: 340 kg" -> "A.Puno"
                    nombre = line.split(":")[0].replace("-", "").strip()
                    if nombre not in almacenes_leidos:
                        almacenes_leidos.append(nombre)
    return almacenes_leidos

if __name__ == "__main__":
    # 1. Leer dinámicamente los almacenes seleccionados por el algoritmo voraz
    almacenes_despachados = leer_almacenes_desde_despachos()
    
    # Definimos el conjunto de los 8 almacenes terrestres transitables en nuestra red
    terrestres_red = {
        "A.Huaraz", "A.Piura", "A.Cusco", "A.Arequipa", 
        "A.Trujillo", "A.Chiclayo", "A.Huancayo", "A.Ayacucho"
    }
    
    # Filtrar para obtener el orden exacto del despacho de tu compañero
    if almacenes_despachados:
        almacenes_objetivo = [a for a in almacenes_despachados if a in terrestres_red]
    else:
        # Fallback si no encuentra el archivo resultado_despachos.txt
        almacenes_objetivo = list(terrestres_red)
        
    # Aseguramos que Lima se mantenga como punto de partida en la visualización
    if "A.Lima" not in almacenes_objetivo:
        # Lima es el origen de operaciones logísticas central
        nombres_para_visualizacion = ["A.Lima"] + almacenes_objetivo
    else:
        nombres_para_visualizacion = almacenes_objetivo
    
    # Coordenadas bidimensionales para el modelado gráfico en el simulador
    coordenadas_almacenes = {
        "A.Piura": {"x": 100, "y": 80},
        "A.Chiclayo": {"x": 140, "y": 160},
        "A.Trujillo": {"x": 190, "y": 240},
        "A.Huaraz": {"x": 220, "y": 300},
        "A.Lima": {"x": 280, "y": 380},
        "A.Huancayo": {"x": 380, "y": 330},
        "A.Ayacucho": {"x": 400, "y": 440},
        "A.Cusco": {"x": 490, "y": 420},
        "A.Arequipa": {"x": 470, "y": 540}
    }
    
    # 2. Grafo de la red vial nacional con la adición de Huaraz
    conexiones_red = {
        "A.Lima": ["A.Huancayo", "A.Trujillo", "A.Chiclayo", "A.Arequipa", "A.Huaraz"],
        "A.Huaraz": ["A.Lima", "A.Trujillo", "A.Huancayo"],
        "A.Piura": ["A.Chiclayo"],
        "A.Cusco": ["A.Huancayo", "A.Ayacucho", "A.Arequipa"],
        "A.Arequipa": ["A.Ayacucho", "A.Cusco", "A.Lima"],
        "A.Trujillo": ["A.Lima", "A.Chiclayo", "A.Huancayo", "A.Huaraz"],
        "A.Chiclayo": ["A.Trujillo", "A.Piura", "A.Lima"],
        "A.Huancayo": ["A.Lima", "A.Cusco", "A.Trujillo", "A.Huaraz"],
        "A.Ayacucho": ["A.Cusco", "A.Arequipa"]
    }
    
    # 3. Conjunto de Vías Bloqueadas (Restricciones del problema)
    vias_bloqueadas = {
        ("A.Huancayo", "A.Ayacucho"),  # Carretera en mantenimiento (Problemática)
        ("A.Trujillo", "A.Piura"),     # Deslizamiento activo
        ("A.Lima", "A.Cusco")          # Restricción de conexión directa
    }
    
    # Iniciar búsqueda partiendo desde Lima Metropolitana
    punto_inicio = "A.Lima"
    visitados_iniciales = [punto_inicio]
    
    print("=" * 60)
    print("INICIANDO CÁLCULO DE BACKTRACKING CON INTEGRACIÓN DINÁMICA...")
    print(f"Almacenes leídos del Voraz: {almacenes_objetivo}")
    print("=" * 60)
    
    # Ejecución del algoritmo principal sobre la lista inyectada del voraz
    ruta_final = buscar_ruta(punto_inicio, nombres_para_visualizacion, visitados_iniciales, conexiones_red, vias_bloqueadas)
    
    # Delegar la renderización interactiva y visualización web a la capa de UI
    generar_html_interactivo(historial_pasos, coordenadas_almacenes, conexiones_red, vias_bloqueadas)
