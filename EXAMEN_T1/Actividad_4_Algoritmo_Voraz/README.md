# Actividad 4: Algoritmo Voraz

## Objetivo
Comprender el concepto y la implementación de un algoritmo voraz (greedy) mediante la resolución del clásico problema del cambio de monedas/billetes. El objetivo es entregar un monto específico utilizando la menor cantidad de billetes posible.

## Algoritmos Utilizados
Se implementó un **algoritmo voraz** en el archivo `cambio_voraz.py`. Este algoritmo funciona iterando sobre una lista de denominaciones de billetes ordenadas de mayor a menor valor. En cada iteración, intenta utilizar la mayor cantidad posible del billete actual antes de pasar al siguiente, reduciendo así rápidamente el monto restante.

## Ejemplo de Ejecución
Para probar el algoritmo, abre la terminal en Visual Studio Code y ejecuta:

```bash
python Actividad_4_Algoritmo_Voraz/cambio_voraz.py
```

El programa calculará automáticamente el cambio óptimo para los montos:
- S/. 380
- S/. 670
- S/. 920

## Conclusiones
*   Los algoritmos voraces son soluciones muy rápidas y directas para ciertos problemas de optimización.
*   En sistemas de monedas estándar (como el peruano usado en este ejemplo: 200, 100, 50, 20, 10), el enfoque voraz siempre encuentra la solución óptima (menor cantidad de billetes).
*   A pesar de su utilidad, hay que ser cautelosos al aplicar algoritmos voraces, ya que en sistemas con diferentes restricciones u otros valores numéricos, podrían no encontrar la mejor respuesta global.
