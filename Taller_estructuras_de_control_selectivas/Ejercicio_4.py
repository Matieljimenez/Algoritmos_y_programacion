"""
Entradas
total del monto a pagar por la compra-->float-->a
Salidas
cantidad de dinero pagado por la empresa-->float-->b
cantidad de dinero a pagado por el fabricante-->float-->c
cantidad de dinero a pagar por intereses al fabricante-->float-->d
cantidad de dinero pagado por el banco en prestamo-->float-->e
"""
a=float(input("digite la cantidad de dinero a pagar por la comprada de las piezas "))
if a>5000000:
    b=a*0.55
    e=a*0.3
    c=a*0.15
    d=c*0.2
    print("la cantidad pagada de los fondos de la empresa es de "+str(b)+" COP")
    print("la cantidad prestada por el banco es de "+str(e)+" COP")
    print("la cantidad pagada por el fabricante es de "+str(c)+" COP")
    print("la cantidad total por pagar al fabricante de intereses del 20 % es de "+str(d)+" COP")
elif a<=5000000:
    b=a*0.7
    c=a*0.3
    d=c*0.2
    print("la cantidad pagada de los fondos de la empresa es de "+str(b)+" COP")
    print("la cantidad pagada por el fabricante es de "+str(c)+" COP")
    print("la cantidad total por pagar al fabricante de intereses del 20 % es de "+str(d)+" COP")