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
valorTotalCrupier = 0
valorTotalMio = 0
for carta,valor in cartas.items():
    print("A la carta {}, se le atribuye el valor {}".format(carta, valor))
listaDeCartas = list(cartas.keys()) 
print("La lista de cartas es: {}".format(listaDeCartas))   
def carta_crupier():
    carta3 = listaDeCartas[2]
    valor3 = cartas[carta3]
    carta4 = listaDeCartas[3]
    valor4 = cartas[carta4]
    global valorTotalCrupier
    valorTotalCrupier = valor3 + valor4
    return carta3, carta4,"cuyo valor es:", (valorTotalCrupier)
def pedir_carta2():
    """"eleccion1 = input("Elige una opción: ")
    try:
        eleccion1 = int(eleccion1)
    except:
        print("No has introducido un número")
        pedir_carta2()
    else:
        carta1 = listaDeCartas[eleccion1]
    eleccion2 = input("Elige una opción: ")
    try:
        eleccion2 = int(eleccion2)
    except:
        print("No has introducido un número")
        pedir_carta2()
    else:
        carta2 = listaDeCartas[eleccion2]"""
    carta1 = listaDeCartas[0]
    valor1 = cartas[carta1]
    carta2 = listaDeCartas[1]
    valor2 = cartas[carta2]
    global valorTotalMio
    valorTotalMio = valor1 + valor2
    return carta1, carta2,"cuyo valor es:", (valorTotalMio)
def pedir_tercera_carta():
    carta1 = listaDeCartas[0]
    valor1 = cartas[carta1]
    carta2 = listaDeCartas[1]
    valor2 = cartas[carta2]
    carta3 = listaDeCartas[4]
    valor3 = cartas[carta3]
    global valorConTresCartas
    valorConTresCartas = valor1 + valor2 + valor3
    return carta1, carta2, carta3,"cuyo valor es:", (valorConTresCartas)
def volverAJugar():
    print("¿Quieres volver a jugar?")
    print("1. Si")
    print("2. No")
    eleccion3 = input("Elige una opción: ")
    try:
        eleccion3 = int(eleccion3)
    except:
        print("No has introducido un número")
        volverAJugar()
    if eleccion3 == 1:
        juego()
    elif eleccion3 == 2:
        return "El juego ha terminado"
    else:
        print("Introduzca una opción válida")
        volverAJugar()
def comparacion():
    if valorTotalCrupier > valorTotalMio:
        print("Has perdido")
    elif valorTotalCrupier < valorTotalMio:
        print("Has ganado")
    else:
        print("Empate")
def juego():
    print("Bienvenido al juego de Blackjack")
    print("¿Quieres jugar?")
    print("1. Si")
    print("2. No")
    eleccion = input("Elige una opción: ")
    try:
        eleccion = int(eleccion)
    except:
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
            print("Sus tres cartas son",pedir_tercera_carta())
            comparacion()
        else:
            comparacion()
            print("Quiere volver a jugar?")
            print("1. Si")
            print("2. No")
    elif eleccion == 2:
        return "El juego ha terminado"
    else:
        print("Introduzca una opción válida")
        juego()
print(juego())