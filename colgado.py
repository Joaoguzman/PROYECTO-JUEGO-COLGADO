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


def obtener_palabra_aleatoria(listado):
    animal = random.choice(listado)
    return animal



palabra_aleatoria = obtener_palabra_aleatoria(colgadito)

lista_palabra = []
for letra in palabra_aleatoria:
        lista_palabra.append("_")

def actualiza_tablero(letra_adivinada, palabra_secreta):
    adivinadas = 0
    if letra_adivinada in palabra_secreta:
        for letra in range(len(palabra_secreta)):
            if palabra_secreta[letra] == letra_adivinada:
                lista_palabra[letra] = letra_adivinada
                adivinadas += 1

            #retornar letras adivinadas
    print(lista_palabra)
    return adivinadas  

#Actualización de tablero 
#El programa tiene 7 intentos
contador = 0
contador_personaje = 0

while True:
    print(figura[contador_personaje])
    letra = input("Ingresa una letra: ")
    if letra in palabra_aleatoria:
        letras_adivinadas = actualiza_tablero(letra, palabra_aleatoria)
        contador += letras_adivinadas
        print("Letras adivinadas: ",contador)
        print("Nº letras palabra: ", len(palabra_aleatoria))
        if contador == len(palabra_aleatoria):
            print("Ganaste! Lo salvaste")
            break
    else:
        print("No está la letra en la palabra")
        contador_personaje += 1
        if contador_personaje == 6:
            print("Perdiste! Lo has ahorcado. Vuelve a intentarlo!")
            break
            
            

