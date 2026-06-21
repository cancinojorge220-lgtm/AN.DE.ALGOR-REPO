# Grafo de ciudades y costos de conexión

grafo = {
    "Lima": {"Trujillo": 8, "Cusco": 10, "Arequipa": 12},
    "Trujillo": {"Lima": 8, "Chiclayo": 4},
    "Chiclayo": {"Trujillo": 4, "Piura": 3},
    "Piura": {"Chiclayo": 3},
    "Cusco": {"Lima": 10, "Arequipa": 5},
    "Arequipa": {"Lima": 12, "Cusco": 5}
}

# -------------------------
# RUTA ENTRE DOS CIUDADES
# (BFS - Búsqueda en Anchura)
# -------------------------

inicio = "Lima"
destino = "Piura"

cola = [[inicio]]
visitados = []

while cola:
    ruta = cola.pop(0)
    ciudad = ruta[-1]

    if ciudad == destino:
        print("Ruta encontrada:")
        print(" -> ".join(ruta))
        break

    if ciudad not in visitados:
        visitados.append(ciudad)

        for vecino in grafo[ciudad]:
            nueva_ruta = ruta + [vecino]
            cola.append(nueva_ruta)

# -------------------------
# ÁRBOL DE RECUBRIMIENTO MÍNIMO
# (PRIM)
# -------------------------

visitados = ["Lima"]
arbol = []
costo_total = 0

while len(visitados) < len(grafo):

    menor_costo = 999
    ciudad_origen = ""
    ciudad_destino = ""

    for ciudad in visitados:
        for vecino, costo in grafo[ciudad].items():

            if vecino not in visitados:
                if costo < menor_costo:
                    menor_costo = costo
                    ciudad_origen = ciudad
                    ciudad_destino = vecino

    arbol.append((ciudad_origen, ciudad_destino, menor_costo))
    visitados.append(ciudad_destino)
    costo_total += menor_costo

print("\nÁrbol de Recubrimiento Mínimo:")

for conexion in arbol:
    print(conexion[0], "-", conexion[1], "Costo:", conexion[2])

print("Costo total:", costo_total)