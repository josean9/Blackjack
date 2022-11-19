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
    return "Cuyo valor es:", (valor1 + valor2)

print(pedir_carta())
"""print(coger_cartas())"""
"""choice(cartas)
sample(cartas, 5) """