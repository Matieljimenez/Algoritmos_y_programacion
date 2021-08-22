"""
Entradas
Categoria_trabajador-->int-->categoria_trabajador
Salario_bruto_trabajador-->float-->salario_bruto_trabajador
Salidas
Categoria_trabajador-->int-->categoria_trabajador
Nuevo_salario_bruto_trabajador-->float-->nuevo_salario_bruto_trabajador
"""
categoria_trabajador=int(input("digite la categoria del trabajador "))
salario_bruto_trabajador=int(input("digite el salario del trabajador "))
if categoria_trabajador==5:
    nuevo_salario_bruto_trabajador=salario_bruto_trabajador+(salario_bruto_trabajador*0.6)
    print("La categoria del trabajador es: "+str(categoria_trabajador)+", El nuevo salario del trabajador es: "+str(nuevo_salario_bruto_trabajador)+" COP")
elif categoria_trabajador==4:
    nuevo_salario_bruto_trabajador=salario_bruto_trabajador+(salario_bruto_trabajador*0.4)
    print("La categoria del trabajador es: "+str(categoria_trabajador)+", El nuevo salario del trabajador es: "+str(nuevo_salario_bruto_trabajador)+" COP")
elif categoria_trabajador==3:
    nuevo_salario_bruto_trabajador=salario_bruto_trabajador+(salario_bruto_trabajador*0.2)
    print("La categoria del trabajador es: "+str(categoria_trabajador)+", El nuevo salario del trabajador es: "+str(nuevo_salario_bruto_trabajador)+" COP")
elif categoria_trabajador==2:
    nuevo_salario_bruto_trabajador=salario_bruto_trabajador+(salario_bruto_trabajador*0.15)
    print("La categoria del trabajador es: "+str(categoria_trabajador)+", El nuevo salario del trabajador es: "+str(nuevo_salario_bruto_trabajador)+" COP")
elif categoria_trabajador==1:
    nuevo_salario_bruto_trabajador=salario_bruto_trabajador+(salario_bruto_trabajador*0.10)
    print("La categoria del trabajador es: "+str(categoria_trabajador)+", El nuevo salario del trabajador es: "+str(nuevo_salario_bruto_trabajador)+" COP")