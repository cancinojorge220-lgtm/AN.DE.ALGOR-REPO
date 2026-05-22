#EJERCICIO 5: DICCIONARIOS
#Pregunta: ¿Cuál es la diferencia fundamental entre un diccionario y una lista? 
#A diferencia de una lista, que se define como una agrupación ordenada de ítems, 
#un diccionario se caracteriza por ser una estructura basada en asociaciones de pares clave-valor.


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
