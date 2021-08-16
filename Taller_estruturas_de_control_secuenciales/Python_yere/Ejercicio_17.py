"""
Entradas
monto de dinero presupuestal-->float-->a
Salidas
dinero correspondiente para ginecologia-->float-->b
dinero correspondiente para traumatologia-->float-->c
dinero correspondiente para pediatria-->float-->d
"""
a=float(input("Presupuesto anual al Hospital rural "))
b=a*0.40
c=a*0.30
d=a*0.30
print("El presupuesto del hospital rural para ginecología es: "+str(b))
print("El presupuesto del hospital rural para traumatología es: "+str(c))
print("El presupuesto del hospital rural para pediatría es: "+str(d))