# Importamos el módulo random para generar números pseudoaleatorios
import random

def numeros_aleatorios():
    ''' Función para generar números pseudoaleatorios. No recibe ningún argumento y devuelve una tupla 
        con los dos números generados entre el 1 y el 6 (ambos inclusive)'''
    return (random.randint(1, 6), random.randint(1, 6))

def comprobar_ganador(tupla1, tupla2):
    ''' Función para comprobar que número es el ganador de la ronda. Recibe cómo argumento dos tuplas formadas por dos elementos cada una.
        Devuelve qué jugador ha sido el ganador de la ronda'''
    for numero in tupla1: # Recorremos la tupla 1
        if(numero in tupla2): 
            # Si algún número de la tupla 1 se encuentra repetido en la tupla 2, el ganador será el jugador 1
            return "Jugador 1"

    if (tupla1[0] == tupla1[1] or tupla2[0] == tupla2[1]):
        # Si en la tupla 1 o en la tupla 2 se repite el mismo número, también gana el jugador 1
        return "Jugador 1"
    
    else:
        return "Jugador 2" # En el caso de no se haya cumplido ninguna condición, gana el jugador 2

# Declaramos variables para contabilizar las partidas ganadas de cada jugador
ganadas_j1, ganadas_j2 = 0, 0

# La variable condicion se ha creado para determinar la continuidad del bucle. Inicializada con el valor True
condicion = True

while condicion == True: # Mientras que condicion = True, se ejecturará el siguiente bucle

    # Primero determinamos los resultados obtenidos al lanzar los dados para cada jugador. Para
    # ello llamamos a la función numeros_aleatorios que genera una tupla con dos valores
    jugador1 = numeros_aleatorios()
    jugador2 = numeros_aleatorios()

    # Mostramos los resultados obtenidos
    print("Jugador 1 ha obtenido: ", end = "")
    print(*jugador1, sep = " y ")

    print("Jugador 2 ha obtenido: ", end = "")
    print(*jugador2, sep = " y ")

    # Llamamos a la función comprobar_ganador que determina quién ha ganado la ronda y lo mostramos por pantalla
    ganador = comprobar_ganador(jugador1, jugador2)
    print("Ganaría la ronda:", ganador)

    # Dependiendo de quien haya ganado la ronda, se incrementa en uno la variable ganadas_jx
    if (ganador == "Jugador 1"):
        ganadas_j1 += 1
    else:
        ganadas_j2 += 1

    # En el momento en el que uno de los tres jugadores llegue a 3 rondas ganadas, se muestra quien es el ganador
    if (ganadas_j1 == 3 or ganadas_j2 == 3):
        print(f"Enhorabuena {ganador}, has ganado la partida.")
        ganadas_j1 = 0 # La partida ha terminado por lo que ponemos a cero los contadores de victorias
        ganadas_j2 = 0

        # Cuando se ha terminado la partida, procedemos a preguntar si desea jugar otra.
        while True:
            respuesta = input("¿Desea jugar otra partida?: ")

            if (respuesta == "NO"):
                # Si la respuesta es que no, condicion pasa a valer false, por lo que se sale del bucle principal, y con 
                # break se sale del bucle interno
                condicion = False
                break

            elif (respuesta == "SI"):
                # Si la respuesta es que si, se sale sólo del bucle interno para repetir otra partida
                break

            else:
                # En el caso de que la respuesta no sea ni SI ni NO, no se sale del bucle y se vuelve repetir la 
                # pregunta
                print("No se ha entendido correctamente su respuesta. Vuelva a intentarlo.")

print("Programa finalizado con éxito.")

