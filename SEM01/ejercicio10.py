# EJERCICIO 10: CIFRADO CÉSAR
# ¿Por qué este procedimiento se considera un ataque de fuerza bruta?
# Se considera fuerza bruta porque en lugar de intentar analizar el texto, buscar patrones 
# o deducir la clave (criptoanálisis), simplemente prueba metódicamente una por una 
# todas las claves posibles (el espacio de búsqueda completo de 26 opciones) hasta 
# que una produce un mensaje legible.

def fuerza_bruta_cesar():
    # El Cifrado César mueve las letras n posiciones en el alfabeto
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    mensaje_cifrado = input("Ingrese el mensaje cifrado: ").upper()
    
    print("\nProbando todas las posibles claves...")
    
    # Probar claves del 0 al 25
    for clave in range(26):
        mensaje_descifrado = ""
        
        for letra in mensaje_cifrado:
            if letra in alfabeto:
                # Encontrar la posición actual de la letra
                posicion_actual = alfabeto.find(letra)
                # Restar la clave para descifrar (y usar módulo 26 para dar la vuelta al alfabeto si es necesario)
                nueva_posicion = (posicion_actual - clave) % 26
                mensaje_descifrado += alfabeto[nueva_posicion]
            else:
                # Mantener espacios y otros caracteres sin cambios
                mensaje_descifrado += letra
                
        print(f"Clave {clave:2d}: {mensaje_descifrado}")

if __name__ == "__main__":
    fuerza_bruta_cesar()
