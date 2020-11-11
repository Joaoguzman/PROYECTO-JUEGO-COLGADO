import random

colgadito = ["puma", "chinchilla", "pudu", "huemul", "condor", "güiña", "guanaco", "ranita de Darwin", "monito del monte", "pingüino de Humbolt"]

figura = ['''
+++++
    |
    |
    |
====''', '''
+++++
 O  |
    |
    |
====''', '''
+++++
 O  |
 |  |
    |
====''', '''
+++++
 O  |
/|  |
    |
====''', '''
+++++
 O  |
/|\ |
    |
====''', '''
+++++
 O  |
/|\ |
/   |
====''', '''
+++++
 O  |
/|\ |
/ \ |
====''']


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
'''
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
lista_palabra = []
for letra in palabra_aleatoria:
        lista_palabra.append("_")
def actualiza_tablero(letra_adivinada, palabra_secreta):
    if letra_adivinada in palabra_secreta:
        for letra in range(len(palabra_secreta)):
            if palabra_secreta[letra] == letra_adivinada:
                lista_palabra[letra] = letra_adivinada
    print(lista_palabra)        

#Actualización de tablero 
#El programa tiene 7 intentos
contador = 1
contador_personaje = 0

while True:
    print(figura[contador_personaje])
    letra = input("Ingresa una letra: ")
    if letra in palabra_aleatoria:
        actualiza_tablero(letra, palabra_aleatoria)
        contador += 1
    else:
        print("No está la letra en la palabra")
        contador_personaje += 1
        if contador_personaje == 6:
            print("Perdiste! Lo has ahorcado. Vuelve a intentarlo!")
            break
        elif contador == len(palabra_aleatoria):
            print("Ganaste! Lo salvaste")
            break
            

