"""
Entradas
valor del producto a contado-->float-->a
cantidad de cuotas-->int-->b
Salidas
porcentaje cobro por cuotas-->float-->d
"""
a=float(input("Ingrese el valor del producto para pagar de contado "))
b=int(input("Ingrese la cantidad de cuotas a financiar del producto "))
c=(a/b)
if b<12:
    d=c*0.1
    print("El porcentaje que se cobra por cada cuota es 10 % y coresponde a "+str(d)+" COP por Cuota")
else:
    d=c*0.15
    print("El porcentaje que se cobra por cada cuota es 15 % y coresponde a "+str(d)+" COP por Cuota")