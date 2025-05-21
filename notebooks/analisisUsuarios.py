import pandas as pd

dataFrameUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx")#ojo que si no te lee. borrar el primer punto.
'''
print(dataFrameUsuarios)



print(dataFrameUsuarios["tipo_usuario"].unique())

print(dataFrameUsuarios["especialidad"].unique())
print(dataFrameUsuarios.info())


print(dataFrameUsuarios["especialidad"].unique())



#1. Solo estudiantes
soloEstudiantes=dataFrameUsuarios.query('tipo_usuario=="estudiante"')
print(soloEstudiantes)

#2. Solo profesores

soloDocentes=dataFrameUsuarios.query('tipo_usuario=="docente"')
print(soloDocentes)
#3. Todos excepto estudiantes


#4. Filtrar por especialidad

filtroEspecialidad=dataFrameUsuarios[dataFrameUsuarios['especialidad'].notna()]
print(filtroEspecialidad)
#5. Excluir una especialidad
filtroPorEspecialidad=dataFrameUsuarios[dataFrameUsuarios['especialidad']=="Ingenieria de Sistemas"]
print(filtroPorEspecialidad)
#6. Excluir administrativos
soloAdministrative=dataFrameUsuarios.query('tipo_usuario=="administrativos"')
print(soloAdministrative)

#7. Direcciones en medellin
df_Medellin=dataFrameUsuarios[dataFrameUsuarios['direccion'].str.lower().str.contains('medellin',na=False)]#.contains('medellin',na=False)
print(df_Medellin)

#8. Direcciones terminadas en sur
#df_sur = dataFrameUsuarios[dataFrameUsuarios['direccion'].fillna('').str.lower().str.endswith('sur')]
#rint(df_sur)

#9. Direcciones que inician con calle
df_calle=dataFrameUsuarios[dataFrameUsuarios['direccion'].fillna('').str.lower().str.startswith('calle')]
print(df_calle)

#10.Especialidades que contienen la palabra datos
df_ContieneDatos=dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.lower().str.contains('dato',na=False)]#.contains('medellin',na=False)
print(df_ContieneDatos)

#11. instructores en itagui

df_filtro = dataFrameUsuarios[
    dataFrameUsuarios['especialidad'].notna()  # Filtra direcciones que terminan en 'sur'
    & dataFrameUsuarios['direccion'].str.contains('itagui', case=False, na=False)  # Filtra direcciones que contienen 'Medellín'
]
print(df_filtro)  

'''
#12. nacidos despues de 2000

dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'])

# Filtrar personas nacidas después de 2000
df_nacidos_despues_2000 = dataFrameUsuarios[(dataFrameUsuarios['fecha_nacimiento'] > '2000-01-01')]
print(df_nacidos_despues_2000)


#13. nacidos en los 90

dataFrameUsuarios['fecha_nacimiento']=pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'])
df_nacidos90=dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'].dt.year==1990]
print(df_nacidos90)

#14. direcciones en envigado
#15. especialdiades que empizan por I
#16. usuarios sin direccion
#17. usuarios sin especialidad
#18. profesores que viven en sabaneta
#19. aprendices que viven en bello
#20. nacidos en el nuevo milenio


#1. total por tipo
#2. total por especialidad
#3. cantidad de especialidades distintas
#4. tipos de usuario por especialidad
#5. usuario mas antiguo por tipo
#6. usuario mas joven por tipo
#7. primer registro por tipo
#8. ultimo registro por tipo
#9. combinacion tipo por especialidad
#10. el mas viejo por especialidad
#11. cuantos de cada especialidad por tipo
#12. edad promedio por tipo
#13. años de nacimeinto mas frecuente por especialidad
#14. mes de nacimiento ams frecuente por tipo
#15. UNA CONSULTA O FILTRO QUE UD PROPONGA




#print(dataFrameUsuarios["tipo_usuario"].unique())

#print(dataFrameUsuarios["especialidad"].unique())
#print(dataFrameUsuarios["direccion"].unique())
#print(dataFrameUsuarios.info())

#print(dataFrameUsuarios)

       ######PYTHON COMMANDS#######
#python -m venv modules // aseguramos installar el VIRTUAL ENVIROMETN
#pip install -r paquetes.txt
#pip freeze => para ver si instalamos correctamente los paquetes.
#pip intall seaborn # un paquete especail para graficas.
#pip install matplotlib => para graficas en python.
#pip freeze > paquetes.txt   ===>> especialmetne para actualizar tus librerias puestas en paquetes txt.
#pip freeze ====>> constantemente para checkear las librearias tal cual como git status.