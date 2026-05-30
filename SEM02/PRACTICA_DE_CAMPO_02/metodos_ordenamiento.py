#Cantidad de datos
n = int(input("Ingrese la cantidad de datos: "))

#Lista vacia
datos = []

#Ingreso de datos
for i in range(n):

    dato = int(input("Ingrese dato " + str(i + 1) + ": "))
    datos.append(dato)

print("\nDatos ingresados:")
print(datos)

#Bandera de Bluce
continuar = True

while continuar:
    print("\nMENU DE ORDENACION")
    print("1. Burbuja")
    print("2. Insercion")
    print("3. Seleccion")
    print("4. Quicksort")
    print("5. Mergesort")

    opcion = int(input("Seleccione una opcion: "))

    #Copiar lista original
    lista = datos[:]

    #METODO DE ORDENAMIENTO 01: BURBUJA
    if opcion == 1:

        for i in range(len(lista)-1):
            for j in range(len(lista)-1-i):

                # Comparar vecinos
                if lista[j] > lista[j+1]:

                    # Intercambiar posiciones
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux

        print("\nResultado Burbuja:")
        print(lista)

    #METODO DE ORDENAMIENTO 02: INSERCION
    elif opcion == 2:

        for i in range(1, len(lista)):

            # Elemento a insertar
            actual = lista[i]

            j = i - 1

            # Desplazar elementos mayores
            while j >= 0 and lista[j] > actual:
                lista[j+1] = lista[j]
                j -= 1

            lista[j+1] = actual

        print("\nResultado Insercion:")
        print(lista)

    #METODO DE ORDENAMIENTO 03: SELECCION
    elif opcion == 3:

        for i in range(len(lista)-1):

            # Buscar menor elemento
            menor = i

            for j in range(i+1, len(lista)):

                if lista[j] < lista[menor]:
                    menor = j

            # Intercambiar posiciones
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux

        print("\nResultado Seleccion:")
        print(lista)

    #METODO DE ORDENAMIENTO 04: QUICKSORT
    elif opcion == 4:

        pila = [(0, len(lista)-1)]

        while len(pila) > 0:

            inicio, fin = pila.pop()

            if inicio < fin:

                pivote = lista[fin]
                i = inicio - 1

                for j in range(inicio, fin):

                    if lista[j] <= pivote:

                        i += 1

                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

                aux = lista[i+1]
                lista[i+1] = lista[fin]
                lista[fin] = aux

                posicion = i + 1

                pila.append((inicio, posicion - 1))
                pila.append((posicion + 1, fin))

        print("\nResultado Quicksort:")
        print(lista)

    #METODO DE ORDENAMIENTO 05: MERGESORT
    elif opcion == 5:

        tamaño = 1
        n = len(lista)

        while tamaño < n:

            izquierda = 0

            while izquierda < n:

                medio = min(izquierda + tamaño - 1, n - 1)
                derecha = min(izquierda + 2 * tamaño - 1, n - 1)

                L = lista[izquierda:medio+1]
                R = lista[medio+1:derecha+1]

                i = 0
                j = 0
                k = izquierda

                while i < len(L) and j < len(R):

                    if L[i] <= R[j]:
                        lista[k] = L[i]
                        i += 1
                    else:
                        lista[k] = R[j]
                        j += 1

                    k += 1

                while i < len(L):
                    lista[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    lista[k] = R[j]
                    j += 1
                    k += 1

                izquierda += 2 * tamaño

            tamaño *= 2

        print("\nResultado Mergesort:")
        print(lista)

    else:
        print("Opcion no valida")

    #Control de Bandera
    print("\n¿Desea volver al menu principal o terminar?")
    print("1. Volver al menu")
    print("2. Terminar programa")
        
    respuesta = int(input("Seleccione una opcion: "))
        
    if respuesta == 2:
        print("\n¡Programa terminado con exito!")
        continuar = False