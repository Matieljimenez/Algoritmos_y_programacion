"""
Entradas
Salario de los vendedores-->float-->a
ingresos del departamento numero uno-->b
ingresos del departamento numero dos-->float-->c
ingresos del departamento numero tres-->float-->d
Salidas
salario nuevo de los empleados del departamento numero uno-->float-->f
salario nuevo de los empleados del departamento numero dos-->float-->g
salario nuevo de los empleados del departamento numero tres-->float-->g
"""
a=float(input("digite el salario que ganan todos los empleados "))
b=float(input("digite la cantidad de ingresos generados por el departamento uno "))
c=float(input("digite la cantidad de ingresos generados por el departamento dos "))
d=float(input("digite la cantidad de ingresos generados por el departamento tres "))
e=(b+c+d)*0.33
if b>e:
    f=a+(a*0.2)
else: f=a
if c>e:
    g=a+(a*0.2)
else: g=a
if d>e:
    h=a+(a*0.2)
else: h=a
print("el salario de los empleados del departamento uno es de "+str(f)+" COP")
print("el salario de los empleados del departamento dos es de "+str(g)+" COP")
print("el salario de los empleados del departamento tres es de "+str(h)+" COP")