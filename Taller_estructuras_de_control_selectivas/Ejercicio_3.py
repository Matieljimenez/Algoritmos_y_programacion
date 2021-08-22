"""
Entradas
valor del dato a-->int-->a
valor del dato b-->int-->b
valor del dato c-->int-->c
valor del dato d-->int-->d
Salidas
Resultado de la primera expresión-->int-->e
Resultado de la segunda expresión-->float-->f
"""
a=int(input("digite el dato a "))
b=int(input("digite el dato b "))
c=int(input("digite el dato c "))
d=int(input("digite el dato d "))
if d==0:
    e=(a-c)**2
    print("el resultado de la primera expresion es "+str(e))
elif d>0:
    f=float(((a-b)**3)/d)
    print("el resultado de la segunda expresion es "+str(f))
else: print("sin respuesta")