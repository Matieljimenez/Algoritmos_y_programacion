Algoritmo Inicio_invertir_dos_numero
	Escribir 'Escribe el primer número de dos cifras para ser invertido'
	Leer a
	Escribir 'Escribe el segundo número de dos cifras para ser invertido'
	Leer b
	c<-Subcadena(a,0,0)
	d<-Subcadena(a,1,1)
	e<-Subcadena(b,0,0)
	f<-Subcadena(b,1,1)
	Escribir 'El primer número invertido es: ' d c
	Escribir 'El segundo número invertido es: ' f e
	Escribir 'Los dos números juntos son: ' a b
	Escribir 'Los dos números invertidos juntos son: ' f e d c
FinAlgoritmo
