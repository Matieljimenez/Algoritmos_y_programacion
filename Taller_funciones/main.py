frutas=open('frutas.txt', 'r+')
numeros=open('numeros.txt','r+')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista_eliminada
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemnto:list)->list:
 auxiliar=[]
 for i in lista:
   a=i.replace(elemnto,"")
   auxiliar.append(a)
 return auxiliar
lista_eliminada=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"e")
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas
lista-->list-->lista
Salidas
lista-->list-->lista_copia
"""
def copia_lista(lista:list)->list:
  return lista.copy()
lista_copia=copia_lista(lista_frutas)
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->list-->lista
Salidas
lista-->numeroslist-->numeros_enteros
"""
def numeros_enteros(lista:list)->list:
  auxiliar=[]
  auxiliar_dos=[]
  for i in lista:
    auxiliar.append(float(i))
  for i in auxiliar:
    auxiliar_dos.append(int(i))
  return auxiliar_dos
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista_sin_elemento
"""  
def elimina_elemento_lista(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-->list-->lista
letra-->str-->letra
Salidas
lista-->list-->lista
"""  
def letra(lista:list,letra:str)->list:
  auxiliar=[]
  for i in lista:
    if i[0]==letra:
      auxiliar.append(i)
  return auxiliar
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
"""   
def tamano_lista(lista:list)->int:
  a=len(lista)
  return a
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
tipo-->str-->tipo
"""  
def informacion_lista(lista:list)->int:
  tamaño=len(lista)
  for i in lista:
    d=lista[0]
  tipo=type(d)
  c="Tamaño de la lista: "+str(tamaño)+" Tipo de la lista: "+str(tipo)
  return c
#Retornar una lista con los numero negativos  
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""  
def numeros_negativos(lista):
  auxiliar=[]
  for i in lista:
    if i<0:
      auxiliar.append(i)
  return auxiliar
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas
lista-->list-->lista
Salida
posicion-->str-->elemento
"""
def posicion_elemento(lista:list, elemento:str):
  a=lista.index(elemento)
  return a
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(lista:list, elemento):
  frutas.write("Banano")
  for i in frutas:
    lista_frutas.append(i)
  return lista_frutas
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(lista:list,elemento):
  a=lista.count(elemento)
  return a
if __name__ == "__main__":
  #lista_l elimina un elemento de la lista
  #print(lista_eliminada)

  #copia imprime la copia de una lista
  #print(lista_copia)

  #numeros_enteros imprime los numeros enteros de una lista
  #print(numeros_enteros(lista_numeros))
  
  #lista_sin_elemento imprime los datos de la lista sin un elemento
  #lista_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  #lista_sin_elemento=elimina_elemento_lista(lista_nueva,"Naranja")
  #print(lista_sin_elemento)

  #letra imprime todos los elementos de una lista que empiece con cierta letra
  #print(letra(lista_frutas,"A"))

  #tamano_lista imprime el tamaño de la lista
  #print(tamano_lista(lista_frutas))
  
  #informacion_lista imprime el tamaño de la lista y los tipos de datos
  #print(informacion_lista(lista_frutas))
  
  #numeros_negativos imprime los numeros negativos de una lista
  #print(numeros_negativos(numeros_enteros(lista_numeros)))
  
  #posicion_elemento imprime la posicion de un elemento
  #print(posicion_elemento(lista_frutas, "Fresa"))

