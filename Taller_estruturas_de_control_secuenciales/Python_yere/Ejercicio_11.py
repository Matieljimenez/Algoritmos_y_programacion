"""
Entradas
nombre del trabajador-->str-->a
Sueldo base del trabajador-->float-->b
precio por hora normal del trabajador-->c
horas normales de trabajo realizadas-->int-->d
horas extra de trabajo realizadas-->int-->e
número de actualización academica del trabajador-->int-->f
número de hijos del trabajador-->int-->g
Salidas
asignaciones del trabajador-->float-->j
deducciones del trabajador-->float-->k
sueldo neto del trabajador-->float-->l
"""
a=str(input("Ingrese el nombre del trabajador "))
b=float(input("Ingrese el sueldo base del trabajador "))
c=float(input("Ingrese el valor por hora normal "))
d=int(input("Ingrese la cantidad de horas normales trabajadas "))
e=int(input("Ingrese la cantidad de horas extras trabajadas "))
f=int(input("Ingrese la cantidad de actualizaciones academicas hechas por el trabajador "))
g=int(input("Ingrese la cantidad de hijos del trabajador "))
h=(c*0.25)*e
i=d*c
j=(250000*f)+(173000*g)+180000
k=((b*0.05)+(b*0.02)+(b*0.07))
l=b+j+h+i-k
print("Las asignaciones del trabajador son: "+str(j))
print("Las deducciones del trabajador son: "+str(k))
print("El sueldo neto del trabajador "+str(a)+" en el mes de diciembre es: "+str(l))