#Programa que extrae las 10 palabras más repetidas de un fichero que está en una ruta
#Función
def top_words(fh):
    #crear un diccionario con las palabras y las veces que se repiten
    cuantas = {}
    for texto in fh:
        palabras = texto.split()
        for word in palabras:
            #word = word.strip()
            cuantas[word] = cuantas.get(word, 0) + 1
    #crear lista sobre el diccionario
    wordlist= list()
    for k,v in cuantas.items():
        wordlist.append((v,k))
    # ordenar los elementos y extraer los 10 primeros
    wordlist.sort(reverse=True)
    lista = wordlist[:10]
    #retorno de la funcion
    return lista

 #MAin pedir al usuario que introduzca una ruta de fichero(open) y comprobar que es cierto con tryexcept  
while True:
    rutarchivo = input("Please enter the full path of the file: ")
    try: #dentro open>>>>>>>>>>>si funciona > break, si no funciona > except
        fh = open(rutarchivo, "r+")
        print("File Found")
        print()
        break
    except:
        print ("File not found")
 
#llamar a la funcion top_words e imprimir resultados
listapalabras = top_words(fh)
print("Top 10 Words in File: c:/Users/Joseba/python/mbox-short.txt")
print(listapalabras)
print()
print("Top 10 Orderer word list:")
#para dar la vuelta a los valores e imprimirlos
for (x, y) in listapalabras:
    print(y, x)
print()
#cerrar el fichero
fh.close()
input("Please enter any key to finish: ")