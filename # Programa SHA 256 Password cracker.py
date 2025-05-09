# Programa que toma como entrada un fichero de texto con el siguiente formato:
# user1:password1
# user2:password2
# user3:password3
# ...
# Calcula el Hash SHA256 de las passwords en claro y genera un nuevo fichero con el siguiente formato:
# user1:hash1
# user2:hash2
# user3:hash3

from Crypto.Hash import SHA256

#FUNCTIONS
def calcular_hash(data):
    h = SHA256.new(data.encode('utf-8'))
    h_data = h.hexdigest()
    return h_data

def pssw_crack(psswd_hash_file, dict_file):
    try:
        fh1 = open(psswd_hash_file, 'r', encoding='utf-8')
    except:
        print(f'**ERROR**: Could not open file: {psswd_hash_file}')
        return

    try:
        dict_fh = open(dict_file, 'r', encoding='utf-8')
    except:
        print(f'**ERROR**: Could not open dictionary file: {dict_file}')
        return
    
    password_list = [line.strip() for line in dict_fh]
    dict_fh.close()

    for line in fh1:
        user, h_psswd = line.strip().split(':')
        found = False
        for pwd in password_list:
            if calcular_hash(pwd) == h_psswd:
                print(f'[CRACKED] {user}: {pwd}')
                found = True
                break
        if not found:
            print(f'[FAILED] {user}: Password not found in dictionary')

    fh1.close()
#END FUNCTIONS


# MAIN

psswd_file = "C:/Users/Joseba/python/passwords.txt"
psswd_hash_file = "C:/Users/Joseba/python/psswd_hash_file"
dict_file = "C:/Users/Joseba/python/dict_file"
pssw_crack(psswd_hash_file, dict_file)
#Abro el fichero con los usuarios y passwords en claro
#user1:psswd1
#user2:passwd2
#...
try:
    fh1 = open(psswd_file, 'r', encoding='utf-8')
except:
    print(f'**ERROR**: Could not open file: {psswd_file}')
    exit()

#Creo un nuevo fichero para almacenar los usuarios y passwords hasheadas
#user1:hash1
#user2:hash2
#...
try:    
    fh2 = open(psswd_hash_file, 'w', encoding='utf-8')
except:
    print(f'**ERROR**: Could not open file: {psswd_hash_file}')
    exit()


#Leao el archivo original linea por linea, hasheo la password y la escribo en el fichero destino
for line in fh1:
    (user, psswd) = line.strip().split(':') #Separo usuario y password eliminando espacios en blanco y saltos de línea
    #print(f'User={user}:Password={psswd}')

    h_psswd = calcular_hash(psswd)    #Calculo el Hash de la password
    fh2.write(f'{user}:{h_psswd}\n')  #Escribo user:hash en el fichero destino
    print(f'User={user}:Password={psswd}:Hash={h_psswd}')

#Cierro los ficheros:
fh1.close()
fh2.close()
