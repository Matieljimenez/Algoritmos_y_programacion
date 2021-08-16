"""
Entradas
Precio final pagado del producto-->float-->a
precio publico a la venta del producto-->float-->b
Salidas
porcentaje de descuento aplicado al producto-->float-->c
"""
a=float(input("cuanto fue el precio pagado con el descuento al producto "))
b=float(input("cuanto era el precio del producto al publico "))
c=abs(((a/b)*100)-100)
print("El descuento final aplicado al producto es: "+str(c)+" %")