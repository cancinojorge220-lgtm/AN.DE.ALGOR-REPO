#EJERCICIO 5: DICCIONARIOS
#¿Cuál es la diferencia entre un diccionario y una lista?
#La diferencia entre un diccionario y una lista es que un diccionario es una colección de pares clave-valor,
#mientras que una lista es una colección ordenada de elementos.

trabajador={
    "nombre": "Jorge",
    "edad": 30,
    "area": "Desarrollo de Software",
    "sueldo": 5000
}

#Mostrar todos los datos. 
print("Datos del Trabajador:")

for atributo, valor in trabajador.items():
    print(" -" + atributo + ": " + str(valor))  

#Modificar el sueldo. 
trabajador["sueldo"] = 5500  
print("\nSueldo modificado: ", trabajador["sueldo"])

#Agregar el campo Correo. 
trabajador["correo"] = "jorge@empresa.com"
print("\nCorreo agregado: ", trabajador["correo"])
