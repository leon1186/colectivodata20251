import pandas as pd
#extraer informar y cargar ----analista
#extraer la info 

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")# ./ es suficiente para pararse en la raiz principal sin necesidad ../

#extraer datos basicos de la data ingresada
#print(dataFrameAsistencia.head(100))
    #print(dataFrameAsistencia.tail(50))

#print(dataFrameAsistencia.info())    # / informacion de los campos.desde int a objetos memory
#print(dataFrameAsistencia.describe())#estadisticas
print(dataFrameAsistencia['estrato'].value_counts().head(2))#cada columna se vuelve un diccionario.

#ANTES DE FILTRAR COMO ANALISTA DE DATOS DEBES CONOCER (LA FUENTE PRIMARIA)
#FILTROS Y CONDICIONES PARA TRANSFORMAR DATOS
print(dataFrameAsistencia["estado"].unique())   
print(dataFrameAsistencia["estrato"].unique())
print(dataFrameAsistencia["medio_transporte"].unique())

#1.REPORTAR TODOS LOS ESTUDIANTES QUE ASISTIERON 
estudianteQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')#aqui uso doble comillas porque estoy buscando un string 
print(estudianteQueAsistieron)

#2.REPORTAR TODOS LOS ESTUDIANTE FALTARON
estudiantesQueFaltaron=dataFrameAsistencia.query('estado=="inasistencia"')
print(estudiantesQueFaltaron)
#3,REPORTAR TODOS LOS ESTUDIANTES QUE LLEGARON TARDE(JUSTIFICADO)
estudiantesQueLLegaronTarde=dataFrameAsistencia.query('estado=="justificado"')
print(estudiantesQueLLegaronTarde)
#4.REPORTAR TODOS LOS ESTUDIANTES DE ESTRATO 1
estudianteEstratoUno=dataFrameAsistencia.query('estrato==1')
print(estudianteEstratoUno)

#5.REPORTAR TODOS LOS ESTUDIANTESDE ESTRATO ALTO 
print(dataFrameAsistencia['estrato'].value_counts())

#6.REPORTAR TODOS LOS ESTUDIANTES QUE LLEGAN EN METRO
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
print(estudiantesQueUsanMetro)


#7.REPORTAR TODOS LOS ESTUDIANTES QUE LLEGAN EN BICICLETA
estudiantesBicicleta= dataFrameAsistencia.query('medio_transporte=="bicicleta"')
print(estudiantesBicicleta)



#8.REPORTAR TODOS LOS ESTUDIANTES QUE NO CAMINAN PARA LLEGAR A LA UNIVERSIDAD.
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')


#9.REPORTAR TODOS LOS REGISTROS DE ASISTENCIA DEL MES DE JUNIO.




# Convert 'fecha' to datetime
dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'], errors='coerce')

# Filter: March dates and estado == 'asistio'
march_asistio_june = dataFrameAsistencia[(dataFrameAsistencia['fecha'].dt.month == 3)&(dataFrameAsistencia['estado'] == 'asistio')]

# Show result
print(march_asistio_june)



#10.REPORTAR TODOS LOS ESTUDIANTES QUE FALTARON Y USAN BUS PARA LLEGAR A LA UNIVERSIDAD.
estuiantesQueFaltanyUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
print(estuiantesQueFaltanyUsanBus)
print(estuiantesQueFaltanyUsanBus.info())#info me dice exactamente cuantos estudiantes son.



#11.REPORTAR TODOS LOS ESTUDIANTES QUE USAN BUS Y SON DE ESTRATOS ALTOS

estudiantesQueEstratoAltoyUsanBus=dataFrameAsistencia[(dataFrameAsistencia['medio_transporte']=='bus')&(dataFrameAsistencia['estrato'].isin([4,5]))]

print(estudiantesQueEstratoAltoyUsanBus)
count=len(estudiantesQueEstratoAltoyUsanBus)
print(f'total of {count} que usan bus y son estratos altos')


#12.REPORTAR TODOS LOS ESTUDIANTES QUE USAN BUS Y SON DE ESTRATOS BAJOS

estudiantesEstratosBajosyUsanBus=dataFrameAsistencia[(dataFrameAsistencia['medio_transporte']=='bus')&(dataFrameAsistencia['estrato'].isin([1,2]))]
count1=len(estudiantesEstratosBajosyUsanBus)
print(estudiantesEstratosBajosyUsanBus)
print(f'total of {count1} que usan bus y son estratos bajos')
'''
#13.REPORTAR TODOS LOS ESTUDIANTES QUE LLEGAN TARDE Y SON DE ESTRATO 3,4,5,O 6


#14.REPORTAR TODOS LOS ESTUDIANTES QUE USAN TRANSPORTES ECOLOGICOS
#15.REPORTAR TODOS LOS ESTUDIANTES QUE FALTAN Y USAN CAROO PARA TRANSPORTARSE
#16. REPORTAR TODOS LOS ESTUDIANTES QUE ASISTEN SON ESTRATOS ALTOS Y CAMINAN
#17.REPORTAR TODOS LOS ESTUDIANTES QUE SON ESTRATOS BAJOS Y JUSTIFICAN SU INASISTENCIA
#19.REPORTAR TODOS LOS ESTUDIANTES QUE USAN CARRO Y JUSTIFICAN SU INASISTENCIA
#20.REPORTAR TODOS LOS ESTUDIANTES QUE FALTAN Y USAN METRO Y SON ESTRATOS MEDIOS




#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. CONTAR CADA REGISTRO DE ASISTENCIA POR CADA ESTADO
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()#.sum(),.value_counts()-->subconjuntos, .size() tamano de como los quiero agrupar
print(conteoRegistrosPorEstado)
#2. NUMERO DE REGISTROS POR ESTRATO.(ASISTENCIAS INASISTENCIAS JUSTIFICADAS POR ESTRATO)

conteoRegistroPorEstrato=dataFrameAsistencia.groupby('estrato').size()
print(conteoRegistroPorEstrato)
#3. CANTIDAD DE ESTUDIANTES POR MEDIO DE TRANSPORTE.
#4. CANTIDAD DE REGISTRO POR GRUPO.
#5. CRUCE ENTRE ESTADO Y MEDIO DE TRSNPORTE.
cruceEstadoMediotransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
print(cruceEstadoMediotransporte)
#6. PROMEDIO DE ESTRATO POR ESTADO DE ASISTENCIA.
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)
#7.ESTRATO PROMEDIO POR MEDIO DE TRANSPORTE.
#8.MAXIMO ESTRATO POR ESTADO DE ASISTENCIA.
#9.MINIMO ESTRATO POR ESTADO DE ASISTENCIA.
#10.CONTEO DE ASISTENCIAS POR GRUPO Y POR ESTADO.
#11.TRASPORTE USADO POR CADA GRUPO.
#12.CUANTOS GRUPOS DISTINTOS REGISTRARON ASISTENCIA POR FECHA
#13 PROMEDIO DE ESTRATO POR FECHA.
#14.NUMERO DE TIPOS DE ESTADO POR TRANSPORTE
#15.PRIMER REGSITRO DE CADA GRUPO 
'''


print(dataFrameAsistencia["estado"].unique())
print(dataFrameAsistencia["estrato"].unique())
print(dataFrameAsistencia["medio_transporte"].unique())