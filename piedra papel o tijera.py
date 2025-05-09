import random

def jugar():

    print("============================================")
    print("==========Piedra, papel o tijera============")
    print("============================================")

    usuario = input("Escoge una opción : 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    ordenador = random.choice(['pi', 'pa', 'ti'])

    if usuario == ordenador:
        return '¡Empate!'
    
    if ganó_el_jugador(usuario, ordenador):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    #retornar TRUE si gana el jugador.
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())

                               
                               
    