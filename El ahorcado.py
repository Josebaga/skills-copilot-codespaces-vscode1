import string
import random

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_válida(palabras):
    #Seleccionar una palabra al azar de la lista de palabras valida
    palabra = random.choice (palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice (palabras)

    return palabra.upper()



def Ahorcado():

    print("==============================")
    print("==========Ahorcado============")
    print("==============================")

    palabra = obtener_palabra_válida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() #vacio, para que no se cree un diccionario sino un conjunto(no se pueden repetir las letras)
    abecedario = set(string.ascii_uppercase) #no contiene la Ñ

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
      #Letras adivinadas
      #" ".join({"a", "b", "c"}) -> "a b c"
        print (f"Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}")
        #H-LA
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {" ".join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        #Si la letra escogida por el usuario está en el abecedario y no está en el conjunto de letras que ya se han ingresado,se añade la letra al conjunto de letras ingresado
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            #Si la letra está en la palabra, quitar la letra del conjunto de letraspendientes de adivinar. Si no está en la palabra quitar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(" ")
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        #Si la letra escogida por el usuario ya fué ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esta letra. Por favor escoge una letra nueva")
        else:
            print("Esta letra no es válida.")

#El juego llega a esta linea cuando se adivinan todas las letras o cuando se agotan las vidas.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")

    else:
        print(f"¡Bravo! ¡Adivinaste la palabra! {palabra}")

Ahorcado()







