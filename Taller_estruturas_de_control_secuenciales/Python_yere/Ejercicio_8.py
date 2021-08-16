"""
Entradas
lado a del triangulo-->float-->a
lado b del triangulo-->float-->b
lado c del triangulo-->float-->c
Salidas
area del triangulo-->float-->e
"""
a=float(input("cual es la longitud del lado A del triangulo "))
b=float(input("cual es la longitud del lado B del triangulo "))
c=float(input("cual es la longitud del lado c del triangulo "))
d=float((a+b+c)/2)
e=float((d*(d-a)*(d-b)*(d-c))**0.5)
print("El area del triangulo es: "+str(e))