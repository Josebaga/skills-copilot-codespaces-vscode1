#RSA ENCRYPT para cifrar un mensaje y generar confidencialidad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# FUNCTIONS

# Function that generates a pair of RSA Public-Private Keys.
# It takes as arguments:
# - The Size of the key Pair
# - The key Format (PEM, SSH, DER) to export it

def gen_keys(size, key_format):
    #Generate a Private-Public RSA key pair of size
    keys = RSA.generate(size)
    
    pub_key = keys.publickey().export_key(key_format)
    priv_key = keys.export_key(key_format)

    return pub_key, priv_key


# Function to encrypt data with RSA Public Key
# It takes as arguments:
# - An RSA key Pair
# - The Data to encrypt (in Binary)

def pub_key_encrypt(pub_key, data):
    # Create RSA Cipher Object, providing Public Key
    cipher_rsa = PKCS1_OAEP.new(pub_key)
    
    # Encrypt Data Bytes with the Public Key
    ciphertext = cipher_rsa.encrypt(data)

    return ciphertext
 

# Function to decrypt data with RSA Private Key
# It takes as arguments:
# - An RSA key Pair
# - The Data encrypted with the RSA Public Key

def priv_key_decrypt(keys, enc_data):
    # Create RSA Decipher Object, providing Private Key
    decipher_rsa = PKCS1_OAEP.new(keys)
    
    # Decrypt Data Bytes with the Private Key
    deciphertext = decipher_rsa.decrypt(enc_data)

    return deciphertext 


# MAIN
size=2048
formats = ["PEM", "OpenSSH", "DER" ]

print(f'\n*** GENERATE RSA PRIVATE-PUBLIC KEYS ***')

# Generate Key Pairs and Export them in different formats
for key_format in formats:
    pub_k, priv_k = gen_keys(size, key_format)
    print(f"Key Format: {key_format}")
    print(f"PUBLIC KEY ({len(pub_k)} Bytes)\n{pub_k}\n")
    print(f"PRIVATE KEY ({len(priv_k)} Bytes)\n{priv_k}\n")
    

# Encrypt Data with Public Key & Decrypt it with Private Key
data='Hello World\n1111111111111\nEND€¿ñ'.encode()
#data = os.urandom(32)

print(f'\n\n*** ENCRYPT DATA WITH RSA PUBLIC KEY ***')

keys = RSA.generate(size)
enc_data = pub_key_encrypt(keys.publickey(), data)
print(f'\nORIGINAL DATA ({len(data)} Bytes):\n{data}')
print(f'\nENCRYPTED DATA ({len(enc_data)} Bytes):\n{enc_data}')


print(f'\n\n*** DECRYPT DATA WITH RSA PRIVATE KEY ***')
dec_data = priv_key_decrypt(keys, enc_data)
print(f'\nDECRYPTED DATA ({len(dec_data)} Bytes):\n{dec_data}')