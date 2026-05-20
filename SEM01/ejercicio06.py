#EJERCICIO 6: CADENAS DE TEXTO
#¿Dónde se utilizan las cadenas de texto en aplicaciones reales?
#Las cadenas de texto se utilizan en aplicaciones reales para almacenar y manipular información de texto,
#como nombres, direcciones, mensajes, etc.

frase = input("Ingrese una frase: ")

#Muestre la cantidad de caracteres.
print("\nCantidad de caracteres:", len(frase))

#Muestre la frase en mayúsculas.
print("\nFrase en mayúsculas:", frase.upper())

#Muestre la frase en minúsculas.
print("\nFrase en minúsculas:", frase.lower())

#Muestre la frase invertida.
print("\nFrase invertida:", frase[::-1])