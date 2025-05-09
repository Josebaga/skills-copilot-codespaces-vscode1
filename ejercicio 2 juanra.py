#funcion que devuelve el mayor de la serie
def fmax(serie):
    max = None
    for i in serie :
        if max is None or i > max:
            max = i
    return(max)

#funcion que devuelve el menor de la serie
def fmin(serie):
    min = None
    for i in serie :
        if min is None or i < min:
            min = i
    return(min)

#funcion que devuelve el nùmero total de elemntos de la serie
def fcount(serie):
    count = 0
    for i in serie:
        count = count + 1
    return(count)

#funcion que devuelve el valor medio de los elemntos de la serie
def favg(serie):
    count = 0
    sum = 0
    for i in serie :
        count = count+1
        sum = sum+i
    avg = sum/count
    return avg
    
#variabe
serie = [1, 54, 6, 78, 9, 123, 5, 4]

#LLamar a las funciones
print("Serie:", serie)
print ("El mayor de los números de la serie:", fmax(serie))
print (f"El mayor de los números de la serie: {fmax(serie)}")
print ("El menor de los números de la serie:", fmin(serie))
print ("El número total de elementos de la serie:", fcount(serie))
print ("Valor medio de los números de la serie:",favg(serie))
