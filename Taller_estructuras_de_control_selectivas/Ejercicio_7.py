"""
Entradas
Kilometros-->int-->a
Salidas
pagos de los clientes-->float-->b
"""
a=int(input("digite la cantidad de Kilometros "))
if a<=300:
    b=50000
    print("Al cliente le corresponde pagar "+str(b)+" COP")
elif a>300 and a<1000:
    b=70000+((a-300)*30000)
    print("Al cliente le corresponde pagar "+str(b)+" COP")
elif a>1000:
    b=150000+((a-1000)*9000)
    print("Al cliente le corresponde pagar "+str(b)+" COP")