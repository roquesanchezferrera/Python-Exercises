# Importamos el módulo random para generar números pseudoaleatorios
import random

def numeros_sorteo():
    ''' Función para generar los 15 números premiados del sorteo. Devolverá una tupla formada por los números ganadores'''
    # Creamos una lista vacía donde iremos guardando los números premiados
    lista = []
    while (len(lista) <= 14): # Mientras que la longitud de la lista sea menor o igual que 14, vamos añadiendo números
        lista.append(random.randint(0, 100)) # Número aleatorio entre 0 y 100 (ambos inclusive)

    return tuple(lista) # Pasamos la lista a tupla con la función tuple()

def validar_numero():  
    '''Función para comprobar si el dato introducido por el usuario es un número entero y positivo. No recibe ningún argumento y devuelve un número entero y positivo''' 
    
    while True: 
        '''Se realiza un bucle while para pedir un número al usuario y comprobar si se trata de un número entero y positivo. En el caso de que no se cumpla
        alguna condición, se vuelve a repetir el bucle y por tanto se le vuelva a pedir otro número al usuario. En el caso de que cumpla todas las condiciones
        se sale del bucle'''

        numero = input("Introduzca un número entero positivo: ") # Introducimos un número por el terminal y lo guardamos en la variable "numero"

        try: 
            numero = int(numero) # Intentamos convetir el número en un entero "int"

        except ValueError: # Se genera una excepción en el caso de que el número introducido no sea un número ó sea decimal 
                try: 
                     numero = float(numero) # Intentamos convertir el número en un float
                    
                except ValueError: # Se genera una excepción en el caso de que no sea un número el dato el introducido
                    print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
                
                else: # En el caso de no generarse una excepción, querrá decir que el número es decimal
                    print("No ha introducido un número entero. Por favor, vuelva a intentarlo.")

        else: # En el caso de que sea un número entero (no se ha generado ninguna excepción) se debe comprobar si es positivo
            if (numero <= 0):
                print("No ha introducido un número entero positivo. Por favor vuelva a intentarlo.") # Si es menor o igual a 0, el número introducido es erróneo
                
            else:
                break # En el caso de que sea mayor de cero. El número habrá cumplido las condiciones de ser un número, entero y positivo y se sale del bucle while con la sentencia break
    
    return numero # Se devuelve un número entero y positivo

# Llamamos a la función numeros_sorteo() para generar los números premiados y la tupla devuelta la guardamos en numeros_ganadores
numeros_ganadores = numeros_sorteo()

# Con la función validar_numero() pedimos al usuario un número entero y positivo
numero_usuario = validar_numero()

# Mostramos los números ganadores y el número ganador más grande (max()) y más pequeño (min())
print("La lista de números ganadores del sorteo es: ", end = "")
print(*numeros_ganadores, sep = ", ")
print(f"El número ganador más pequeño es el {min(numeros_ganadores)}")
print(f"El número ganador más grande es el {max(numeros_ganadores)}")

# Declaramos la variable condicion inicializada con True que determinará la continuidad del bucle
condicion = True
while condicion == True:
    if (numero_usuario in numeros_ganadores):
        # Si el número introducido por el usuario está entre los números ganadores, vemos si se repite más de una vez para aumentar el premio ganado
        veces_repetido = numeros_ganadores.count(numero_usuario) # Con la función count determinamos cuantas veces se repite un número en la tupla

        if (veces_repetido == 1):
            # Si sólo se ha repetido una vez el premio es de 15€
            print(f"¡Felicidades! Su número {numero_usuario} se encuentra dentro de la lista de ganadores. Ha ganado un total de 15€")
        else:
            # Si se ha repetido más de una vez, se debe calcular el premio total.
            print(f"¡Felicidades! Su número {numero_usuario} se encuentra dentro de la lista de ganadores y además se ha repetido {veces_repetido} veces. Ha ganado un total de {15 + (5 * (veces_repetido - 1))}€")

        condicion = False # Como condicion pasa a valer False, se sale del bucle y termina el programa
    
    else:
        # Si el número introducido no está entre los premiados, le preguntamos si desea intentarlo otra vez
        while True:
            respuesta = input("Lo sentimos. Su número no ha resultado premiado. ¿Desea volver a intentarlo?: ")

            if (respuesta == "SI"):
                # Si desea repetir otra vez se le vuelve a pedir un número con la función validar_numero() y se sale de este bucle interno para volver a ver si se 
                # encuentra en la lista de los numeros_ganadores
                numero_usuario = validar_numero()
                break

            elif (respuesta == "NO"):
                # Si la respuesta es NO, condicion pasa a valer False (se puede salir del bucle principal) y con break salimos de este bucle interno
                condicion = False
                break
            
            else:
                # En el caso de que la respuesta no sea ni SI ni NO, le pedimos que repita
                print("No hemos logrado entender su respuesta. Repítala, por favor.")
