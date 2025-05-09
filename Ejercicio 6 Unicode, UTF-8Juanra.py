# Definir funcion dec_BinHexa()
def dec_BinHexa(E):
    print("OK, this is a Decimal Number: ", int(x))
    print()
    print("\033[33mDecimal Number transformation to HEXADECIMAL/BINARY:\033[0m")
    print(f"DECIMAL: {int(x):<10}  HEXADECIMAL: {hex(E):<10}  BINARY: {bin(E)}")
    print()            #:<10 es rellenar con espacios a la izquierda :<10 indica que el resultado debe ocupar al menos 10 espacios, alineando el valor a la izquierda. Si el valor en hexadecimal es más corto que 10 caracteres, se rellenarán los espacios restantes con espacios en blanco.

# Definir función str_Unicode()
def str_Unicode(S):
    print("OK, this is a String: ", str(x))
    print()
    print("\033[33mString transformation to UNICODE (per character):\033[0m")
    for i in S:       
        #for a in i.encode():      #.encode() ‘Iruña’.encode()->b“Iru\xc3\xb1a” en UTF-8             
            #a = "".join(bin(a)[2:].zfill(8))
            #print(a)   #Para comprobar que hemos hecho                              #con el espacio en las comillas separamos los elementos de la string y con .join() añadimos los octetos
        print(f"{i:<3} DECIMAL= {ord(i):<6} BINARIY= {bin(ord(i))[2:].zfill(8):<18}  HEXADECIMAL= \\x{hex(ord(i))[2:]:<8}   UTF-8= {" ".join((bin(a)[2:].zfill(8)) for a in i.encode())}")
        #print(f"{i:<3} DECIMAL= {ord(i):<6} BINARIY= {bin(ord(i))[2:].zfill(8):<18}  HEXADECIMAL= \\x{hex(ord(i))[2:]:<8}   UTF-8= \n{" ".join((bin(a)[2:].zfill(8)) for a in i.encode())}")
    print()                                 # Contrabarra \ dos vecesx delante para añadir \x, [2:] para quitar el 0b        \n salto de linea
        #Con el ord(i) hemos sustituido por el unicode                       
#Main
x = input("\033[33mPlease Enter a Number or String: \033[0m")   #Solicitar entrada con color amarillo
try:
    b = int(x)                 #Si es entero int, para que sea decimal float(con coma y cero)(,0)
    validar = "OK"              #COMPARAR
except:
    validar = "NOK"             #COMPARAR
    
if validar == "OK": # comparar validaciones (si es entero solo se ejecuta la de dentro del if)
    dec_BinHexa(int(x))     # LLamar a la funcion  dec desde aquí para que tome el entero 
str_Unicode(str(x))     # LLamar a la funcion  str desde aquí para que tome la string

input("\033[33mPress any key to finish \033[0m")