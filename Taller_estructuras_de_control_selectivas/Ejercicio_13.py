"""
Entradas
Fecha_nacimiento-->int-->fecha_nacimiento
Salidas
signo_zodiacal-->str-->signo_zodiacal
edad-->int-->edad
"""
fecha_nacimiento=input("digite su fecha de nacimiento completa separada por (/) y el año debe contener 4 números ").split("/")
dia, mes, año=fecha_nacimiento
dia=int(dia)
mes=int(mes)
año=int(año)
if dia>=22 and mes==11 or dia<=21 and mes==12:
    edad=2021-año
    print("Tú signo zodiacal es Sagitario")
    print("Tú edad es "+str(edad)+" años")
elif dia>=22 and mes==12 or dia<=20 and mes==1:
    edad=2021-año
    print("Tú signo zodiacal es Capricornio")
    print("Tú edad es "+str(edad)+" años")
elif dia>=21 and mes==1 or dia<=19 and mes==2:
    edad=2021-año
    print("Tú signo zodiacal es Acuario")
    print("Tú edad es "+str(edad)+" años")
elif dia>=20 and mes==2 or dia<=19 and mes==3:
    edad=2021-año
    print("Tú signo zodiacal es Pisis")
    print("Tú edad es "+str(edad)+" años")
elif dia>=21 and mes==3 or dia<=20 and mes==4:
    edad=2021-año
    print("Tú signo zodiacal es Aries")
    print("Tú edad es "+str(edad)+" años")
elif dia>=21 and mes==4 or dia<=21 and mes==5:
    edad=2021-año
    print("Tú signo zodiacal es Tauro")
    print("Tú edad es "+str(edad)+" años")
elif dia>=22 and mes==5 or dia<=21 and mes==6:
    edad=2021-año
    print("Tú signo zodiacal es Géminis")
    print("Tú edad es "+str(edad)+" años")
elif dia>=22 and mes==6 or dia<=22 and mes==7:
    edad=2021-año
    print("Tú signo zodiacal es Cáncer")
    print("Tú edad es "+str(edad)+" años")
elif dia>=23 and mes==7 or dia<=23 and mes==8:
    edad=2021-año
    print("Tú signo zodiacal es Leo")
    print("Tú edad es "+str(edad)+" años")
elif dia>=24 and mes==8 or dia<=22 and mes==9:
    edad=2021-año
    print("Tú signo zodiacal es Virgo")
    print("Tú edad es "+str(edad)+" años")
elif dia>=23 and mes==9 or dia<=22 and mes==10:
    edad=2021-año
    print("Tú signo zodiacal es Libra")
    print("Tú edad es "+str(edad)+" años")
elif dia>=23 and mes==10 or dia<=21 and mes==11:
    edad=2021-año
    print("Tú signo zodiacal es Escorpión")
    print("Tú edad es "+str(edad)+" años")