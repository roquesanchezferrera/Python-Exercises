# Python-Exercises
Ejercicios básicos de programación en python.

# Requerimientos:
- Python 3.11.5

# Librerías utilizadas:
- random (Ejercicios 3 y 5)
  
# Ejercicio 1

Crea un programa que solicite al usuario introducir un número entero positivo y lo almacene en una variable. Si lo introducido por el usuario:

a) No es un número se deberá mostrar por pantalla un mensaje de error que le informe de que lo introducido no es un número. Tras ello, el programa deberá volver a solicitarle que introduzca un número entero positivo.

b) No es un número entero se deberá mostrar por pantalla un mensaje de error que le informe de que lo introducido no es un número entero. Tras ello, el programa deberá volver a solicitarle que introduzca un número entero positivo.

c) No es un número entero positivo se deberá mostrar por pantalla un mensaje de error que le informe de que lo introducido no es un número entero positivo. Tras ello, el programa deberá volver a solicitarle que introduzca un número entero positivo.

d) Es un número entero positivo deberás crear una función que lo reciba y compruebe si el número es primo o no. La función deberá devolver un mensaje que informe al usuario del resultado.

# Ejercicio 2

![image](https://github.com/roquesanchezferrera/Python-Exercises/assets/148702288/25161685-49f9-465a-b816-2064620a5089)

Con los datos mostrados en la tabla anterior crea un programa que:

◼ Muestre por pantalla cuántos alumnos suspendieron cada asignatura.

◼ Realiza la media de las notas de cada alumno y muéstralas por pantalla.

◼ Muestra por pantalla los nombres de los alumnos que han aprobado el curso, sabiendo que para aprobar necesitan obtener una nota media igual o superior a 5.

# Ejercicio 3

Crea un programa que simule una partida de dados entre dos amigos, siendo las normas del juego las siguientes:

◼ Cada jugador lanzará dos dados de 6 simultáneamente y apuntará los resultados obtenidos. 

◼ Si alguno de los números obtenidos por los jugadores coincide, el Jugador1 ganará la ronda. Por el contrario, si ninguno de los números coincide ganará el Jugador2.

◼ El juego finalizará cuando alguno de los jugadores gane 3 rondas. 

El programa deberá enviar un mensaje de enhorabuena al jugador que haya ganado la partida y preguntar si se desea jugar otra. Si el usuario responde NO, el programa finalizará, en caso de que responda SI, el programa se repetirá y en caso de que escriba algo diferente, se le deberá indicar que no se ha entendido correctamente su respuesta y se le solicitará repetirla.

# Ejercicio 4

Crea una clase llamada PERSONA con las siguientes propiedades: nombre, apellido, nacionalidad y una función que se llame saludar que muestre un saludo por pantalla. Después crearás una clase llamada ITALIANO, subclase de PERSONA, que tendrá como propiedad: idioma principal cuyo valor estará ya definido y será italiano. Además, la clase ITALIANO establecerá que el valor de la nacionalidad 
(propiedad que hereda de la clase PERSONA) estará ya definido y será siempre: italiana. Por último, la clase incorporará un método llamado saludar que mostrará por pantalla un saludo similar a: “Bonjorno! Mi nombre es: .........., soy de nacionalidad italiana y mi idioma principal es italiano.”

Tras la creación de las dos clases, deberás crear un programa que: 

◼ Solicite al usuario los datos necesarios para crear un objeto de la clase Italiano. Recuerda que el idioma y la nacionalidad ya tienen valores definidos por lo que no se le deberían preguntar al usuario.

◼ El programa deberá contener un método que reciba los datos introducidos por el usuario para crear con ellos un objeto/instancia de la clase italiano. 

◼ Por último, se deberá mostrar por pantalla el mensaje del saludo, llamando a la función saludar desde el objeto de la clase ITALIANO que se ha creado.

# Ejercicio 5

Para este programa deberás definir una tupla compuesta por 15 números enteros positivos aleatorios entre 0 y 100, estos números serán los ganadores del último sorteo de la lotería. Tras ello, el programa solicitará al usuario que introduzca un número entero positivo. El programa deberá comprobar que lo introducido por el usuario es un número entero positivo de igual forma que se realizó en el ejercicio 1, el programa no podrá continuar hasta que el dato introducido cumpla los requisitos, es decir, sea un número entero positivo. Una vez que el dato introducido sea correcto, el programa mostrará por pantalla la lista de números ganadores del sorteo e informará del número ganador más pequeño y del número ganador más grande. Después, el programa comprobará si el número indicado por el usuario, es decir, aquel con el que ha participado en el sorteo, se encuentra entre los ganadores (es decir, en la tupla).

Si el número indicado por el usuario aparece en la lista de números ganadores el usuario habrá ganado 15€. Si el número se ha repetido varias veces, por cada repetición se le sumarán 5€ extra. El programa deberá informar al usuario del resultado y después finalizará. Ejemplo: Si el usuario introduce el 7 y este sólo aparece una vez el usuario habrá ganado 15€. Por el contrario, si el 7 apareciese dos veces, habría ganado 15€ por aparecer en la lista y 5€ extra por la repetición, total 20€.

Si el número no aparece en la lista de números ganadores se le deberá preguntar al usuario si dispone de otro número. Si el usuario responde SI entonces el programa se repetirá, si el usuario responde NO el programa finalizará, si el usuario responde algo diferente, se le pedirá que repita de nuevo su respuesta.

# Ejercicio 6

Para este programa deberás crear una agenda en la que un usuario pueda almacenar sus contactos. La agenda será un diccionario cuya clave será el nombre de los contactos y cuyo valor serán sus teléfonos. En la agenda no se podrán guardar nombres repetidos. En caso de que el usuario intenté introducir un nombre que ya exista en la agenda se le deberá indicar que no es posible y que por favor, vuelva a intentarlo. Tras introducir cada contacto se le deberá preguntar al usuario si desea continuar o salir del programa. Si la respuesta del usuario no es clara el programa deberá pedirle que repita su respuesta. Cuando el usuario desee salir, se le mostrará la agenda y el programa finalizará.





