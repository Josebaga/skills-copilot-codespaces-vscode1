def bitStr_bitList(str):
    lista = [] 
    for a in str:
        lista.append(int(a))
    return lista
def bitList_dec(list):
    listados = [2**i for i in range(len(d)-1, -1, -1)] 
    print("Calculating DECIMAL number:")
    f = sum(a*p)
    while list:
        a, p = listados.pop(0), d.pop(0)
        print(f"{p} * {a} = {a * p}")
        return f
def bitList_hexa(list): #definir funcion que devuelva hexadecimal de una lista de enteros 0 y 1
    #fe = "OX"
    list = [list[i:i+4] for i in range(0, len(list), 4)]
    #print("FourBitList: ",list)
    #for a in list:
        #a = bitList_dec(a)  
    #return fe #fe lo que es tengo pero salir no sale
    return "0x" + "".join(hex_table[bitList_dec(list[i:i+4])] for i in range(0, len(list), 4))

while True: #Main comprobar con while true que la entrada son 0's y 1's y crear variables
    x = input("Please enter a binary sequence: ")
    valid_string = "OK"
    for i in x :
        if i == "0" or i == "1":
            continue
        else:
            valid_string = "NOK"
            break
    if valid_string == "OK":
#print("hola") para comprobar que ha llegado hasta aqui el programa
        break
#print("adios") para comprobar que ha llegado hasta aqui el programa
    if valid_string == "NOK":
        print("Isn't a correct binary sequence.")
#Main
b = x.zfill(len(x)+4-len(x)%4) #rellenar con ceros hasta multiplo de cuatro
hex_table =[]
c = ord("0")
hex_table += [chr(c+i) for i in range(10)]
c =ord("A")
hex_table += [chr(c+i) for i in range(6)] #crear lista hexadecimal añadiendo los 6 ultimos valores letras


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