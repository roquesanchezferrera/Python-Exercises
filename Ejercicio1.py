def comprobar_primo(dato):
    '''Función para comprobar si un número es primo o no. Recibe como argumento la variable dato (se trata de un número entero y positivo)
       y devuelve un mensaje de texto para mostrar por pantalla'''
    
    if (dato < 2): # Si "dato" es menor de "2", el número no es primo
        return f"El número {dato} no es primo"
    
    for i in range(2, dato): # Recorremos un bucle desde "2" hasta "dato - 1"
        if (dato % i == 0): # Si desde "2" hasta "dato - 1" alguna división entre "dato" e "i" ha tenido como resto un cero, querrá decir que no es sólo divisible por "1" o "dato". Por tanto no es primo
            return f"El número {dato} no es primo"
    
    return f"El número {dato} es primo" # En el caso de que no se haya encontrado ningún número cuya división tenga como resto "0", el número es primo

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

print(comprobar_primo(validar_numero())) # Llamamos a la función comprobar_numero y le pasamos como argumento la función validar_numero() que devulve un entero positivo. Lo que devuelve comprobar_primo() se muestra por pantalla