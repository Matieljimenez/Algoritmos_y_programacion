"""
Entradas
cantidad_dinero-->int-->cantidad_dinero
Salidas
dinero_desglosado-->int-->dinero_desglosado
"""
canitad_dinero=int(input("digite la cantidad de dinero a desglosar "))
bi100mil=int(canitad_dinero/100000)
bi50mil=int((canitad_dinero%100000)/50000)
bi20mil=int(((canitad_dinero%100000)%50000)/20000)
bi10mil=int((((canitad_dinero%100000)%50000)%20000)/10000)
bi5mil=int(((((canitad_dinero%100000)%50000)%20000)%10000)/5000)
bi2mil=int((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)/2000)
bimil=int(((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)%2000)/1000)
mo500=int((((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)%2000)%1000)/500)
mo200=int(((((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)/200)
mo100=int((((((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)/100)
mo50=int(((((((((((canitad_dinero%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)%100)/50)
dinero_desglosado=(str(bi100mil)+" Billete de 100 mil, "+str(bi50mil)+" Billete de 50 mil, "+str(bi20mil)+" Billetes de 20 mil, "+str(bi10mil)+" Billete de 10 mil, "+str(bi5mil)+" Billete de 5 mil, "+str(bi2mil)+" Billetes de 2 mil, "+str(bimil)+" Billete de mil, "+str(mo500)+" moneda de 500, "+str(mo200)+" monedas de 200, "+str(mo100)+" moneda de 100, "+str(mo50)+" moneda de 50")
print(dinero_desglosado)