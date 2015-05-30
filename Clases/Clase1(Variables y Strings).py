#Esta es la primera clase de python
#Los leguajes de programacion manejan varios tipos de datos algunos son: String(cadenas de texo), enteros o int(numeros, operaciones matematicas), reales(numeros decimales)y booleans(falso/verdadero)
#En esta clase vamos a empezar con los strings
#primero tienen que saber que el codigo se lee de arriba para abajo osea es secuencial




print("Hola Mundo");
#De esta menera se puede declarar un string escribiendo print(); y adentro del parentesis entre comillas doble la cadena de texto o lo que se quiere escribit
#Si le dan "run" esto deberia mostrar en la pantalla Hola mundo, si el print(); no tiene paraentesis o no esta entre comillas esto va a dar un error y el codigo no va a funcionar





#Otro concepto muy importate en la programacion son las variables, las variables son espacios en la memoria en donde se pueden alamacenar datos, a esta variable se le tiene que asignar un nombre para poder usarla




saludo="Hola!";
#Aqui se muestra como se hace una variable que se llama saludo y su valor es Hola! el nombre de una variable no puede empezar con un numero
#Recordar que la variable saludo es de tipo string(texto) y para esto al declararse tiene que estar entre comillas " "
#Las variables pueden cambiar de valor(Ver mas en la seccion de re-declaracion de variables)





print(saludo);
#al hacer esto lo que estamos haciendo es imprimir el valor de la variable saludo, saludo no esta entre comillas porque es una variable no un string(texto)




#Existe varias formas de organizar el codigo una de las maneras es comentando(que es lo que estas leyendo) un comentario como dice el nombre es un comentario de aclaracion para los que leen tus codigos
#Los comentarios no son leidos por python osea no es obligatorio un comentario se puede declarar escribiendo un numeral y lo demas es un comentario

#Concatenacion
#la conactenacion es unir dos valores que pueden ser un string y una variable o dos variables


print (saludo + " Mundo?");

#Aqui se muestra la union de una variable y un string

despedida ="Adios";
print(saludo+" "+despedida);
#Union de dos variables -Aclaracion el +" "+ es la union de una variable un espacio y otra variable esto se usa para imprimir un espacio en blanco si esto no se hace, se imprimira hola!adios




#Re-Declaracion de variables



saludo = "HOLA";
saludo = "Adios";
print(saludo);

#Como el codigo se lee de arriba para abajo el valor de saludo es adios


#Un error que puede pasar en python es esto

#print(bienvenido);
#bienvanido="Adios";


#Como el codigo se lee de arriba para abajo la funcion print va a buscar despedida arriba de el pero como no existe va a dar un error de bienvenido not defined
#Para evitar esto se debe declarar la variable antes de usarla en este caso usar print
bienvenido="Hola bienvenido";
print(bienvenido);



#Input(Borrar el numeral para proabar)
#el input es una funcion que hace que lo que se escriba su valor sea asignado a una variable en el caso mas abajo lo que escribamos se va almacenar en la variable nombre(Probar primero)

nombre = input("Cual es tu nombre? ");
print("Bienvenido "+nombre);