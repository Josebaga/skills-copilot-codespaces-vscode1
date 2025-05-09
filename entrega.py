#convertir binario a decimal / hexadecimal
#definir funcion que convierte la string en lista, calcula su tamaño y agrega 0's delante hasta que sea multiplo de 4
def bitStr_bitList(str):
    lista = [] 
    for a in str:
        lista.append(int(a))
    return lista

def bitList_dec(list): #definir funcion que devuelva un entero, de la lista de enteros 0 y 1
    listados = [2**i for i in range(len(list)-1, -1, -1)]  #crear lista de potencias de 2 de igual longitud a la entrada
    list = {listados[i]: list[i] for i in range(len(list))}    # crear un diccionario con las 2 listas
    #print(list) 
    f = sum(a * b for a, b in list.items())
    for (a, b) in list.items():
        print(a, "*", b, "=", a*b)  #OJO poner comas
    print("                 Total =", f)
    return f
     
def bitList_hexa(list): #definir funcion que devuelva hexadecimal de una lista de enteros 0 y 1
    list = [list[i:i+4] for i in range(0, len(list), 4)]
    print("FourBitList: ",list)
    hex_table =[]
    c = ord("0")
    hex_table += [chr(c+i) for i in range(10)]
    c =ord("A")
    hex_table += [chr(c+i) for i in range(6)] #crear lista hexadecimal añadiendo los 6 ultimos valores letras
    t = [bitList_dec(a) for a in list]
    h = [hex_table[int(f)] for f in t]
    return "0x" + "".join(h)
    
while True: #Main comprobar con while true que la entrada son 0's y 1's y crear variables
    x = input("Please enter a binary sequence: ")
    valid_string = "OK"
    for i in x :
        if i == "0" or i == "1":
            continue                         #CONTINUEEEEEEEE
        else:                                   
            valid_string = "NOK"
            break
    if valid_string == "OK":
#print("hola") para comprobar que ha llegado hasta aqui el programa
        break
#print("adios") para comprobar que ha llegado hasta aqui el programa
    if valid_string == "NOK":
        print("Isn't a correct binary sequence.")
    
b = x.zfill((len(x)+4-len(x)%4)%4) #rellenar con ceros hasta multiplo de cuatro

#prints y llamar a la funcion 1
print("Creating Bit List padded with 0's (BIG ENDIAN):")
print("Original Len = ",len(x))
print("Filled Len =", len(b))
d = bitStr_bitList(b)
print("Bitlist ", d)
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
print("HEXADECIMAL Number:")
print(hexaopera)
input("Please enter any key to finish: ")