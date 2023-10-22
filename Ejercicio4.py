# Creamos la clase PERSONA
class PERSONA():
    # Definimos el constructor de PERSONA
    def __init__(self, nombre, apellido, nacionalidad):
        # Inicializamos atributos propios
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    # Definimos un método  de PERSONA llamado saludar que muestra un saludo por pantalla
    def saludar():
        print("Hola!!!")

# Creamos la clase ITALIANO que hereda de la clase PERSONA ---- ITALIANO(PERSONA)
class ITALIANO(PERSONA):
    # Definimos el constructor de ITALIANO
    def __init__(self, nombre, apellido):
        # Inicializamos los atributos heredados llamando al constructor de PERSONA
        PERSONA.__init__(self, nombre, apellido, "italiana")

        # Inicializamos atributos propios
        self.idioma = "italiano"

    # Definimos el método saludar que recibe como argumento self y que muestra un saludo por 
    # pantalla con los distintos datos
    def saludar(self):
        print(f"Bonjorno! Mi nombre es {self.nombre} {self.apellido}, soy de nacionalidad {self.nacionalidad} y mi idioma principal es {self.idioma}")

# Mostramos el saludo de la clase PERSONA
PERSONA.saludar()

# Pedimos los datos al usuario
nombre = input("Nombre del usuario: ")
apellido = input("Apellidos del usuario: ")

# Creamos el objeto persona
persona = ITALIANO(nombre, apellido)

# Mostramos el saludo
persona.saludar()
