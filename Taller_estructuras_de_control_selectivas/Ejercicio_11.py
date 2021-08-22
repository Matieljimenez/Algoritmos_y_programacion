"""
Entradas
Temperatura-->float-->temperatura
Salidas
deporte_realizar-->str-->deporte
"""
temperatura=float(input("digite la cantidad de °Fahrenheit "))
if temperatura<=10:
    deporte="Marcha"
    print("El deporte apropiado para practicar es: "+str(deporte))
elif temperatura>10 and temperatura<=32:
    deporte="Esquí"
    print("El deporte apropiado para practicar es: "+str(deporte))
elif temperatura>32 and temperatura<=70:
    deporte="Golf"
    print("El deporte apropiado para practicar es: "+str(deporte))
elif temperatura>70 and temperatura<=85:
    deporte="Tenis"
    print("El deporte apropiado para practicar es: "+str(deporte))
elif temperatura>85:
    deporte="Natación"
    print("El deporte apropiado para practicar es: "+str(deporte))