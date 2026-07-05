# Caso Práctico 3: Teoría de Grafos — Optimización de Rutas con el Algoritmo de Dijkstra

## 1. Tabla de Iteraciones (Ejecución de Dijkstra)

El algoritmo de Dijkstra mantiene un registro de la distancia mínima conocida desde el nodo inicial ($A$) hacia todos los demás nodos, actualizándose a medida que se exploran los caminos de forma codiciosa (*greedy*).

Los valores tienen el formato **Distancia (Nodo Predecesor)**. El símbolo $\infty$ denota un nodo inalcanzable temporalmente.

| Iteración | Nodo Seleccionado (Permanente) | Distancia a A | Distancia a B | Distancia a C | Distancia a D | Distancia a E | Conjunto de Nodos No Visitados |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | *Inicio* | **0 (-)** | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\{A, B, C, D, E\}$ |
| **1** | **A** | 0 (-) | **4 (A)** | **2 (A)** | $\infty$ | $\infty$ | $\{B, C, D, E\}$ |
| **2** | **C** *(Menor: 2)* | 0 (-) | 4 (A) | 2 (A) | **10 (C)** | **12 (C)** | $\{B, D, E\}$ |
| **3** | **B** *(Menor: 4)* | 0 (-) | 4 (A) | 2 (A) | **9 (B)** | 12 (C) | $\{D, E\}$ |
| **4** | **D** *(Menor: 9)* | 0 (-) | 4 (A) | 2 (A) | 9 (B) | **11 (D)** | $\{E\}$ |
| **5** | **E** *(Menor: 11)* | 0 (-) | 4 (A) | 2 (A) | 9 (B) | **11 (D)** | $\emptyset$ (Vacío) |

---

## 2. Justificación Paso a Paso 


1. **Paso Inicial (Iteración 0 y 1):** Partiendo desde **A**, se evalúan sus vecinos directos. Se descubren los caminos hacia **B** con un costo de $4$ y hacia **C** con un costo de $2$. El resto de nodos permanecen con distancia infinita ($\infty$).
   
2. **Evaluación desde el Nodo C (Iteración 2):**
   El nodo no visitado más cercano es **C** (distancia 2). Al explorar desde **C**, se puede llegar a **D** con un costo acumulado de $2 + 8 = 10$, y a **E** con un costo directo de $2 + 10 = 12$. Estos valores se registran temporalmente.

3. **Evaluación desde el Nodo B (Iteración 3):**
   El siguiente nodo más cercano en la lista global es **B** (distancia 4). Al explorar desde **B**, se descubre que se puede llegar a **D** a través de la arista $B 
ightarrow D$ con un costo de $5$. Esto nos da un costo acumulado de $4 + 5 = 9$. Como $9 < 10$ (el camino anterior vía C), el algoritmo **actualiza y optimiza** la distancia hacia **D**, guardando a **B** como su nuevo predecesor.

4. **Evaluación desde el Nodo D (Iteración 4):**
   El nodo con la menor distancia acumulada disponible es **D** (distancia 9). Desde **D**, se puede alcanzar el destino final **E** utilizando la arista $D 
ightarrow E$ con un costo de $2$. El costo acumulado resultante es $9 + 2 = 11$. Al comparar este nuevo camino ($11$) con la ruta directa anterior vía C ($12$), se observa que pasar por D es más eficiente. Por lo tanto, se actualiza la distancia final a **E** como $11$.

5. **Finalización (Iteración 5):**
   El único nodo restante es el destino **E** con una distancia consolidada de $11$. El algoritmo termina al haber procesado todos los nodos del grafo.

