"""
Entradas
cantidad de naranjas-->int-->a
Precio por docena de las naranjas-->float-->b
ganancias al vender las naranjas-->float-->c
Salidas
porcentaje de ganancias producidas por las naranjas-->float-->e
"""
a=int(input("ingrese la cantidad de naranjas compradas "))
b=float(input("cual es el precio por docena de las naranjas "))
c=float(input("cuales fueron las ganancias producidas al vender las naranjas "))
d=a*(b/12)
e=((c-d)/d)*100
print("El Porcentaje de ganancias producidas por las naranjas es del "+str(e)+" %")