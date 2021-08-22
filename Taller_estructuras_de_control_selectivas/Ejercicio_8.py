"""
Entradas
Valor_P-->int-->P
Valor_Q-->int-->Q
Salidas
satisfaccion_expresion-->int-->expresion
"""
print("Se determinara si dos valores satisfacen la siguiente expresión P**3+Q**4-2*P**2>680")
P=int(input("digite el valor de P "))
Q=int(input("digite el valor de Q "))
expresion=(P**3)+(Q**4)-2*(P**2)>680
if expresion==True:
    print(str(P)+" y "+str(Q)+" satisfacen la expresión")
else: print(str(P)+" y "+str(Q)+" no Satisfacen la expresión")