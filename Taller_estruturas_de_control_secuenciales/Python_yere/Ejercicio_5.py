"""
Entradas
parcial numero uno-->float-->b
parcialnumero dos-->float-->c
parcial numero tres-->float-->d
examen-->float-->e
trabajo-->float-->f
Salidas
promedio-->float-->g
"""
a=input("Ingrese el valor de sus parciales ").split(" ")
b,c,d=a
b=float(b)
c=float(c)
d=float(d)
e=float(input("Ingrese el valor de su examen final "))
f=float(input("Ingrese el valor de su trabajo final "))
g=((b+c+d)/3)*0.55+e*0.3+f*0.15
print("El promedio final del alumno es "+str(g))