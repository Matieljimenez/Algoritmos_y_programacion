"""
Entradas
cantidad de metros a convertir-->float-->a
Salidas
pies equivalentes en metros-->float-->c
pulgadas equivalentes en metros-->float-->b
"""
a=float(input("Ingrese la cantidad de metros a convertir "))
b=float(a*39.37)
c=float(b/12)
print("Esa cantidad equivale a "+str(b)+" Pulgadas")
print("Esa cantidad equivale a "+"{:.4f}".format(c)+" Pies")