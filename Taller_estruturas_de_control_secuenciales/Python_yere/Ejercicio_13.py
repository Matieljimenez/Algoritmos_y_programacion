"""
Entradas
cantidad de billetes de 50000-->int-->a
cantidad de billetes de 20000-->int-->b
cantidad de billetes de 10000-->int-->c
cantidad de billetes de 5000-->int-->d
cantidad de billetes de 2000-->int-->e
cantidad de billetes de 1000-->int-->f
cantidad de billetes de 500-->int-->g
cantidad de billetes de 100-->int-->h
Salidas
Cantidad de dinero en el banco-->float-->i
"""
a=int(input("cual es la cantidad de billetes de 50000 "))
b=int(input("cual es la cantidad de billetes de 20000 "))
c=int(input("cual es la cantidad de billetes de 10000 "))
d=int(input("cual es la cantidad de billetes de 5000 "))
e=int(input("cual es la cantidad de billetes de 2000 "))
f=int(input("cual es la cantidad de billetes de 1000 "))
g=int(input("cual es la cantidad de billetes de 500 "))
h=int(input("cual es la cantidad de billetes de 100 "))
i=(a*50000)+(b*20000)+(c*10000)+(d*5000)+(e*2000)+(f*1000)+(g*500)+(h*100)
j=(a+b+c+d+e+f+g+h+i)
print("El banco cuenta con la siguente cantidad de dinero: "+str(i)+" con esta cantidad de billetes "+str(j))