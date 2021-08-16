"""
Entradas
calificacion del Examen de matematicas-->float-->a
tarea numero uno de matematicas-->float-->c
tarea numero dos de matematicas-->float-->d
tarea numero tres de matematicas-->float-->e
Examen de quimica-->float-->f
tarea numero uno de quimica-->float-->h
tarea numero dos de quimica-->float-->i
Examen de fisica-->float-->j
tarea numero uno de fisica-->float-->l
tarea numero dos de fisica-->float-->m
tarea numero tres de fisica-->float-->n
Salidas
promedio general de las materias-->float-->x
promedio de la materia de matematicas-->float-->q
promedio de la materia de quimica-->float-->t
promedio de la materia de fisica-->float-->w
"""
a=float(input("Ingrese la nota del examen de matematicas "))
b=input("Ingrese las notas de las tres tareas de matematicas ").split(" ")
c,d,e=b
c=float(c)
d=float(d)
e=float(e)
f=float(input("Ingrese la nota del examen de quimica "))
g=input("Ingrese la nota de las dos tareas de quimica ").split(" ")
h,i=g
h=float(h)
i=float(i)
j=float(input("Ingrese la nota del examen de fisica "))
k=input("Ingrese la nota de las tres tareas de fisica ").split(" ")
l,m,n=k
l=float(l)
m=float(m)
n=float(n)
ñ=a*0.9
p=((c+d+e)/3)*0.1
q=ñ+p
r=f*0.85
s=((h+i)/2)*0.15
t=r+s
u=j*0.8
v=((l+m+n)/3)*0.2
w=u+v
x=(q+w+t)/3
print("El promedio de Matematicas es: "+str(q))
print("El promedio de Quimica es: "+str(t))
print("El promedio de Fisica es: "+str(w))
print("El promedio general de las materias es: "+str(x))