s = ["a, b, c, d, e, f"]
len(s)
#1 porque las comillas van de la a a la f
g = ["a", "b", "c", "d"]
len(g)
#4 TOdO ENTRECOMILLADO
g.append("e")
print(g)
#['a', 'b', 'c', 'd', 'e']
g.append("g") # con append añado elementos al final
print(g)
#['a', 'b', 'c', 'd', 'e', 'g']
abc = ":".join(g)
print(abc)          #CON JOIN OBTENGO UNA STRING y con los dos puntos entrecomillados >separar por :
#'a:b:c:d:e:g'
cab = "-".join(g)
print(cab)
#'a-b-c-d-e-g'
list = cab.split("-")  #CON SPLIT CREO LISTA Y ELIMINO -------
print(list)
#['a', 'b', 'c', 'd', 'e', 'g']
list.reverse()
print(list)
#['g', 'e', 'd', 'c', 'b', 'a']
list.remove("g")
print(list)
#['e', 'd', 'c', 'b', 'a']
list.reverse()
print(list)
#['a', 'b', 'c', 'd', 'e']
cab
#'a-b-c-d-e-g'
lab = cab.replace(":", "-")
print(lab)
#'a-b-c-d-e-g'
list.insert(3,"1")
print(list)
#['a', 'b', 'c', '1', 'd', 'e']
list.remove("1")
print(list)
#['a', 'b', 'c', 'd', 'e']
for i in range(len(list)):
    list[i] = list[i].upper()
print(list)