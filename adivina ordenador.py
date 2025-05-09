import random


def adivina_el_número_ordenador(x):


    print("=============================")
    print("====¿Que número pienso?======")
    print("=============================")
    print(f"Selecciona un número entre 1 y {x} para que el ordenador intente adivinarlo.")

    límite_inferior = 1
    límite_superior = x

    respuesta = ""

    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior
         #  Obtener respuesta  

        respuesta = input(f"Creo que será... {predicción}. Si es muy alta, ingresa (A), si es muy baja ingrsa (B), si es correcto ingrsa (C).").lower()
        
        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(f"Bravo el ordenador adivinó tu número {predicción}, que bueno soy!!!!")


adivina_el_número_ordenador(50)




