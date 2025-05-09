#EXAMEN JOSEBA

#Transformar el String de Bits en una lista de Bits rellenda con ceros al final para que su longitud sea multiplo de 6
def bitStr_bitList(bit_str):
    bitList = [int(bit) for bit in bit_str] # tamaño de la lista
    pad = (6 - (len(bitList) % 6)) % 6 # numero de ceros que hay que añadir para que sea multiplo de 6
    for _ in range (pad):   # como append solo agrega un cero lo metemos en bucle para añadirle los que queremos
        bitList.append(0)
    return bitList, pad

#Transformar la lista de Bits rellenada con ceros en un String Base64
def bitList_base64(bitList, pad):
    b64_dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # diccionario b64
    SixBitList = [bitList[i:i+6] for i in range(0, len(bitList), 6)] #lista de listas de 6
    print(f"**INFO LOG** SixBitList: {SixBitList}")
    base64codes = [(sum(t[i] * (2 ** (len(t) - i - 1)) for i in range(len(t)))) for t in SixBitList] #convertir lista de 6 en decimal
    print(f"**INFO LOG** Base 64 Codes: {base64codes}\n")
    return ''.join(b64_dict[c] for c in base64codes) + "=" * (pad // 2) #eliminar comas espacios, sustituir por el valor debase64 y añadir = 

#Main
while True:
    try:
        x = input("\033[33mPlease enter the name of the Binary File: \033[0m") # Solicitar entrada            
        fh = open(x, "rb") # abrir en modo binario
        buffer = fh.read() #leerlo
        print(f"**INFO LOG** File \"{x}\" successfully open.")
        print("**INFO LOG* READING FILE")
        print(f"**INFO LOG** Raw content of the Binary File: {buffer}")
        fh.close()  #cerrar fichero
        break
    except:  # No es correcta la entrada solicito de nuevo
        print ("File not found,try again.") 

i = 0
while i < len(buffer):
    z = buffer[i] #convierte en decimal el primer byte 
    t = buffer[i+1:z+i+1] # tramo de lectura de bytes
    print(f"\n[NEW BYTE SEQUENCE DETECTED:] {t}")
    print(f"*INFO LOG* Bytes Length = {z}, Bytes Sequence = {t}\n")
#STEP 0: Leer la siguiente secuencia de bytes del ‘buffer’    
    i = i + 1 + z # Avanzar una posicion + el entero del byte
#STEP 1: Transformar la secuencia de Bytes en un String de Bits
    bit_str = ''.join(bin(b)[2:].zfill(8) for b in t) #Cada byte de t lo conviertes a su representación binaria de 8 bits
    print("**INFO LOG** STEP1: Transforming Bytes sequence to Bit String:")
    print(f"**INFO LOG** Bit String: \"{bit_str}\"\n")
#STEP 2 LLamar a la funcion bitStr_bitList()
    bitList, pad = bitStr_bitList(bit_str)
    print("**INFO LOG** STEP2: Creating Bit List padded with 00's (multiple of 6):")
    print(f"**INFO LOG** Original Len = {8*len(t)}, Filled Len = {8*len(t)+pad}, Pad = {pad}")
    print(f"**INFO LOG** BitList: {bitList}")
    print(f"**INFO LOG** Pad: {pad}\n")
#STEP 3 Llamar a la función bitList_base64()
    print("**INFO LOG** STEP3: Calculating BASE64 String:") 
    d = bitList_base64(bitList, pad)    
    print(f"[BASE64 STRING:] \033[31m{d}\033[0m")
input("\033[33mPress any key to finish \033[0m")