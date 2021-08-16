Algoritmo Ejercicio_21
	Escribir 'Ingrese el valor del producto para pago de contado '
	Leer a
	Escribir 'Ingrese la cantidad de cuotas '
	Leer b
	c <- (a/b)
	Si b<12 Entonces
		d <- c*0.1
		Escribir 'El porcentaje que se cobra por cada cuota es 10 % y coresponde a ',d,' COP por Cuota'
	SiNo
		d <- c*0.15
		Escribir 'El porcentaje que se cobra por cada cuota es 15 % y coresponde a ',d,' COP por Cuota'
	FinSi
FinAlgoritmo
