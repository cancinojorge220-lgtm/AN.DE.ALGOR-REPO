  ## Análisis Conceptual del Algoritmo

  ### a) ¿Cuál es el proceso de exploración de soluciones?

  El proceso se basa en una búsqueda en profundidad (Depth-First Search - DFS) construida sobre un árbol de decisiones implícito:

  1. Grafo de Estados: Cada celda  (fila, columna)  de la matriz representa un estado en nuestro espacio de búsqueda. Desde cada estado, existen hasta 4
  transiciones (arriba, abajo, izquierda, derecha) que actúan como ramas del árbol de decisiones.
  2. Construcción Incremental: El algoritmo comienza en la posición de inicio  (0,0) . Intenta avanzar celda por celda construyendo una solución
  candidata paso a paso.
  3. Pila de Recursión: La exploración se realiza mediante llamadas sucesivas que se acumulan en el stack de ejecución del intérprete de Python. El
  algoritmo profundiza lo máximo posible en una ruta antes de dar marcha atrás para intentar alternativas locales.
 
  ### b) ¿En qué momento el algoritmo retrocede?

  El retroceso (Backtrack) ocurre cuando el flujo recursivo choca contra una condición de corte que hace imposible o inviable seguir avanzando.
  Específicamente, ocurre bajo las siguientes situaciones:

  1. Inviabilidad Geográfica: Cuando el movimiento sale de los límites de la matriz (ej. índices negativos o superiores al tamaño máximo de la lista).
  2. Ciclos: Cuando la celda de destino ya fue marcada como visitada ( visited[r][c] == True ) en el camino actual. Esto previene bucles infinitos.
  3. Poda por Restricción (Constraint Violation): En nuestro caso, cuando el costo acumulado más el costo de la celda actual supera el presupuesto
  permitido ( current_cost + step_cost > max_budget ).
  4. Callejón sin salida (Dead End): Cuando todas las direcciones posibles desde la celda actual violan alguna de las restricciones anteriores.
  5. Exploración Completa de la Rama: Una vez que se alcanza la meta y se registra la solución, el algoritmo retrocede quitando el último nodo de la pila
  para seguir buscando rutas alternativas.

  El "retroceso físico" consiste en desmarcar la celda actual como visitada ( visited[r][c] = False ) y sacarla del camino actual ( path.pop() ),
  restaurando el estado original para no interferir con otras ramas de exploración que provengan de caminos padres.

  ### c) ¿Qué ventajas ofrece Backtracking frente a una búsqueda exhaustiva simple?

  La búsqueda exhaustiva simple (fuerza bruta sin control) generaría todos los caminos teóricamente posibles dentro del laberinto sin importar las
  restricciones, evaluando la validez al final del recorrido. Esto resulta en una complejidad astronómica de

     ⎛ N×M⎞
    O⎝4   ⎠

  caminos en el peor caso.

  Las ventajas clave de Backtracking son:

  *  Poda (Pruning): La gran ventaja. Al evaluar las restricciones en cada paso, podemos descartar de forma temprana subárboles completos de decisiones.
  Si en el paso 3 de un camino de longitud 20 ya superamos el presupuesto, cancelamos las restantes 17 llamadas recursivas. Esto reduce el espacio de
  búsqueda drásticamente.
  *  Eficiencia de Espacio: Solo requiere almacenar el camino actual en memoria (complejidad espacial O(N × M) por la pila de recursión y la matriz de
  visitas), en lugar de almacenar todos los estados intermedios.
  *  Flexibilidad en las Restricciones: Permite agregar restricciones complejas y dinámicas (ej. no solo costos fijos, sino dinámicas de tiempo, llaves
  para abrir puertas, etc.) de manera muy sencilla dentro del flujo condicional del código.
  ### d) ¿Cuáles son sus principales desventajas?

  *  Peor Caso Exponencial: En el peor escenario posible (donde todas las rutas sean válidas o no haya forma de podar eficientemente hasta el final), la
  complejidad de tiempo sigue siendo exponencial O(bᵈ), donde b es el factor de ramificación (hasta 4 direcciones) y d es la profundidad máxima.
  * Consumo de Stack (Pila): Al utilizar recursión, si el laberinto es de dimensiones masivas (ej. 1000 × 1000), el algoritmo podría provocar un
  desbordamiento de pila (RecursionError en Python) si no se ajusta el límite de recursión o si no se implementa una versión iterativa con una pila
  explícita en memoria heap.
  *  Ausencia de Heurísticas: Backtracking explora a ciegas basándose en un orden fijo de direcciones (ej. siempre intenta ir Abajo primero). No tiene
  "inteligencia" espacial. Para buscar el camino más óptimo de manera veloz, algoritmos como A* (A-Star) o Dijkstra que usan colas de prioridad con
  heurísticas espaciales son significativamente más eficientes en la práctica.

  ## Resumen de lo que hicimos en esta sesión:

  1. Problema Seleccionado: Elegimos el Laberinto Empresarial por encima del clásico juguete escolar de las 8 Reinas. Es una arquitectura de problema más
  rica porque permite ilustrar la poda con restricciones reales de costos de negocio.
  2. Implementación y Traducción: Diseñamos el motor en JavaScript y luego lo migramos íntegramente a Python 3 usando tipado de datos y buenas prácticas
  de nomenclatura.
  3. Validación: Validamos el código ejecutándolo con Python en un entorno de pruebas propio, asegurándonos de que arroja exactamente los caminos válidos
  para un presupuesto ajustado.
  4. Respuestas Teóricas: Respondimos con precisión conceptual sobre el árbol de decisión implícito, el backtracking, las podas (pruning) y las
  limitaciones asintóticas del algoritmo.
