# Preguntas Teóricas - Tipos Estructurados, Registros y Cadenas

# a ¿Por qué la estructura elegida resulta adecuada para almacenar la información?
Se seleccionó esta estructura porque cada pedido contiene diversos tipos de datos, encontramos cadenas de texto, junto con valores numéricos para el Peso y el Costo. Bajo esa premisa lo ideal es usar diccionarios para facilitar la agrupación organizada de la información.

# b. ¿Qué ventajas ofrece utilizar registros (diccionarios) frente a listas simples?
La ventaja esta en el orden y la claridad gracias al sistema de clave y valor. Si usáramos una lista simple para cada pedido tendriamos que acordarnos de memoria que el índice [0] es el código, el [1] es el cliente, y así; si te equivocas de número, rompes todo. Con el diccionario vas directo al grano usando etiquetas claras como pedido["cliente"].