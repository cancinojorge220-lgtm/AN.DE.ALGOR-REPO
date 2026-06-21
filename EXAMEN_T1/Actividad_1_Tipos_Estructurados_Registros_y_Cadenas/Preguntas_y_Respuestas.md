# Preguntas Teóricas - Tipos Estructurados, Registros y Cadenas

# a ¿Por qué la estructura elegida resulta adecuada para almacenar la información?
Básicamente porque un pedido es un "paquete" en donde tienes datos como: texto para el Código o el Cliente, y números para el Peso y el Costo. Por lo que un diccionario es lo ideal para esto porque te deja agrupar datos de diferentes tipos en un solo lugar. Además, al meter esos diccionarios dentro de una lista, la estructura se vuelve súper flexible; podemos meter 15, 50 o los pedidos que queramos de forma ordenada y recorrerlos sin problemas.

# b. ¿Qué ventajas ofrece utilizar registros (diccionarios) frente a listas simples?
Legibilidad mediante claves (Key-Value): En una lista simple tendrías que recordar la posición indexada de cada dato (ej. pedido[0] para código, pedido[1] para cliente). Con un diccionario, accedes directamente por su nombre descriptivo (pedido["cliente"]), lo que reduce errores humanos y vuelve el código autodocumentado.

Flexibilidad: Si en el futuro la empresa requiere añadir un nuevo campo (como "Fecha de envío"), en el diccionario se agrega la nueva clave sin alterar ni romper el orden o la lógica de los índices preexistentes.