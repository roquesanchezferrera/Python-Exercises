# Establecemos los datos de la tabla. Para cada alumno se ha creado un diccionario con las asignaturas y notas
alumno1 = {"Latín": 8, "Castellano": 8, "Francés": 9, "Inglés": 4}
alumno2 = {"Latín": 7, "Castellano": 6, "Francés": 9, "Inglés": 2}
alumno3 = {"Latín": 10, "Castellano": 7, "Francés": 8, "Inglés": 9}
alumno4 = {"Latín": 4, "Castellano": 4, "Francés": 3, "Inglés": 2}
alumno5 = {"Latín": 9, "Castellano": 8, "Francés": 9, "Inglés": 6}

# Establacemos una lista donde guardamos los diferentes dicciconarios
alumnos = [alumno1, alumno2, alumno3, alumno4, alumno5]

# Lista donde se guardan los alumnos aprobados
alumnosAprobados = []

# Declaramos variables para contabilizar la cantidad de alumnos suspensos por asignatura
suspensosLatin = 0
suspensosCastellano = 0
suspensosFrances = 0
suspensosIngles = 0

for alumno in alumnos: #Recorremos la lista alumnos
    # Para cada alumno, comprobamos si el valor de la clave es menor de 5. En ese caso significará suspenso y 
    # se incrementará en uno la variable correspondiente a la asignatura
    if (alumno["Latín"] < 5):
        suspensosLatin += 1

    if (alumno["Castellano"] < 5):
        suspensosCastellano += 1

    if (alumno["Francés"] < 5):
        suspensosFrances += 1
    
    if (alumno["Inglés"] < 5):
        suspensosIngles += 1

# Una vez contabilizados los suspensos, se muestran por pantalla
print(f"Latín se ha suspendido por {suspensosLatin} alumnos.")
print(f"Castellano se ha suspendido por {suspensosCastellano} alumnos.")
print(f"Francés se ha suspendido por {suspensosFrances} alumnos.")
print(f"Inglés se ha suspendido por {suspensosIngles} alumnos.")

for alumno in alumnos: # Se vuelve a recorrer la lista alumnos pero en este caso para realizar el cálculo de la nota media
    nota_media = (alumno["Latín"] + alumno["Castellano"] + alumno["Francés"] + alumno["Inglés"]) / 4

    # Dependiendo de que alumno sea, se mostrará su nota media por pantalla. En el caso de que ese alumno esté aprobado, se añadirá a la lista alumnosAprobados
    if (alumno == alumno1):
        print(f"El alumno1 ha tenido una nota media de {nota_media}.")

        if(nota_media >= 5):
            alumnosAprobados.append("Alumno1")

    elif (alumno == alumno2):
        print(f"El alumno2 ha tenido una nota media de {nota_media}.")

        if(nota_media >= 5):
            alumnosAprobados.append("Alumno2")

    elif (alumno == alumno3):
        print(f"El alumno3 ha tenido una nota media de {nota_media}.")

        if(nota_media >= 5):
            alumnosAprobados.append("Alumno3")

    elif (alumno == alumno4):
        print(f"El alumno4 ha tenido una nota media de {nota_media}.")

        if(nota_media >= 5):
            alumnosAprobados.append("Alumno4")

    elif (alumno == alumno5):
        print(f"El alumno5 ha tenido una nota media de {nota_media}.")

        if(nota_media >= 5):
            alumnosAprobados.append("Alumno5")

# Mostramos el contenido de la lista alumnosAprobados
print("Los alumnos que han aprobado el curso son:", end = " ")
print(*alumnosAprobados, sep = ", ")