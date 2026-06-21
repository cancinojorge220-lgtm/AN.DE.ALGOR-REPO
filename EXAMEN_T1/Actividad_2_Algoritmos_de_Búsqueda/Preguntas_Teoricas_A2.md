# a. ¿Qué requisitos deben cumplirse para aplicar búsqueda binaria?
El requisito obligatorio es que debe estar ordenada, ya sea de menor a mayor o de mayor a menor, según el campo que vas a usar para buscar.

# b. ¿Cuál de los algoritmos resulta más eficiente para una lista de 10 000 pedidos?
La Búsqueda Binaria, ya sea la iterativa o la recursiva. Si se usara la búsqueda lineal, en el peor de los casos la computadora tendría que revisar los 10,000 pedidos uno por uno hasta encontrar el correcto. En cambio, como la búsqueda binaria va partiendo la lista a la mitad en cada paso, haciendola mas rapida y eficiente para este caso.

# c. Analice la complejidad temporal de cada algoritmo.
Usando la notación Big O, podemos evaluar lo siguiente:

    - Búsqueda Lineal: 
    Su complejidad es $O(n)$. Esto significa que si la lista de pedidos crece, el tiempo que tarda el algoritmo crece exactamente en la misma proporción. Si la lista se duplica, el tiempo se duplica.

    - Búsqueda Lineal Acotada: 
    También es $O(n)$. A nivel de eficiencia el algoritmo esta obligado a revisar los elementos uno por uno desde el principio. Por eso, aunque en la práctica ahorra unas milésimas de segundo en procesador, técnicamente sigue tardando lo mismo y pertenece a la misma categoría de velocidad que la lineal común.
    
    - Búsqueda Binaria Iterativa: 
    Su complejidad es $O(\log n)$. El tiempo crece de forma lentísima aunque le metamos millones de pedidos.

    - Búsqueda Binaria Recursiva: 
    En tiempo también es $O(\log n)$, pero tiene un pequeño truco en contra, al llamarse a sí misma de forma recursiva, va acumulando memoria en la computadora.