# Convierte una cadena de bits en una lista de bits,#
# rellenándola con ceros para que su longitud sea un múltiplo de 6#
#:parámetros: 0 y 1#
#:return: Tupla #
def bitStr_bitList(s):
    bit_list = [int(bit) for bit in s]
    pad = (6 - (len(bit_list) % 6)) % 6
    bit_list.extend([0] * pad)
    return bit_list, pad

#Este lo que hace es Convierte una lista de bits en una cadena codificada en Base64.
# #:param bit_list: Lista de enteros 0 y 1
#:parametros: Número de ceros de relleno añadidos
#:return: Cadena codificada en Base64#
def bitList_base64(bit_list, pad=0):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_codes = [int(''.join(map(str, bit_list[i:i+6])), 2) for i in range(0, len(bit_list), 6)]
    b64 = ''.join(base64_chars[code] for code in base64_codes)
    if pad:
        b64 += "=" *(pad // 2)
    return b64

#MAIN 
#Abre el archivo en binario
while True:
    try:
        file_path = input("Please enter the name of the Binary File: ")
        with open(file_path, 'rb') as file:
            buffer = file.read()
        print(f"\n*INFO LOG* File \"{file_path}\" successfully open.\n")
        break
    except FileNotFoundError:
        print("*ERROR LOG* File not found. Please try again.")
i = 0
while i < len(buffer):
    #Lee el siguiente Byte
    byte_seq = buffer[i:i+6]  #Lee 6 bytes al mismo tiempo
    i += len(byte_seq)
    print(f"\n[NEW BYTE SEQUENCE DETECTED:] {byte_seq}")
    print(f"*INFO LOG* Bytes Length = {len(byte_seq)}, Bytes Sequence = {byte_seq}\n")
    
    #Convertir la secuencia de bytes en una cadena de bits
    bit_string = ''.join(format(byte, '08b') for byte in byte_seq)
    print(f"*INFO LOG* STEP1: Bit String: \"{bit_string}\"\n")
    
    #Convertir la cadena de bits en una lista de bits rellenada
    bit_list, pad = bitStr_bitList(bit_string)
    print(f"*INFO LOG* STEP2: Bit List (padded): {bit_list}, Pad: {pad}\n")
    
    #Convertir la lista de bits a Base64
    base64_string = bitList_base64(bit_list, pad)
    print(f"*INFO LOG* STEP3: Base64 String: {base64_string}\n")
#Pulsar para salir
input("Press any key to finish")