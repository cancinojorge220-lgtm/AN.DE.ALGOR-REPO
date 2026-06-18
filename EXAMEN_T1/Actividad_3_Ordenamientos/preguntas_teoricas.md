# Preguntas Teóricas - Algoritmos de Ordenamiento

### 1. ¿Cómo funciona el algoritmo Burbuja?
El algoritmo Burbuja funciona comparando repetidamente pares de elementos adyacentes en una lista. Si el primer elemento es mayor que el segundo, los intercambia de posición. Este proceso "empuja" o "hace burbujear" los valores más grandes hacia el final de la lista en cada pasada. El recorrido por la lista se repite hasta que no se necesiten más intercambios, lo que significa que la lista está ordenada.

### 2. ¿Cómo funciona el algoritmo Selección?
El algoritmo Selección divide la lista en dos partes: una parte ordenada y otra no ordenada. En cada paso, busca el elemento más pequeño dentro de la parte no ordenada y lo intercambia con el primer elemento de esa parte. Luego, mueve el límite entre las dos partes un elemento hacia la derecha. De esta forma, va construyendo la lista ordenada seleccionando siempre el menor elemento disponible.

### 3. ¿Cómo funciona el algoritmo Inserción?
El algoritmo Inserción funciona de manera similar a como ordenamos cartas en nuestra mano. Toma un elemento de la lista y busca su posición correcta dentro de los elementos que ya revisó (la parte izquierda de la lista). Para hacer espacio, desplaza hacia la derecha todos los elementos mayores que el actual, y luego "inserta" el elemento en el hueco encontrado.

### 4. ¿Cuál fue más eficiente para la cantidad de datos utilizada?
Para la cantidad pequeña de datos que utilizamos (5 pedidos), el algoritmo de **Inserción** fue el más eficiente en términos de cantidad de iteraciones. Esto se debe a que la inserción detiene sus comparaciones tan pronto como encuentra la posición correcta para un elemento, mientras que la versión básica de Burbuja y Selección siempre realizan todas las comparaciones posibles independientemente de si los datos ya están ordenados parcialmente.

### 5. ¿En qué situaciones conviene usar cada algoritmo?
*   **Burbuja:** Solo se recomienda para fines educativos o para listas extremadamente pequeñas, ya que es el menos eficiente en la mayoría de los casos. Podría ser útil si la lista ya está casi ordenada y se utiliza una versión optimizada del algoritmo.
*   **Selección:** Es útil cuando el costo de escribir o intercambiar elementos en memoria es muy alto y queremos minimizar la cantidad de intercambios (Selección hace como máximo *n* intercambios, menos que Burbuja o Inserción).
*   **Inserción:** Es el mejor de los tres para listas pequeñas o para listas que ya están casi ordenadas. En la práctica, muchos lenguajes de programación usan una variante de Inserción como parte de algoritmos más complejos (como Timsort en Python) para ordenar bloques pequeños de datos debido a su alta velocidad y simplicidad.
