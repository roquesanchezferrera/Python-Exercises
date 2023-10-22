# Creamos un diccionario donde iremos guardando el nombre del contacto como clave y el número de telefono como valor
agenda = {}

# Declaramos la variable condición que determinará la continuidad del bucle
condicion = True

while condicion == True:
    # Pedimos al usuario que introduzca el nombre del contacto
    nombre = input("Introduzca en nombre del contacto: ")

    if (nombre not in agenda):
        # Si el nombre no está previamente guardado en la agenda, se le pide el número de teléfono
        telefono = input("Introduzca su número de teléfono: ")

        # Guardamos ambos datos en la agenda con la función update()
        agenda.update({nombre: telefono})

        # Cremos un bucle para preguntarle al usuario si desea seguir añadiendo contactos
        while True:
            respuesta = input("¿Desea continuar o salir del programa?: ")

            if (respuesta == "continuar"):
                # Si su respuesta es 'continuar', con la sentencia break salimos de este bucle interno
                break

            elif (respuesta == "salir"):
                # Si la respuesta es 'salir', condicion pasa a valer False (saldriamos del bucle principal) y con
                # la sentencia break salimos del bucle interno
                condicion = False
                break

            else:
                # En el caso de que la respuesta sea distinta, se pide volver a repetirla
                print("No logramos entender su respuesta. Vuelva a intentarlo.")

    else:
        # En el caso de que el contacto ya exista, se muestra el mensaje de error
        print("Este contacto ya existe en la agenda por lo que no es posible añadirlo. Vuelva a intentarlo.")

# Mostramos el contenido de la agenda
print(f"Agenda: {agenda}")
