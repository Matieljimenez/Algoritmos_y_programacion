"""
Entradas
Nombre_cliente-->str-->nombre_cliente
Valor_compra-->float-->valor_compra
Salidas
nombre_cliente-->str-->nombre_cliente
Valor_compra-->float-->valor_compra
Valor_pagar-->float-->valor_pagar
descuento-->float-->descuento
"""
nombre_cliente=str(input("digite el nombre del cliente "))
valor_compra=float(input("digite el valor de la compra realizada por el cliente "))
if valor_compra<50000:
    valor_pagar=valor_compra
    print(nombre_cliente+" el valor de su compra fue "+str(valor_compra)+" COP el total a pagar es: "+str(valor_pagar)+" COP y No recibe descuento")
elif valor_compra>=50000 and valor_compra<=100000:
    valor_pagar=valor_compra-(valor_compra*0.05)
    print(nombre_cliente+" el valor de su compra fue "+str(valor_compra)+" COP el total a pagar es: "+str(valor_pagar)+" COP y recibio un descuento del 5%")
elif valor_compra>100000 and valor_compra<=700000:
    valor_pagar=valor_compra-(valor_compra*0.11)
    print(nombre_cliente+" el valor de su compra fue "+str(valor_compra)+" COP el total a pagar es: "+str(valor_pagar)+" COP y recibio un descuento del 11%")
elif valor_compra>700000 and valor_compra<=1500000:
    valor_pagar=valor_compra-(valor_compra*0.18)
    print(nombre_cliente+" el valor de su compra fue "+str(valor_compra)+" COP el total a pagar es: "+str(valor_pagar)+" COP y recibio un descuento del 18%")
elif valor_compra>1500000:
    valor_pagar=valor_compra-(valor_compra*0.25)
    print(nombre_cliente+" el valor de su compra fue "+str(valor_compra)+" COP el total a pagar es: "+str(valor_pagar)+" COP y recibio un descuento del 25%")