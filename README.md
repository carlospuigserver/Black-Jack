# Black-Jack

Dirección de Github para este repositorio: (https://github.com/carlospuigserver/Black-Jack.git)

Para realizar est tarea, la cual es jugar de una forma simplificada al Black Jack, hemos tenido que haber entendido y asimilado lo que es un diccionario, y una lista, sabiendo que en el diccionario, este nos relaciona valores, con números o con cualquier otra forma de datos, mientras que la lista solo se basa en controlar un valor, y este, sin estar relacionado con ningún dato


El diagrama de flujo relacionado con nuestro trabajo es : 





<img width="686" alt="Diagrama de flujo Black Jack" src="https://user-images.githubusercontent.com/91721643/142933937-bfb05ffd-f8e3-4f19-ab43-afee46257fc0.png">







El código del juego del Black Jack es el siguiente:

```#Para empezar con la tarea, emezaremos creando una librería "cartas", donde se van a definir las cartas con las que jugaremos al BlackJack

# El diccionario,te relaciona un valor con cualquier dato, como un número(las cartas del programa), y la lista solo enumera el valor

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



#En el joinkeys, relacionamos los valores con las cartas con el dibujo(primer print)
print("Cartas: {}".format(" ".join(cartas.keys())))

#En el list cartas, hacemos una lista con los valores de las cartas(segundo print)
print("Puntos: {}".format(list(cartas.values())))

#En este print con el for, llevaremso a cabo la relacion de la carta con el valor, con el item, para que nos salga de uno en uno, no la lista entera, y con el format...
#...  y los valores en el item, van del 0 hasta el numero de de valores que tengas, es decir, el valor 0 vale 11, el valor 1 vale 2, el for recorre toda la lista...
#... el format, es darle cuerpo a la llave, que está definido en el primer print  (tercer print)  
print("1\ Itineración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} tiene el valor {}".format(carta,valor))


#itineracion ordenada, que cada carta , coja el mismo numero siempre, y estas las ordenas, por ejemplo estas est,an ordenadas de menor a mayor(cuarto print)
print("2\ Itineración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print(" la carta {} tiene el valor {}". format(carta,cartas[carta])) 

#Ahora creamos una lista del diccionario
print("3\ Black Jack")
listaCartas=list(cartas)

#choice- para seleccionar una carta de la lista de cartas
#score, miras el valor de la carta que has elegido de la lista de carta
#otro choice, eligo otra carta
#segundo score, se va aculumando el valor de las cartas,si el valor de la primera es 5, y la segunda es 6, el valor de la segunda es 11, solo se sacan 2 cartas en este juego
print("Ha seleccionado :", end=" ")
carta=choice(listaCartas)
score=cartas[carta]
print(carta, end =" ")
carta=choice(listaCartas)
score += cartas[carta]
print(carta, end =" ")
print("  >>> su puntuación es de ", score)



# hacer sample, barajar las cartas
# esta es la parte de la banca
main_banca= sample(listaCartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],main_banca[1],score_banca))

