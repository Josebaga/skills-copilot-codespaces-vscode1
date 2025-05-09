#crear clave de proteccion (AES)
#import os
def aesblockcipher(key, block):
    matrix = [[byte for byte in block[i:i+4]] for i in range(0,len(block), 4)]
    kmatrix = [[byte for byte in key1[i:i+4]] for i in range(0,len(key1), 4)]
    print(f"\tBlock Matrix:{matrix}")
    print(f"\tkey Matrix:{kmatrix}")
    n_rounds = 10
    n = 0
    
#MAin
x = "Este es el mensaje a escribir con AES".encode('utf-8')
#key = os.urandom(16) #------------ genera clave aleatoria (16) en este caso de 16
key1 = b'1234567890123456'
#len(x)%16 ------ el resto de dividir por 16
y = x + b'\x00'*(16-len(x)%16)  #si quisiera agregar a la misma variable x---- x+=b'\x00

for i in range(0, len(y), 16):
    block = y[i:i+16]
    #h_block = ' '.join([f'{byte:02x}'.upper() for byte in block])
    #d_block = [byte for byte in block]
    llamablock =  aesblockcipher(y, key1)   #Así llamo a la funcion con los parametros las veces  que necesito



