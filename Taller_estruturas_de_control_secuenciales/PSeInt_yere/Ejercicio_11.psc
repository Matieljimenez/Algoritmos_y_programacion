Algoritmo Ejercicio_11
	Escribir "cual es el nombre del trabajador "
	leer a
	Escribir "cual es el sueldo base del trabajador "
	leer b
	Escribir "cual es el valor por hora normal "
	leer c
	Escribir "cual es la cantidad de horas normales trabajadas "
	leer d
	Escribir "cual es la cantidad de horas extras trabajadas "
	leer e
	Escribir "cual es la cantidad de actualizaciones academicas hechas por el trabajador "
	leer f
	Escribir "cual es la cantidad de hijos que tiene el trabajador "
	leer g
	h=(c*0.25)*e
	i=d*c
	j=(250000*f)+(173000*g)+180000
	k=((b*0.05)+(b*0.02)+(b*0.07))
	l=b+j+h+i-k
	escribir "Las asignaciones del trabajador son: " j 
	escribir "Las deducciones del trabajador son: " k
	escribir "El sueldo neto del trabajador es " a " en el mes de diciembre es: " l
FinAlgoritmo