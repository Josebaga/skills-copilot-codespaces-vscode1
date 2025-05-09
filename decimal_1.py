x = input(" ingresa un numero decimal: ")
decimal = int(x)
#decimal = 255
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
      hexadecimal = str(remainder) + hexadecimal
    else:
      hexadecimal = chr(remainder - 10 + ord('a')) + hexadecimal
    decimal //= 16
print(hexadecimal) 

def dec_BinHexa(E):
    hexa = ""
    bin = ""
    while E > 0:
        resto = E % 16
        if resto < 10:
            hexa = str(resto) + hexa
        else:
            hexa = chr(resto - 10 + ord("a")) + hexa
        E //= 16
    print("\033[33mDecimal Number transformation to HEXADECIMAL/BINARY:\033[0m")
    print("DECIMAL:", int(x),    "HEXADECIMAL:", "0x"+"".join(hexa),    "BINARY:", "0b"+"".join(bin))
    print()

print(f"{dec_BinHexa(int(x))}")

def dec_bin(A):
   if A == 0:
      return "0"
   else:
    A == (A // 2) + str(A % 2)
    
    print (A)