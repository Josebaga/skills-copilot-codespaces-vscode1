#Al principio del programa importamos las librerias que vamos a necesitar en este caso libreria re(Expresiones regulares)
import re
#funcion find
def s_find(string):
    posarroba = string.find("@")
    print("String @ position:", posarroba)
    posespacio = string.find(" ", posarroba)
    print("String Space position:", posespacio)
    dominio = string[posarroba+1: posespacio]
    print ("String Slice [18-27]:", dominio)
    return dominio

#funcion split
def s_split(string):
    words = string.split()
    print("Word List:", words)
    word = words[1]
    Email = word.split("@")
    print("Email List:",Email)
    Domain = Email[1]
    return Domain

#funcion re
def s_re(string):
    #Extraer nombre y dominio con la REGEX(caracteres que hacen extraer lo que quieres)
    groups = re.findall("^From ([^ ]*)@([^ ]*)", string)
    print(f"RegEx Groups List: {groups}")
    regex = groups[0]
    doman = regex[1]
    return doman

#Main
string = "From stephen.marq@uct.ac.ra Sat Jan 5 09:20:44 2009"

#imprimir en pantalla 
print ("String:", string)
# llamar a la funcion find
print ("### Find Domain using find() ###")
print(f"Doamin: {s_find(string)}")

#llamar a la funcion split
print("### Find Domain using split() ###")
print(f"Doamin: {s_split(string)}")

#Llamar a la funcion RegEx re.finall()
print("### Find Domain using Regex re.findall() ###")
print(f"Domain: {s_re(string)}")                              #LA F SIGNIFICA DAR FORMATO NO LLAMAR A LA FUNCION
