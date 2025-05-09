#calculo de sueldo segun horas trabajadas
def computepay (fhoras, ftarifa):
    if fhoras >= 40:
      print("Este es tu sueldo")
      pay = (ftarifa * fhoras)
      return pay
    else:
        paganormal =40*ftarifa
        horasextras=(fhoras-40)*ftarifa*1.5
        pay=horasextras+paganormal
        return pay

#END FUNCION

#MAIN
while True:
    shoras = input("Introcude el número de horas curradas esta week: ")
    try:
        fhoras = float(shoras)
        break
    except:
        print("Perdona, mete un número")


while True:
    starifa = input("Mete tu tarifa: ")
    try:
        ftarifa = float(starifa)
        break
    except:
        print("Dime tu sueldooo")
        



pay = computepay(fhoras, ftarifa)
print(pay)
print("Que poco cobras!!!!")


