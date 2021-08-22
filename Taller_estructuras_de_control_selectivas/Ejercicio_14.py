"""
Entradas
lectura_anterio-->int-->lectura_anterior
lectura_actual-->int-->lectura_actual
Salidas
pago-->float-->pago
"""
lectura_anterior=int(input("digite el valor de la lectura anterior del recibo "))
lectura_actual=int(input("digite el valor de la lectura actual del recibo "))
diferencia=abs(lectura_actual-lectura_anterior)
if diferencia>=0 and diferencia<=100:
    pago=diferencia*4.600
    print("El total a pagar por el recibo es: "+str(pago)+" COP")
elif diferencia>=101 and diferencia<=300:
    pago=diferencia*80.00
    print("El total a pagar por el recibo es: "+str(pago)+" COP")
elif diferencia>=301 and diferencia<=500:
    pago=diferencia*100.000
    print("El total a pagar por el recibo es: "+str(pago)+" COP")
elif diferencia>500:
    pago=diferencia*120.000
    print("El total a pagar por el recibo es: "+str(pago)+" COP")