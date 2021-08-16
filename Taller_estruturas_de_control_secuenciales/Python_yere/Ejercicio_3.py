"""
Entradas
Sueldo-->float-->a
ventas realizadas-->int-->b
Salidas
ganancias por ventas-->float-->c
Sueldo mas las Comiciones-->float-->d
"""
a=float(input("Ingrese su sueldo "))
b=int(input("Ingrese el numero de ventas realizadas "))
c=b*(a*0.1)
d=a+c
print("Las ganancias por ventas son: "+str(c))
print("Su sueldo final es: "+str(d))