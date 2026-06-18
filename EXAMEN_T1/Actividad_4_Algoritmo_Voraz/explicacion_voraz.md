# Explicación del Algoritmo Voraz (Greedy)

### 1. ¿Qué es un algoritmo voraz?
Un algoritmo voraz (o greedy) es una estrategia de resolución de problemas que toma la mejor decisión posible en cada paso de manera local y en el momento, con la esperanza de que estas elecciones locales óptimas lleven a una solución global óptima. No reconsidera sus decisiones; una vez que toma un camino, sigue adelante.

### 2. ¿Por qué el algoritmo toma primero los billetes de mayor valor?
Toma primero los billetes de mayor valor porque su objetivo inmediato ("voraz") en cada paso es reducir la cantidad de dinero restante lo más rápido posible. Al usar el billete más grande disponible, se minimiza la cantidad total de billetes que se necesitarán al final. Esta es la esencia de su comportamiento codicioso.

### 3. Ventajas del enfoque voraz
*   **Simplicidad:** Son generalmente muy fáciles de entender, pensar y programar.
*   **Rapidez:** Suelen ser muy rápidos y eficientes en tiempo de ejecución, ya que solo recorren los datos una vez sin necesidad de cálculos complejos o de probar múltiples combinaciones.
*   **Eficiencia de memoria:** Utilizan muy pocos recursos porque no guardan estados previos.

### 4. Desventajas del enfoque voraz
*   **No siempre dan la respuesta correcta:** La principal desventaja es que no garantizan encontrar la solución óptima (la mejor) en todos los problemas. Solo funciona bien para problemas específicos (como este problema de cambio con este sistema de monedas en particular).
*   **Miopía:** Solo miran el paso actual y no consideran las consecuencias futuras de sus decisiones.

### 5. Casos donde una estrategia voraz puede fallar
Una estrategia voraz falla cuando tomar la mejor decisión a corto plazo te impide alcanzar la mejor decisión a largo plazo.

**Ejemplo en el problema del cambio:**
Imaginemos que en un país extraño existen billetes de **S/. 25, S/. 20 y S/. 5**.
Queremos dar un cambio de **S/. 40**.

*   **Algoritmo Voraz:** Tomará primero el billete más grande que pueda: un billete de S/. 25. Le faltarán S/. 15. Luego intentará tomar de S/. 20 (no puede). Tomará de S/. 5 (tres billetes).
    *   *Resultado Voraz:* 1 billete de 25 + 3 billetes de 5 = **4 billetes en total**.
*   **Solución Óptima Real:** Dar 2 billetes de S/. 20.
    *   *Resultado Óptimo:* **2 billetes en total**.

En este caso ficticio, el algoritmo voraz fracasó en encontrar la solución que usa la menor cantidad de billetes, porque al ser codicioso en el primer paso (tomar el 25), cerró la puerta a la mejor combinación (20 + 20). En nuestro sistema monetario real de 200, 100, 50, 20, 10, sí funciona a la perfección.
