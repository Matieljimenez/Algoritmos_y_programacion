from io import open
#imprima la posicion de colombia
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print("La posición de colombia es "+str(c))
archivo.close()
"""
#Imprima todos los paises
"""
archivo=open("paises.txt","r")
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
archivo.close()
"""
#Imprima todas las Capitales
"""
#Nota: si está sección del código es ejecutada más de una vez va a generar errores
#con una vez es sufuciente de lo contrario modificar el archivo paises.txt para
#eliminar el ultimo cambio de linea y solucionar el problema
archivo=open("paises.txt","a")
archivo.write("\n")
archivo.close()
#fin de la nota
archivo=open("paises.txt","r")
lista=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista.append(i[r])
    a="".join(lista)
  print(a)
  lista=[]
archivo.close()
"""
#Imprimir todos los paises que inicien con la letra C
"""
archivo=open("paises.txt","r")
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
archivo.close()
"""  
#imprima todas las capitales que inicien con la leta B
"""
#nota: si el archivo paises.txt no tiene ha ejecutado antes el codigo de las capitales
#no ha creado el cambio de linea y generará error
archivo=open("paises.txt","a")
archivo.write("\n")
archivo.close()
#si este codigo se genera más de una vez presentará error y habrá que eliminar el ultimo
#cambio de linea generado en el archivo paises.txt
#fin de la nota
archivo=open("paises.txt","r")
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)
archivo.close()
"""
#Cuente e imprima cuantas ciudades inician con la letra M  
"""
archivo=open("paises.txt","r")
lista=[]
ciudad=[]
c=0
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
    c=c+1
print("La cantidad de ciudades que inicia con la (M) son: "+str(c))
archivo.close()
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
archivo=open("paises.txt","r")
print("Las ciudades que inician con la letra (U) son: ")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
archivo.close()
archivo=open("paises.txt","r")
print("Los paises que inician con la letra (U) son: ")
lista_paises=[]
paises=[]
for o in archivo:
  a=o.index(":")
  for r in range(0,a):
    lista_paises.append(o[r])
  a="".join(lista_paises)
  paises.append(a)
  lista_paises=[]
for o in paises:
  if(o[0]=="U"):
    print(o)
archivo.close()
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
archivo=open("paises.txt","r")
lista=[]
c=0
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
  c=c+1
lista_cantidad=[]
for i in archivo:
  lista_cantidad.append(i)
  a=" ".join(lista_cantidad)
  c=c+1 
  if(a=="\n"):
    break
  lista=[]   
print("El total de paises en el archivo es: "+str(c))
archivo.close()
"""
#Busque e imprima la ciudad de Singapur
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print("La posición de la ciudad Singapur es "+str(c))
archivo.close()
archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Singapur"):
    print("La ciudad de "+str(i))
archivo.close()
"""
#Busque e imprima el pais de Venezuela y su capital
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print("La posición del pais de Venezuela es "+str(c))
print(a)
archivo.close()
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
archivo=open("paises.txt","r")
lista_paises=[]
paises=[]
c=0
for o in archivo:
  a=o.index(":")
  for r in range(0,a):
    lista_paises.append(o[r])
  a="".join(lista_paises)
  paises.append(a)
  lista_paises=[]
for o in paises:
  if(o[0]=="E"):
    c=c+1
print("Los "+str(c)+" paises que inician con la letra (E) tienen ")
print("Las "+str(c)+" siguientes Ciudades")

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Quito"):
    print("1. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="El Cairo"):
    print("2. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="San Salvador"):
    print("3. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Abu Dabi"):
    print("4. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Asmara"):
    print("5. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Bratislava"):
    print("6. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Liubliana"):
    print("7. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Madrid"):
    print("8. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Washington D C"):
    print("9. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Tallin"):
    print("10. La ciudad de "+str(i))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Adís Abeba"):
    print("11. La ciudad de "+str(i))
archivo.close()

archivo.close()
"""
#Busque e imprima la Capital de Colombia
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print("La posición de la Capital de Colombia es "+str(c))
archivo.close()

archivo=open("paises.txt","r")
lista_ciudad=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index("\n")
  for r in range(a+2,b):
    lista_ciudad.append(i[r])
  a="".join(lista_ciudad)
  ciudad.append(a)
  lista_ciudad=[]
for i in ciudad:
  if(i=="Bogotá"):
    print("La capital de colombia es "+str(i))
archivo.close()
"""
#imprima la posicion del pais de Uganda
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
archivo.close()
"""
#imprima la posicion del pais de Mexico
"""
archivo=open("paises.txt","r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
archivo.close()
"""
#Modificar el error que hay en la lista
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, 
ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo.
Utilice un For para cambiar ese Dato
"""
"""
archivo=open("paises.txt","r+")
lista_texto=archivo.readlines()
lista_texto[108]="Madagascar: Antananarivo\n"
archivo.seek(0)
archivo.writelines(lista_texto)
archivo.close()
"""
#Agregue un país que no esté en la lista 
"""
archivo=open("paises.txt","r+")
lista_texto=archivo.readlines()
lista_texto.insert(134,"Países Bajos: Holanda\n")
a="".join(lista_texto)
print(a)
archivo.close()
"""
#Nota todos los codigos fueron probados en replit.com