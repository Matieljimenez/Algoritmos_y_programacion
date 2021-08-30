a=int(input("dividendo "))
b=int(input("divisor "))
c=1
d=0
e=a%b
print(a)
while (a>b):
    if a>0 and e==0:
        a=a-b
        c=c+1
        print(a)
    elif a>0 and e>0:
        a=a-b
        d=d+1
        print(a)
    elif a==0:
        break
print(e)
if b>0 and e==0:
    print("cociente "+str(c))
    print("residuo "+str(e))
else:
    print("cociente"+str(d))
    print("residuo"+str(e))