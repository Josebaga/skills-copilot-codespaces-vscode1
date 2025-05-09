# Escribir un programa en PYTHON que transforme un número Binario de longitud arbitraria
# en un número Decimal y Hexadecimal

## NOTE: EXAMPLES WITH RANGES   
    ## WHITE_PAWN='x'
    ## row = [WHITE_PAWN for i in range(8)]
    ## ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

    ## squares = [x ** 2 for x in range(10)]
    ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    ## board = [[(row*3+column+1) for column in range(3)] for row in range(3)]
    ## [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Import RegEx Library
import re

#FUNCTIONS

# Function to transform a String of cvharacters '0' & '1' into a list of integers 0 & 1, padded with 0's (BIG ENDIAN)
# to make the number of digits multiple of 4.

def bitStr_bitList(s):
    #Fill input string with 0's on the left (BIG ENDIAN) to make the number of digits multiple of 4
    if len(s)%4 != 0:
        bitStr = s.zfill(len(s)+4-len(s)%4)
    else:
        bitStr = s
    print(f" Original Len = {len(s)}")
    print(f" Filled Len = {len(bitStr)}")

    # Transform the padded string into a list of integers
    bitList=[]
    for b in bitStr:
        bitList.append(int(b))
    # Another option to create the list in a single line of code:
    #[int(b) for b in bitStr]
    
    # Return the padded list of integers
    return bitList



# Function to transform a list of integers 0 & 1 into a DECIMAL number.
# The list is padded with 0's (BIG ENDIAN)to make the number of digits multiple of 4.

def bitList_dec(bitList):
    # Create a list of powers of 2, in descendent order: [128, 64, 32, 16, 8, 4, 2, 1]
    twos = [2 ** i for i in range(len(bitList)-1,-1,-1)]
    #print(twos) 
    
    # Calculate the Decimal number multiplying the 1's by the corresponding powers of 2 and adding teh values
    ## Powers of 2: [128, 64, 32, 16, 8, 4, 2, 1]
    ## BitList:     [  1,  0,  1,  0, 1, 1, 1, 0]
    ## Result:      [128+  0+ 32+  0+ 8+ 4+ 2+ 0] = 174
    
    dec=0
    # Use i to iterate through the lists
    for i in range(len(bitList)):
        dec+=bitList[i]*twos[i]
        
        #Print for Debugging purposes
        if bitList[i] != 0:
            print(f" {twos[i]} * {bitList[i]} = {bitList[i]*twos[i]}")
   
    #Print for Debugging purposes
    print(f"  Total= {dec}")
    
    #Return the DECIMAL value
    return dec



# Function to transform a list of integers 0 & 1 into an HEXADECIMAL number.
# The list is padded with 0's (BIG ENDIAN)to make the number of digits multiple of 4.

def bitList_hexa(bitList):
    # Create a list of Hexadecimal characters
    # Option 1 to create hex_dict:
    #hex_dict = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    # Option 2 to create hex_dict:
    hex_dict=[]
    c = ord('0')
    hex_dict += [chr(c+i) for i in range (0,10)]    # Adds characters [0-9]
    c = ord('A')
    hex_dict += [chr(c+i) for i in range (0,6)] # Adds characters [A-F]

    # Option 3 to create hex_dict:
    #hex_dict = [f"{i:X}" for i in range(16)]  
    
    # Create a list where each element is a group/list of Four-bits.
    # Example: [[1, 0, 1, 0], [1, 1, 1, 0]]
    
    fourBitList = [[b for b in bitList[i:i+4]] for i in range(0,len(bitList), 4)]
    # Another option
    # fourBitList = [[b for b in bitList[i*4:(i+1)*4]] for i in range(len(bitList)//4)]
    
    print(f" FourBitList: {fourBitList}")
    
    # Iterate through the list of 4-bit elements
    hexa=''
    for bit4 in fourBitList:
        # For each 4-bit element, calculate its corresponding Hexadecimal Digit
        # First calculate its DECIMAL value (using the "bitList_dec" function"
        h_dec = bitList_dec(bit4)
        # Then transform the DECIMAL into HEXADECIMAL usig the list
        hex_digit=hex_dict[h_dec]
        hexa+=hex_digit
        print(f"{bit4} --> {h_dec} --> {hex_digit}")
    return hexa
    

#END FUNCTIONS


#MAIN
#s = '1101010000' # BIG ENDIAN

#Ask for a binary string and check for input validity
while True:  
    #Ask the user for a valid binaty string
    s= input("Please enter a binary sequence (0's & 1's): ")
    
    # OPTION 1: Check String Format with RegEx:
    if re.search('^[01]+$', s):
        break
    else:
        print("\t***ERROR: Wrong Binary Number***\n")
    
    #OPTION 2: Check String Format one character at a time:
    #valid_string = True
    # for c in s:
        # if c=='0' or c =='1':
            # continue
        # else:
            # print("\t***ERROR: Wrong Binary Number***\n")
            # valid_string = None
            # Exit the For loop if one character is not valid (not 0 or 1)
            # break
    
    #Exit the While loop if all characters are valid (0 or 1)
    # if valid_string:
        # break


print("\nCreating Bit List padded with 0's (BIG ENDIAN):")
bitList = bitStr_bitList(s)
print(" BitList", bitList)

print("\nCalculating DECIMAL number:")
dec = bitList_dec(bitList)
print(f"\nDECIMAL Number:\n{dec}")

print("\nCalculating HEXADECIMAL number:")
hexa = bitList_hexa(bitList)
print(f"\nHEXADECIMAL Number:\n 0x{hexa}")


s=input("\n\nEnter any key to finish")

#END MAIN








