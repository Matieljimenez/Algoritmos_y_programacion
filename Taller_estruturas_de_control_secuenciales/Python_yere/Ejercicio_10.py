"""
Entradas
chelines austriacos-->float-->a
dracmas griegos-->float-->b
pesetas-->float-->c
Salidas
pesetas-->float-->d
francos franceses-->float-->e
dolares-->float-->f
liras italianas-->float-->g
"""
a=float(input("cual es la cantidad de chelines austriacos que serán convertidos a pesetas "))
b=float(input("cual es la cantidad de dracmas griegos que serán convertidos a francos franceses "))
c=float(input("cual es la cantidad de pesetas que serán covertidas a dólares y liras italianas "))
d=a*(956.871/100)
e=(b*(88.607/100))/20.110
f=c/122.499
g=c/(9.289/100)
print("El equivalente de los chelines austriacos es: "+str(d)+" pesetas")
print("El equivalente de los dracmas griegos es: "+str(e)+" francos franceses")
print("El equivalente de las pesetas es: "+str(f)+" dolares y "+str(g)+" liras italianas")