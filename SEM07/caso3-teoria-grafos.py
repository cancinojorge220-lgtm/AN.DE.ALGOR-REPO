import heapq


def dijkstra(grafo, inicio, destino):
    # Inicializamos todas las distancias con infinito, excepto el nodo de inicio (0)
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0

    # Diccionario para guardar el camino recorrido
    rutas = {nodo: [] for nodo in grafo}
    rutas[inicio] = [inicio]

    # Cola de prioridad para explorar siempre el nodo más cercano disponible
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        (distancia_actual, nodo_actual) = heapq.heappop(cola_prioridad)

        # Si la distancia actual es mayor a la guardada, la ignoramos
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Explorar vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si encontramos un camino más corto hacia el vecino, actualizamos
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                rutas[vecino] = rutas[nodo_actual] + [vecino]
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return rutas[destino], distancias[destino]


grafo_mensajeria = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

# Aplicar el algoritmo desde A hasta E
ruta_optima, distancia_total = dijkstra(grafo_mensajeria, 'A', 'E')

print("--- Resultados de la Ruta ---")
print(f"Ruta óptima: {' -> '.join(ruta_optima)}")
print(f"Distancia total recorrida: {distancia_total}")