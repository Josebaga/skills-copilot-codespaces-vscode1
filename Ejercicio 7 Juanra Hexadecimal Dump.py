#Hexadecimal Dump
import os
#Definir función hexdump
def hexdump(src, lenght, offset):
    lines = []
    for i in range(0, len(src), lenght):
        lin = src[i:i+lenght] #para extraer 16 bytes por linea del texto   y lugo los 16 siguientes
        print(lin)
        hexa = ' '.join(hex(b)[2:].zfill(2).upper() for b in lin)                   #f'{b:02X}' =====> hex(b)[2:].zfill(2).upper()
        texto = ''.join([chr(b).isprintable() and chr(b) or "." for b in lin])         # if 32 <= b < 127 else =====>
        lines.append(f'{offset + i:08X} {hexa:<48} {texto}')
        #print(texto)
    return lines
#Main pedir al usuario que ingrese el path del archivo y comprobar que existe
while True:
    x = input("\033[33mPlease enter the full path of the file: \033[0m")
    try:
        fh = open(x, "rb")
        break
    except:
        print ("File not found")

tamaño = os.path.getsize(x)
n_líneas = tamaño // 16 + 1
n_pags = n_líneas // 20 + 1
print(f"The size of C:\\Users\Joseba\\python\\mbox-short.txt is {tamaño}") #\\ doble para que no la tenga en cuenta
print(f"The number of 16 byte lines will be {n_líneas}")
print(f"The number of 20 line pages will be {n_pags}")
print()
src = fh.read(20*16)
lenght = 16
offset = 0
#print(src)
for n_pags in range(n_pags):
    validar = input(f"\033[33mPress {n_pags +1} to print Page {n_pags + 1} or Press another key to finish:\033[0m")
    if validar == str(n_pags + 1):   
        lines = hexdump(src, lenght, offset)
        for line in lines:
            print(line)
        print()
    else:
        break

fh.close()
#input("\033[33mPress any key to finish \033[0m")