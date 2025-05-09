#Convertir binario a decimal / hexadecimal

def bitStr_bitList(str):   # Definir funcion que convierte la string en lista
    lista = [] 
    for a in str:
        lista.append(int(a))  # Añadir enteros a la lista
    return lista

def bitList_dec(list): #definir funcion que devuelva un entero decimal, de la lista de enteros 0 y 1
    listados = [2**i for i in range(len(list)-1, -1, -1)]  #crear lista de potencias de 2 de igual longitud a la entrada
    list = {listados[i]: list[i] for i in range(len(list))}    # crear un diccionario con las 2 listas
    f = sum(a * b for a, b in list.items())   # Operacion que nos multiplica los valores y es la que retornamos
    for (a, b) in list.items():   #  .items() es un método que se usa en los diccionarios para obtener sus claves y valores como pares (clave, valor)
        print(a, "*", b, "=", a*b)  #OJO poner comas
    print("                 Total =", f)
    return f
     
def bitList_hexa(list): #definir funcion que devuelva hexadecimal de una lista de enteros 0 y 1
    list = [list[i:i+4] for i in range(0, len(list), 4)] #crear lista en grupos de 4
    print("FourBitList: ",list)
    hex_table =[]
    c = ord("0")
    hex_table += [chr(c+i) for i in range(10)]            #   += AGREGAR CARACTERES a la lista    chr genera caracteres
    c = ord("A")
    hex_table += [chr(c+i) for i in range(6)] #Crear lista hexadecimal añadiendo los 6 ultimos valores letras
    t = [bitList_dec(a) for a in list]        # Pasar la funcion a decimal a los elementos (listas de 4) que hay en la list
    h = [hex_table[int(f)] for f in t]         # Mapear los elementos de la lista por su valor con hex_table
    return "0x" + "".join(h)                  # Extraer los elementos de la lista h [.join()] y añadirlos a la string(+)
    
while True: #Main solicitar entrada y comprobar con while true que la entrada son 0's y 1's
    x = input("\033[33mPlease enter a binary sequence: \033[0m") # Solicitar entrada
    valid_string = "OK"
    for i in x :      #bucle para recorrer toda la entrada
        if i == "0" or i == "1":
            continue                         #CONTINUEEEEEEEE
        else:    # SI NO                               
            valid_string = "NOK"
            break
    if valid_string == "OK":  # print("hola") para comprobar que ha llegado hasta aqui el programa(debajo del if sin espacios)
        break    # print("adios") para comprobar que ha llegado hasta aqui el programa (debajo del break sin espacios)
    if valid_string == "NOK":
        print("Isn't a correct binary sequence.")
    
if (len(x))%4 == 0: # si es multiplo de 4 dejarlo igual    [len(x)% es el resto de la division]
    b = (x)
else :  #ELSE ---> SI NO           ELIF----> PERO (1 falsa 2 verdadera)
    b = x.zfill((len(x)+4-len(x)%4)) # si no es multiplo de 4 rellenar con ceros hasta multiplo de cuatro(TAMAÑO +4-resto)

#prints y llamar a la funcion 1
print("Creating Bit List padded with 0's (BIG ENDIAN):")
print("Original Len = ", len(x))
print("Filled Len =", len(b))
d = bitStr_bitList(b)
#print("Bitlist ", d)
print(f"Bitlist {bitStr_bitList(x)}")
print()
#prints y llamar a la funcion 2
print("Calculating DECIMAL number:")
decopera = bitList_dec(d)
print()
print("Decimal Number:")
print(decopera)
print()
#prints y llamar a la funcion 3
print("Calculating HEXADECIMAL number:")
hexaopera = bitList_hexa(d)
print()
print("HEXADECIMAL Number:")
print(hexaopera)
input("\033[33mPress any key to finish \033[0m")
