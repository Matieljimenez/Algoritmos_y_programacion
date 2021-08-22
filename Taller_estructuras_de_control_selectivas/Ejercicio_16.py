"""
Entradas
Dato_a-->float-->A
Dato_b-->float-->B
Dato_c-->float-->C
Salidas
valor_D-->float-->D
Equación_utilizar-->float-->equiacion_utilizada
X1-->float-->X1
X2-->float-->X2
"""
A=float(input("digite el valor del dato A "))
B=float(input("digite el valor del dato B "))
C=float(input("digite el valor del dato C "))
D=(B**2)-4*A*C
if D==0:
    X1=X2=-B/(2*A)
    equiacion_utilizada="-B/(2*A)"
    print("La formula utilizada es "+equiacion_utilizada)
    print("X1 vale: "+str(X1)+" y X2 vale: "+str(X2))
elif D>0:
    X1=(-B+((B**2-4*A*C)**0.5))/(2*A)
    X2=(-B-((B**2-4*A*C)**0.5))/(2*A)
    equiacion_utilizada="X1=(­B+SQRT(B**2-­4*A*C))/(2*A) y X2=(­B­-SQRT(B**2-­4*A*C))/(2*A)"
    print("La formula utilizada es "+equiacion_utilizada)
    print("X1 vale: "+str(X1)+" y X2 vale: "+str(X2))
elif D<0:
    print("No tiene solución en los Reales. ")