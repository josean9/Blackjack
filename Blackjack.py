from random import choice, sample, shuffle 
import random
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
for carta,valor in cartas.items():
    print("A la carta {}, se le atribuye el valor {}".format(carta, valor))
listaDeCartas = list(cartas.keys()) 
print("La lista de cartas es: {}".format(listaDeCartas))   
def pedir_carta():
    eleccion1 = random.randint(1, 13)
    eleccion2 = random.randint(1, 13)
    while eleccion1 == eleccion2:
        eleccion2 = random.randint(1, 13)
    else:
        pass
    carta1 = list(cartas.keys())[eleccion1]
    valor1 = list(cartas.values())[eleccion1]
    carta2 = list(cartas.keys())[eleccion2]
    valor2 = list(cartas.values())[eleccion2]
    print(carta1, valor1)
    print("Sus dos cartas son",carta1, carta2)
    print(cartas)
    return "Cuyo valor es:", (valor1 + valor2)
def carta_crupier():
    carta3 = listaDeCartas[2]
    valor3 = cartas[carta3]
    carta4 = listaDeCartas[3]
    valor4 = cartas[carta4]
    return carta3, carta4,"cuyo valor es:", (valor3 + valor4)
def pedir_carta2():
    carta1 = listaDeCartas[0]
    valor1 = cartas[carta1]
    carta2 = listaDeCartas[1]
    valor2 = cartas[carta2]
    return carta1, carta2,"cuyo valor es:", (valor1 + valor2)
def pedir_tercera_carta():
    carta1 = listaDeCartas[0]
    valor1 = cartas[carta1]
    carta2 = listaDeCartas[1]
    valor2 = cartas[carta2]
    carta3 = listaDeCartas[4]
    valor3 = cartas[carta3]
    return carta1, carta2, carta3,"cuyo valor es:", (valor1 + valor2 + valor3)
def juego():
    print("Bienvenido al juego de Blackjack")
    print("¿Quieres jugar?")
    print("1. Si")
    print("2. No")
    eleccion = input("Elige una opción: ")
    try:
        eleccion = int(eleccion)
    except ValueError:
        print("No has introducido un número")
        juego()
    if eleccion == 1:
        shuffle(listaDeCartas)
        print("Las dos cartas del crupier son",carta_crupier())
        print("Sus dos cartas son",pedir_carta2())
        print("¿Quieres otra carta?")
        print("1. Si")
        print("2. No")
        eleccion2 = int(input("Elige una opción: "))
        if eleccion2 == 1:
            print("Sus dos cartas son",pedir_tercera_carta())
        else:
            pass
    else:
        pass
print(juego())
"""print(coger_cartas())"""
"""choice(cartas)
sample(cartas, 5) """