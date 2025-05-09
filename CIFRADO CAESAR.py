#CIFRADO CAESAR

#Escribir un programa en PYTHON que decodifique un mensaje ASCII codificado usando en algoritmo de cifrado CAESAR (sustitución de letras del alfabeto desplazando “X” caracteres).

#Program to decode a message encrypted with Caesar algorithm

import string

#FUNCTIONS
def caesar_decrypt(cryptogram, shift):
    # Generate alphabet (uppercase, lowercase)
    A = ''.join([chr(65+num) for num in range(26)])
    a = ''.join([chr(97+num) for num in range(26)])
        
    #A = string.ascii_uppercase #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #a = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
    
    flag = ''
    for c in cryptogram:
        if c.isalpha():
            if c.isupper():
                index = A.find(c)
                flag += A[(index - shift) % len(A)]
            if c.islower():
                index = a.find(c)
                flag += a[(index - shift) % len(a)]                
        else:
            flag += c
        
    return flag


#MAIN
message = 'P0apynir'
#message = 'EXXEGOEXSRGI'

# Loop to shift from 0 to 25
for s in range(26):
    flag = caesar_decrypt(message, s)
    print(f'Salto = {s}, Mensaje Decodificado = {flag}')