"""
Entradas
sexo-->str-->sexo
edad-->int-->edad
nivel_hemoglobina-->nivel_hemoglobina
Salidas
anemia-->str-->anemia
"""
nivel_hemoglobina=int(input("digite el nivel de hemoglobina del paciente "))
sexo=str(input("digite su sexo (Mujer o Hombre) "))
edad_años=int(input("digite su edad en años sin meses "))
edad_meses=int(input("digite su edad en meses si no tiene años, de lo contrario no ingresar dato "))
sexo_mujer=sexo[0]
sexo_hombre=sexo[0]
edad_años_mujeres=edad_años
edad_años_hombres=edad_años
if (sexo_mujer=="m" or sexo_mujer=="M") and (12<=nivel_hemoglobina<=16) and edad_años_mujeres>=16:
    print("El paciente no tiene Anemia ")
elif (sexo_mujer=="m" or sexo_mujer=="M") and (nivel_hemoglobina>=17) and edad_años_mujeres>=16:
    print("El paciente tiene Anemia ")
elif sexo_hombre=="h" or sexo_hombre=="H" and (14<=nivel_hemoglobina<=18) and edad_años_hombres>=16:
    print("El paciente no tiene Anemia ")
elif sexo_hombre=="h" or sexo_hombre=="H" and nivel_hemoglobina>=19 and edad_años_hombres>=16:
    print("El paciente tiene Anemia ")
elif edad_meses>=0 and edad_meses<=1 and (13<=nivel_hemoglobina<=26):
    print("El paciente no tiene Anemia ")
elif edad_meses>=0 and edad_meses<=1 and nivel_hemoglobina>=27:
    print("El paciente tiene Anemia ")
elif edad_meses>=1 and edad_meses<=6 and (10<=nivel_hemoglobina<=18):
    print("El paciente no tiene Anemia ")
elif edad_meses>=1 and edad_meses<=6 and nivel_hemoglobina>=18:
    print("El paciente tiene Anemia ")
elif edad_meses>=6 and edad_meses<=12 and (11<=nivel_hemoglobina<=15):
    print("El paciente no tiene Anemia ")
elif edad_meses>=6 and edad_meses<=12 and nivel_hemoglobina>=16:
    print("El paciente tiene Anemia ")
elif edad_años>=1 and edad_años<=5 and (11.5<=nivel_hemoglobina<=15):
    print("El paciente no tiene Anemia ")
elif edad_años>=1 and edad_años<=5 and nivel_hemoglobina>=16:
    print("El paciente tiene Anemia ")
elif edad_años>=5 and edad_años<=10 and (12.6<=nivel_hemoglobina<=15.5):
    print("El paciente no tiene Anemia ")
elif edad_años>=5 and edad_años<=10 and nivel_hemoglobina>=15.6:
    print("El paciente tiene Anemia ")
elif edad_años>=10 and edad_años<=15 and (13<=nivel_hemoglobina<=15.5):
    print("El paciente no tiene Anemia ")
elif edad_años>=10 and edad_años<=15 and nivel_hemoglobina>=15.6:
    print("El paciente tiene Anemia ")