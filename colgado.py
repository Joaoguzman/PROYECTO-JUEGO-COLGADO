import random
#Colgadito es la lista de palabras para jugar
colgadito = ["puma", "chinchilla", "pudu", "huemul", "condor", "güiña", "guanaco"]
#Figura es lo que va mostrando la consecuencia de los errores del jugador
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

#Elige palabra para adivinar
def obtener_palabra_aleatoria(listado):
    animal = random.choice(listado) #Elige una palabra del listado aleatoria
    return animal 

palabra_aleatoria = obtener_palabra_aleatoria(colgadito)#Queda registrado el animal que retornó la función anterior
#Crea lista vacía, que se llama lista_palabra
lista_palabra = []
for letra in palabra_aleatoria: #Agrega los caracteres de la palabra_aleatoria como _  a lista_palabra   
    lista_palabra.append("_")

def actualiza_tablero(letra_adivinada, palabra_secreta):
    adivinadas = 0
    if letra_adivinada in lista_palabra: 
        print("La letra ya fue agregada")
    else:
        if letra_adivinada in palabra_secreta:
            for letra in range(len(palabra_secreta)): #Recorre los caracteres de la palabra_secreta
                if palabra_secreta[letra] == letra_adivinada: #Pregunta si la letra adivinada está en la palabra_secreta
                    lista_palabra[letra] = letra_adivinada #Muestra letra donde corresponde
                    adivinadas += 1 #Contador Letras adivinadas

            #retornar letras adivinadas
    print(lista_palabra) #Mostrando tablero del estado de la palabra
    return adivinadas  

contador_puntaje = 120 #Parámetro para ir descontando de a 20 puntos los errores

def calcula_puntaje(puntaje):
    puntaje -=20
    print("Tienes ", puntaje, " puntos.")
    return puntaje



#Actualización de tablero 
#El programa tiene 6 intentos
contador = 0 #Va manejando cuántas letras tengo adivinadas
contador_personaje = 0 #Va agregando partes al colgado mediante el índice

print(lista_palabra)    
while True:
    print(figura[contador_personaje])
    letra = input("Ingresa una letra: ")
    if letra in palabra_aleatoria:
        letras_adivinadas = actualiza_tablero(letra, palabra_aleatoria)
        contador += letras_adivinadas
        print("Letras adivinadas: ",contador)
        print("Esta palabra tiene ", len(palabra_aleatoria), " letras.")
        print("Tienes ", contador_puntaje, " puntos.")
        if contador == len(palabra_aleatoria):
            print("Ganaste! Lo salvaste")
            break
    else:
        print("No está la letra en la palabra")
        contador_personaje += 1
        contador_puntaje = calcula_puntaje(contador_puntaje)
        if contador_personaje == 6:
            print(figura[contador_personaje])
            print("Perdiste! Lo has ahorcado. Vuelve a intentarlo!")
            break


