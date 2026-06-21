# Preguntas Teóricas - Tipos Estructurados, Registros y Cadenas

# a ¿Por qué la estructura elegida resulta adecuada para almacenar la información?
Básicamente porque un pedido es un "paquete" en donde tienes datos como: texto para el Código o el Cliente, y números para el Peso y el Costo. Por lo que un diccionario es lo ideal para esto porque te deja agrupar datos de diferentes tipos en un solo lugar. Además, al meter esos diccionarios dentro de una lista, la estructura se vuelve súper flexible; podemos meter 15, 50 o los pedidos que queramos de forma ordenada y recorrerlos sin problemas.

# b. ¿Qué ventajas ofrece utilizar registros (diccionarios) frente a listas simples?
La ventaja millonaria es el orden y la claridad gracias al sistema de clave-valor (key-value). Si usáramos una lista simple para cada pedido, tendrías que acordarte de memoria que el índice [0] es el código, el [1] es el cliente, y así; si te equivocas de número, rompes todo. Con el diccionario vas directo al grano usando etiquetas claras como pedido["cliente"].

Otra ventaja técnica es la mantenibilidad: si mañana el negocio cambia y nos piden agregar, por ejemplo, la "Fecha de entrega", se añade como una clave más al diccionario y listo, no se nos descuadra ningún índice ni se rompe el código que ya teníamos hecho.