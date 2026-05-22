#EJERCICIO 6: CADENAS DE TEXTO
#Pregunta: ¿Dónde se utilizan las cadenas de texto en aplicaciones reales?
#En aplicaciones reales, las cadenas de texto son esenciales para gestionar datos crticos, como nombres de usuario, 
#direcciones y correos institucionales.


frase = input("Ingrese una frase: ")

#Muestre la cantidad de caracteres.
print("\nCantidad de caracteres:", len(frase))

#Muestre la frase en mayúsculas.
print("\nFrase en mayúsculas:", frase.upper())

#Muestre la frase en minúsculas.
print("\nFrase en minúsculas:", frase.lower())

#Muestre la frase invertida.
print("\nFrase invertida:", frase[::-1])