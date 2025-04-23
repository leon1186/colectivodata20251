import pandas as pd

#extraer la info 

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")# ./ es suficiente para pararse en la raiz principal sin necesidad ../

#extraer datos basicos de la data ingresada

    #print(dataFrameAsistencia.head(100))
    #print(dataFrameAsistencia.tail(50))

#print(dataFrameAsistencia.info())    # / informacion de los campos.desde int a objetos memory
#print(dataFrameAsistencia.describe())#estadisticas
print(dataFrameAsistencia['estrato'].value_counts().head(2))#cada columna se vuelve un diccionario.
