#EXAMEN
import base64
#string de bits en una lista de bits
def bitStr_bitList(bit_str):
    
    return [int(bit) for bit in bit_str]

#Main
while True:
    try:
        x = input("\033[33mPlease enter the name of the Binary File: \033[0m") # Solicitar entrada            
        fh = open(x, "rb") # abrir en modo binario
        buffer = fh.read() #leerlo
        print(f"**INFO LOG** File \"{x}\" successfully open.")
        print("**INFO LOG* READING FILE")
        print(f"**INFO LOG** Raw content of the Binary File:{buffer}")
        fh.close()  #cerrar fichero
        break
    except:  # No es correcta la entrada solicito de nuevo
        print ("File not found,try again.") 
i = 0
while i < len(buffer):
    z = buffer[i]
    t = buffer[i:i+z]
    i += z
    
    bit_str = ''.join(f"{byte:08b}" for byte in t)
    bit_list = bitStr_bitList(bit_str)
#for i in range(0, len(list), 6):

print(t,z, i)
print("[NEW BYTE SEQUENCE DETECTED:] b'Python'")
print()
print("**INFO LOG** STEP1: Transforming Bytes sequence to Bit String:")
print(f"**INFO LOG** Bit String: {bit_str}")
print("**INFO LOG** STEP2: Creating Bit List padded with 00's (multiple of 6):")
#print(f"**INFO LOG** Original Len = {len}, Filled Len = 48, Pad = 0")
def bitList_base64(bitList, pad):
    b64_dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64codes = [(sum(t[i] * (2 ** (len(t) - i - 1)) for i in range(len(t)))) for t in 
                    [bitList[i:i+6] for i in range(0, len(bitList), 6)]]
    return ''.join(b64_dict[c] for c in base64codes) + "=" * (pad // 2)