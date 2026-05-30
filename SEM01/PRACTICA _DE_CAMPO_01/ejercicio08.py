# EJERCICIO 8: FUERZA BRUTA PARA CONTRASEÑAS
# ¿Qué limitaciones presenta este algoritmo cuando la contraseña es más larga?
# La principal limitación es el tiempo de ejecución (crecimiento exponencial). 
# Con 3 dígitos numéricos son 1000 combinaciones posibles. Si añadimos más dígitos, 
# o caracteres alfanuméricos, el espacio de búsqueda crece de manera astronómica, 
# haciendo que la fuerza bruta sea inviable.

def descifrar_contrasena():
    # Contraseña ingresada por el usuario
    contrasena_real = input("Ingrese una contraseña numérica de 3 dígitos (000-999): ")
    
    if len(contrasena_real) != 3 or not contrasena_real.isdigit():
        print("La contraseña debe tener exactamente 3 dígitos numéricos.")
        return

    intentos = 0
    encontrada = False

    print("Iniciando ataque de fuerza bruta...")
    
    # Probar combinaciones desde 000 hasta 999
    for i in range(1000):
        intentos += 1
        # Formatear el número para que tenga 3 dígitos con ceros a la izquierda
        intento_actual = f"{i:03}"
        
        if intento_actual == contrasena_real:
            print(f"¡Contraseña descubierta! La contraseña es: {intento_actual}")
            encontrada = True
            break
            
    print(f"Cantidad de intentos realizados: {intentos}")

if __name__ == "__main__":
    descifrar_contrasena()
