"""
Entradas
lectura del recibo anterior-->float-->a
lectura del recibo actual-->float-->b
costo del kilovatio en el recibo-->float-->c
Salidas
total a pagar en el recibo-->floa-->d
"""
a=float(input("Ingrese la lectura anterior del recibo de la luz "))
b=float(input("Ingrese la lectura actual del recibo de la luz "))
c=float(input("Ingrese el valor por kilovatio "))
d=(a*c)+(b*c)
print("El total a pagar en el recibo es: "+str(d))