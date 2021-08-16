"""
Entradas
Numero de hombres en el curso-->int-->a
Numero de mujeres en el curso-->int-->b
Salidas
porcentaje de hombres en el salon-->float-->f
porcentaje de mujeres en el salon-->float-->g
"""
a=int(input("cual es el número de hombres en el curso "))
b=int(input("cual es el número de mujeres en el curso "))
c=int(a+b)
d=float(a/c)
e=float(b/c)
f=float(d*100)
g=float(e*100)
print("El porcentaje de los hombres en el salon es: "+str(f)+" %")
print("El porcentaje de las mujeres en el salon es: "+str(g)+" %")