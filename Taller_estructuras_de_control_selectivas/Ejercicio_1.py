"""
Entradas
Dinero invertido en el banco-->float-->a
procentaje del banco por inversion-->float-->b
Salidas
ganancias generadas en total de dinero-->float-->e
"""
a=float(input("digite la cantidad de dinero que invirtio en el banco "))
b=float(input("digite la cantidad del porcentaje aplicado por el banco "))
c=b/100
d=c*a
e=d+a
if d>=100000:
    print("si puede reinvertir su dinero de nuevo ")
else: print("no puede reinvertir su dinero de nuevo ")
print("Las ganancias producidas por el banco son de "+str(e)+" COP")