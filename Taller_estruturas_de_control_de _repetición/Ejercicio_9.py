a=0
b=0
c=0
d=0
while True:
    a=input("")
    if (a=="1"):
          b=b+1
    elif (a=="2"):
            c=c+1
    elif  (a=="3"):
            d=d+1
    elif (a=="4"):
            break
print("MUITO OBRIGADO")
print("Alcool: "+str(b))
print("Gasolina: "+str(c))
print("Diesel: "+str(d))