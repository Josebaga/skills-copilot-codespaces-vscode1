#FIRMA DIGITAL
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import os

# FUNCTIONS

# Function to Generate Key Pairs and Export them to files in PEM formats
# It receives as arguments:
#   The size of the Key
#   The format of the exported Keys
#   The path where the exported keys will be stored

def generate_and_store_keys(key_size, key_format, key_path):
    # Calculate the full path where the PEM files will be stored
    priv_pem_file = os.path.join(key_path, "priv_key.pem")
    pub_pem_file = os.path.join(key_path, "pub_key.pem")

    #Generate a Private-Public RSA key pair of size
    key = RSA.generate(key_size)
    priv_pem = key.export_key(key_format)
    pub_pem = key.publickey().export_key(key_format)
    
    # Export the Private Key to a PEM file
    with open(priv_pem_file, 'wb') as pem_fh:
        pem_fh.write(priv_pem)
    print(f'PEM PRIVATE FILE NAME: {priv_pem_file}: SIZE: {os.path.getsize(priv_pem_file)}')
    #print(f'\nDATA: {pem.decode()}')

    # Export the Public Key to a PEM file
    with open(pub_pem_file, 'wb') as pem_fh:
        pem_fh.write(pub_pem)
    print(f'PEM PUBLIC FILE NAME: {pub_pem_file}: SIZE: {os.path.getsize(pub_pem_file)}')
    #print(f'\nDATA: {pem.decode()}')
    return key



# Function to Calculate the Hash of a given File
# It receives as argument the full path of the File
# And returns the hash in binary & hexadecimal format

def calculate_file_hash(filename):
    # Open the file and store binary content in a variable
    with open(filename, 'rb') as fh:
        content = fh.read()

    # Calculate the SHA256 hash value of the file content
    h_obj = SHA256.new(content) # Create SHA256 Hash Object
    b_hash = h_obj.digest()     # Obtain Hash as a Bytes sequence
    hx_hash = h_obj.hexdigest() # Obtain Hash as an Hexadecimal String
    print(f'DOCUMENT NAME: {filename}: SIZE: {os.path.getsize(filename)}')
    print(f'SHA256 HEX ({len(hx_hash)} Digits): {hx_hash}\nSHA256 ({len(b_hash)} Bytes): {b_hash}')
    return h_obj
    
    

# Function that signs a hash with an RSA Private Key imported from a File
# It receives as arguments:
#   The Hash object
#   The private key object

def sign_hash(h_obj, private_key, key_path):
    # Create RSA Signature Object, providing Private Key
    sign_rsa = pkcs1_15.new(private_key)

    # Sign Hash Bytes with the Private Key
    signature = sign_rsa.sign(h_obj)

    # Calculate the full path where the Signature file will be stored    
    signature_file = os.path.join(key_path, "signature.bin")
    
    # Store Signature in signature file
    with open(signature_file, 'wb') as sign_fh:
        sign_fh.write(signature)

    print(f'RSA SIGNATURE FILE NAME: {signature_file}: SIZE: {os.path.getsize(signature_file)}')
    print(f'RSA SIGNATURE ({len(signature)} Bytes): {signature}')
    return signature


# Function that validates a signature with an RSA Public Key
# It receives as arguments:
#   The Hash object
#   The signature (binary)
#   The public key object

def verify_signature(h_obj, signature, public_key):
    print(f'ORIGINAL SHA256 (HEX {len(h_obj.hexdigest())} Digits): {h_obj.hexdigest()}')
    print(f'ORIGINAL SHA256 ({len(h_obj.digest())} Bytes): {h_obj.digest() }')
    print(f'RSA SIGNATURE ({len(signature)} Bytes): {signature}')

    # Create RSA Signature Validation Object, providing Public Key
    sign_valid_rsa = pkcs1_15.new(public_key)

    # Validate Digital Signature Bytes with the Public Key
    try:
        sign_valid_rsa.verify(h_obj, signature)
        print(f"\n***OK***: RSA SIGNATURE IS VALID")
    except:
        print(f"\n***ERROR***: RSA SIGNATURE IS NOT VALID")



# MAIN
#filename = "C:\\PYTHON\\RSA\\Doc.pdf"
#filename = "C:\\PYTHON\\RSA\\4.2_ConstruirFunciones.pdf"
#filename = "C:\\PYTHON\\RSA\\5.2_Bucles_definidos.pdf"

# Ask user for the file to be Signed
filename = input("Please enter the file path: ")

while True:
    if os.path.exists(filename):
        print(f"File Exists: {filename}")
        break
    else:
        filename = input("File does not exist, please enter a new file path: ")


#*** STEP 1: GENERATING RSA PRIVATE-PUBLIC KEYS, storing in PEM File ***
print(f'\n\n*** STEP 1: GENERATING RSA PRIVATE-PUBLIC KEYS, storing in PEM File ***')
key_size=2048
key_format ='PEM'
key_path = os.path.dirname(filename)

key = generate_and_store_keys(key_size, key_format, key_path)


#*** STEP 2: CALCULATING FILE HASH ***
print(f'\n*** STEP 2: CALCULATING FILE HASH ***')
hash_obj = calculate_file_hash(filename)


#*** STEP 3: SIGNING HASH WITH RSA PRIVATE KEY ***
print(f'\n*** STEP 3: SIGNING HASH WITH RSA PRIVATE KEY ***')

signature = sign_hash(hash_obj, key, key_path)


#*** STEP 4: VALIDATING DIGITAL SIGNATURE ***
print(f'\n*** STEP 4: VALIDATING DIGITAL SIGNATURE ***')
pub_pem_file = os.path.join(key_path, "pub_key.pem")
signature_file = os.path.join(key_path, "signature.bin")
    
# Load Public RSA key from PEM file
with open(pub_pem_file, 'rb') as pem_fh:
    public_key = RSA.import_key(pem_fh.read())
    
# Load Signature from file
with open(signature_file, 'rb') as sign_fh:
    signature = sign_fh.read()

result = verify_signature(hash_obj, signature, public_key)