"""
Entradas
capital prestado-->float-->a
tiempo de interes-->int-->b
interes-->float-->c
Salidas
porcentaje de interes anual-->float-->d
"""
a=float(input("cual es la cantidad dde dinero prestado "))
b=int(input("cuantos años de interes tiene el prestamo "))
c=float(input("cual es la cantidad total del capital abonado "))
d=(c*100)/(b*a)
print("El procentaje de interes anual es el siguiente "+str(d)+" %")