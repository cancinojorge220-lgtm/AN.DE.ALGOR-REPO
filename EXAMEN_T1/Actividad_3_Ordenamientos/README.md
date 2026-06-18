# Actividad 3: Algoritmos de Ordenamiento

## Objetivo
El objetivo de esta actividad es implementar, comparar y analizar tres algoritmos clásicos de ordenamiento (Burbuja, Selección e Inserción). Se busca ordenar una lista de diccionarios (pedidos) basándonos en su costo de envío, de menor a mayor.

## Algoritmos Utilizados
1.  **Burbuja (`burbuja.py`)**: Intercambia elementos adyacentes si están en el orden incorrecto.
2.  **Selección (`seleccion.py`)**: Busca el elemento mínimo de la lista no ordenada y lo coloca al principio.
3.  **Inserción (`insercion.py`)**: Toma elementos uno por uno y los inserta en su posición correcta respecto a los ya ordenados.
4.  **Comparación (`comparacion_resultados.py`)**: Ejecuta los tres algoritmos, valida que den el mismo resultado y compara su eficiencia midiendo las iteraciones.

## Ejemplo de Ejecución
Para probar cualquier algoritmo, abre la terminal en Visual Studio Code y ejecuta:

```bash
python Actividad_3_Ordenamientos/burbuja.py
python Actividad_3_Ordenamientos/comparacion_resultados.py
```

Al ejecutar `comparacion_resultados.py`, obtendremos la cantidad de iteraciones internas, demostrando qué algoritmo hace menos trabajo para llegar al mismo resultado.

## Conclusiones
*   Los tres algoritmos logran el mismo resultado final: una lista ordenada.
*   Para nuestra lista de datos pequeña, **Inserción** demostró ser el más eficiente porque requiere menos pasos (iteraciones internas) al aprovechar el orden parcial de los datos.
*   Estos algoritmos básicos nos ayudan a entender la lógica de programación y la importancia de analizar la eficiencia (Complejidad Algorítmica).
