"""
Entradas
sueldo base-->float-->a
horas trabajadas-->int-->b
precio por hora-->float-->c
Salida
Sueldo neto-->float-->f
"""
a=float(input("cual es su sueldo base "))
b=int(input("cual es la cantidad de horas trabajadas "))
c=float(input("cual es el precio de cada hora "))
e=a-(a*0.2)
f=(b*c)+e
print("El sueldo neto del trabajador es: "+str(f))