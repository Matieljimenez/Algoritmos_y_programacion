"""
Entradas
Sueldo del trabajador-->float-->a
Salidas
nuevo sueldo del trabajador-->float-->b
"""
a=float(input("digite el sueldo del trabajador "))
if a<900000:
    b=(a*0.15)+a
else: b=(a*0.12)+a
print("el nuevo sueldo del trabajador es "+str(b)+" COP")