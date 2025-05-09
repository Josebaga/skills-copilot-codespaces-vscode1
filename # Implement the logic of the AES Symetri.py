# Implement the logic of the AES Symetric Cryptography algorithm


# FUNCTIONS
def aes_block_cipher(key, block):
    #print (key, block)
    # Transform 16 byte block into a 4x4 matrix
    matrix = [[byte for byte in block[i:i+4]] for i in range(0, len(block), 4)]
    
    # Trnasform 16 byte key into a 4x4 matrix
    k_matrix = [[byte for byte in key[i:i+4]] for i in range(0, len(key), 4)]

    print(f'\tBlock Matrix: {matrix}')    
    print(f'\tKey Matrix: {k_matrix}')
    
    n_rounds = 10
    
    # Round 0
    n = 0
    print(f'\tROUND {n}: AddRoundKey')
    s_matrix = addRoundKey(matrix, k_matrix)
    
    # Rounds 1 to 9 of data transformation
    for n in range(1, n_rounds):
        print(f'\n\tROUND {n}: SubBytes + ShiftRows + MixColumns + AddRoundKey')
        s_matrix = subBytes(s_matrix)
        s_matrix = shiftRows(s_matrix)
        s_matrix = mixColumns(s_matrix)
        s_matrix = addRoundKey(s_matrix, k_matrix)
    
    # Round 10
    n += 1
    print(f'\n\tROUND {n}: SubBytes + ShiftRows + AddRoundKey')
    s_matrix = subBytes(s_matrix)
    s_matrix = shiftRows(s_matrix)
    s_matrix = addRoundKey(s_matrix, k_matrix)
    
    return s_matrix


def addRoundKey(m, k_m):
    # XOR the state matrix with the Key matrix
    s_m = [[m[i][j] ^ k_m[i][j] for j in range(4)] for i in range(4)]
    print(f'\tAdd Round Key: {s_m}')
    return s_m
      

def subBytes(m):
    # Substitution Table: each value from 0 to 255
    sub_table = [(i+1) % 256 for i in range(256)]
    # Substitute each Byte from a substitution table
    s_m = [[sub_table[m[i][j]] for j in range(4)] for i in range(4)]
    print(f'\tSub Bytes: {s_m}')
    return s_m

def shiftRows(m):
    s_m = [[m[i][(j+i) % 4] for j in range(4)] for i in range(4)]
    print(f'\tShift Rows: {s_m}')
    return s_m
    
def mixColumns(m):
    # Constant Matrix: each value from 0 to 255
    const_table = [[i for j in range (4)] for i in range (4)]
    # Multiply each Byte from a column
    s_m = [[(const_table[i][j] * m[i][j]) % 256 for j in range(4)] for i in range(4)]
    print(f'\tMix Columns: {s_m}')
    return s_m
    
# END FUNCTIONS



# MAIN
data = b'This is a message to encrypt with AES algorithm'  # len(data) = 47 bytes (3 AES blocks)
#data = "This is a message to encrypt with AES algorithm".encode('utf-8')
#data = os.urandom(16) #Random byte sequence
key = b'1234567890123456'   # AES 128 bit Key
#key = os.urandom(16) # Define a random key: Example: b'\x8bg\xef\xee\x10\xa6\x9e\x17G\xc6\xb4\xdcF`3\x1d'


# Padding to make size multiple of 16 Bytes (one AES Block)
if len(data) % 16 != 0:
    data += b'\x00' * (16 - len(data) % 16)

print(f'****Plaintext Data (padded with 0x00): {data}****')
print(f'****AES Encryption key {len(key)*8} bits: {key}****')

# Loop to encrypt AES blocks of 16 bytes
n = 0
for i in range(0, len(data), 16):
    input("\n\nPulsa INTRO para imprimir el siguiente bloque de 16 bytes:\n")
    block = data[i:i+16]
    h_block = ' '.join([f'{byte:02x}'.upper() for byte in block])
    #h_block = ' '.join([hex(byte)[2:].zfill(2).upper() for byte in block])
    d_block = [byte for byte in block]
    print(f'\nOriginal Block {n} (Hexadecimal): {h_block}')
    print(f'Original Block {n} (Decimal): {d_block}')
    
    c_block = aes_block_cipher(key, block)
    
    #print(c_block)
    h_c_block = ' '.join([f'{c_block[j][i]:02x}'.upper() for j in range(4) for i in range(4)])
    print(f'\nOriginal Block {n} (Hexadecimal): {h_block}')
    print(f'AES Ciphered Block {n} (Hexadecimal): {h_c_block}')
    n += 1

input('\n\nEnter any key to exit...')

# END MAIN