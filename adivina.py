import random

def adivina_el_número(x):

    print("Tu meta es adivinar el número generado por el ordenador")

    número_aleatorio = random.randint(1, x) #número aleatrio entre 1 y x.

    predicción = 0

    while predicción != número_aleatorio:
        predicción = int(input(f"Adivina un número entre 1 y {x}: "))

        if predicción < número_aleatorio:
            print("Intentalo otra vez. Este número es muy pequeño.")

        elif predicción > número_aleatorio:
            print("Intentalo otra vez. Este número es muy grande.")

    print("Enhorabuenaaaa!!!!!! Por fin acertaste el número", número_aleatorio, "Te ha costado mucho jaja.")


adivina_el_número(100)

