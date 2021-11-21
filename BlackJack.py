#Para empezar con la tarea, emezaremos creando una librería "cartas", donde se van a definir las cartas con las que jugaremos al BlackJack

#di viene en corchetes, lista, si viene entre llaves, es un diccionario. El diccionario,te relaciona un valor con un numero, como las cartas del programa, y la lista solo el valor

from random import choice, sample   #choice elige dos cartas, y sample es la q se encarga de mostrarte las carts(caractéres,elememntos...)
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
print(chr(0x1f0a1))
print(chr(0x1f0a2))

#En el joinkeys, relacionamos los valores con las cartas con el dibujo(primer print) -1
#En el list cartas, hacemos una lista con los valores de las cartas(segundo print) -2

#En este print con el for, llevaremso a cabo la relacion de la carta con el valor, con el item, para que nos salga de uno en uno, no la lista entera, y con el format...
#...  y los valores en el item, van del 0 hasta el numero de de valores que tengas, es decir, el valor 0 vale 11, el valor 1 vale 2, el for recorre toda la lista...
#... el format, es darle cuerpo a la llave, que está definido en el primer print  (tercer print)  -3

#itineracion ordenada, que cada carta , coja el mismo numero siempre, y estas las ordenas, por ejemplo estas est,an ordenadas de menor a mayor(cuarto print) -4

#Ahora creamos una lista del diccionario -5

#choice- para seleccionar una carta de la lista de cartas
#score, miras el valor de la carta que has elegido de la lista de carta
#otro choice, eligo otra carta
#segundo score, se va aculumando el valor de las cartas,si el valor de la primera es 5, y la segunda es 6, el valor de la segunda es 11, solo se sacan 2 cartas en este juego
#(print 6) -6

# hacer sample, barajar las cartas
# esta es la parte de la banca

