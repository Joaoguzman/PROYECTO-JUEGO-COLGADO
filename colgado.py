import random

colgadito = ["puma", "chinchilla", "pudu", "huemul", "condor", "güiña", "guanaco", "ranita de Darwin", "monito del monte", "pingüino de Humbolt"]


#animal = random.choice(colgadito)

#print(animal)

def obtener_palabra_aleatoria(listado):
    animal = random.choice(listado)
    return animal

#print(obtener_palabra_aleatoria(colgadito))

palabra_aleatoria = obtener_palabra_aleatoria(colgadito)

for letra in range(len(palabra_aleatoria)):

    if palabra_aleatoria[letra]== 'n':
        print("_", end= ' ')
    else:
        print(palabra_aleatoria[letra], end = ' ')