#02 ALGORITMO DE DIJKSTRA

import heapq

def dijkstra(grafo, inicio):
    #Empezamos asumiendo que todo está "lejos" (infinito)
    pasos = {lugar: float('infinity') for lugar in grafo}
    pasos[inicio] = 0
    
    #Lista de lugares por revisar (prioriza el que tenga menos pasos)
    revisar = [(0, inicio)]
    
    while revisar:
        pasos_actuales, lugar_actual = heapq.heappop(revisar)
        
        #Revisamos los lugares conectados
        for vecino, costo in grafo[lugar_actual].items():
            camino_corto = pasos_actuales + costo
            
            #Si este camino es más corto, lo guardamos
            if camino_corto < pasos[vecino]:
                pasos[vecino] = camino_corto
                heapq.heappush(revisar, (camino_corto, vecino))
                
    return pasos


#EL CAMPUS UPN
campus = {
    'Entrada': {'Aulas': 10, 'Biblioteca': 20},
    'Aulas': {'Cafetería': 15, 'Biblioteca': 2},
    'Biblioteca': {'Cafetería': 5},
    'Cafetería': {}
}

#Calculamos cuántos pasos toma llegar a cada lugar desde la Entrada
resultado = dijkstra(campus, 'Entrada')

#Mostramos el resultado en pantalla
print("PASOS DESDE LA ENTRADA:")
for lugar, total_pasos in resultado.items():
    print(f"-> Hacia la(s) {lugar}: {total_pasos} pasos")