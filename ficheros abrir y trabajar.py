l = ["a", "b", "c", "d"]
for i in range(len(l)):
    l[i] = l[i].upper()

print(l)

fhand = open("ejercicio 1 juanra.py")
#error
fhand = open("C://python//ejercicio 1 juanra.py")
print(fhand)
#<_io.TextIOWrapper name='C://python//ejercicio 1 juanra.py' mode='r' encoding='cp1252'>
count = 0
for line in fhand:
    count = count+1
    print("numero de lineas", count)


for line in fhand:
    count = count+1
print("numero de lineas", count)

#numero de lineas 40

#para que salga impreso el archivo y se lea
fhand.read()


fhand.tell()
815 #posicion del lector de disco

#para cerrar fhand y no haga bucle infinito
fhand.close()    # PARA QUE NO SE SATURE EL ARCHIVO Y VOLVER A LA POSICION INICIAL     

815
#fhand.seek(0)         PARA COMPROBAR DONDE ESTA EL LECTOR
fhand = open("C://python//ejercicio 1 juanra.py")
for line in fhand:
    if not line.startswith("#"):
     print(line)
fhand.seek(0)
0
for line in fhand:
     if not line.startswith("#"):
         print(line)


for line in fhand:
     if not line.startswith("#"):
         print(line.strip())


for line in fhand:
     if not line.startswith("#"):
         word=line.split()
         yo="#".join(word)
         print(yo)