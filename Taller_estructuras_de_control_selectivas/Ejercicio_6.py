"""
Entradas
dato a-->int-->A
dato b-->int-->B
dato c-->int-->C
dato d-->int-->D
Salidas
numero N-->int-->N
"""
A=int(input("digite el valor del dato A "))
B=int(input("digite el valor del dato B "))
C=int(input("digite el valor del dato C "))
D=int(input("digite el valor del dato D "))
N=int(str(A)+str(B)+str(C)+str(D))
if C>5 and B<9:
    N=(str(A)+str(B+1)+str(C*0)+str(D*0))
    print(N)
elif C>5 and B>=9:
    N=str(A+1)+str(B*0)+str(C*0)+str(D*0)
    print(N)
elif C<5 and B==9:
    N=str(A)+str(B)+str(C*0)+str(D*0)
    print(N)
elif C<5 and B<9:
    N=(str(A)+str(B)+str(C*0)+str(D*0))
    print(N)
elif D>0:
    N=(str(A)+str(B)+str(C)+str(D*0))
    print(N)
else: print(N)