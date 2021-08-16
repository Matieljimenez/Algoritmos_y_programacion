"""
Entradas
cantidad de litros vendidos-->float-->a
Salidas
litros comprados por el cliente-->float-->b
"""
a=float(input("cual es la cantidad de litros de gasolina comprados por el cliente "))
b=(a/3.785)*(3.785*50000)
print("El total a pagar por el cliente es: "+str(b)+" COP")