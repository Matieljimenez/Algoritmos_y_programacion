while True:
    a=input().split(" ")
    b, c=a
    b=int(b)
    c=int(c)
    if (b<=3 and b>0 and c<=2**32-1 and c>=10):
        d=c*b
        print(d)
    elif b==0 and c==0:
        break