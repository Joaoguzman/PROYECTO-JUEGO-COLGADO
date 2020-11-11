import random

colgadito = ["puma", "chinchilla", "pudu", "huemul", "condor", "güiña", "guanaco", "ranita de Darwin", "monito del monte", "pingüino de Humbolt"]


#animal = random.choice(colgadito)

#print(animal)

def obtener_palabra_aleatoria(listado):
    animal = random.choice(listado)
    return animal

#print(obtener_palabra_aleatoria(colgadito))

palabra_aleatoria = obtener_palabra_aleatoria(colgadito)

lista_palabra = []

for letra in palabra_aleatoria:
    lista_palabra.append("_")

print("Lista_palabra", lista_palabra)
print("Lista_palabra", palabra_aleatoria)

"""
for letra in range(len(palabra_aleatoria)):
    if palabra_aleatoria[letra]:
        print("_", end= ' ')
    else:
        print(palabra_aleatoria[letra], end = ' ')
"""
contador = 0
while True:
    letra = input("Ingrese una Letra: ")

    if letra in palabra_aleatoria:
        for i in range(len(palabra_aleatoria)):
            if palabra_aleatoria[i] == letra:
                lista_palabra[i] = letra
    print(lista_palabra)
    contador +=1

    if contador == len(palabra_aleatoria):
        print("Todas las letras adivinadas")
        break





'''
while True:
        l = input("Ingrese una Letra")
        if l in palabra_aleatoria:
            for x in palabra_aleatoria:
                if x == l:
                    print(l, end=' ')
                else:
                    print("_", end=' ')
'''