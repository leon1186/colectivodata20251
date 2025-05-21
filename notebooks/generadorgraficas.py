import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#GRAPHICS
colors=["#185db3","#0088d1","#00aecb","#00cfab","#86e883","#f9f871"]

#definimos las figuras primero con matplotlib
'''
plt.figure(figsize=(8,5))# base x altura

sns.countplot(x='estado',data=dataFrameAsistencia,palette=colors)
plt.title("cantidad de registros por estados de asistencia")
plt.xlabel("Estado de Asistencia")
plt.ylabel("cantidad de registros")
plt.tight_layout
plt.show()

'''
#GRAFICA DE TORTA
#sirve para mostrar proporciones entre columnas del dataframe(proporcion de estudiantes x medio de trasnporte)

conteoMedioTransporte=dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.2f%%',
    colors=sns.color_palette('Blues'),
)
plt.title("distribucion de estudiantes por medio de transporte ")
plt.tight_layout()
plt.show()


#GRAFICO DE BARRAS AGRUPADAS
#SE APLICA CUANDO HAGO CRUCES EN EL DATAFRAME
#con el size creamos una matriz  en este caso asistir , no asistio con , moto, a pie,moto
#cuando tengo un cruce creando una matriz tengo que contruilro en lista cpara que sea un solo vector
conteoEstadoMedioTranporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTranporte.plot(

    kind='bar',
    figsize=(10,6),
    color=colors,

)

plt.title("registras por estado de asistencia y medio de trasnporte")
plt.xlabel("estado de asitencia")
plt.ylabel("cantidad de registros")
plt.legend(title="medio trasnporte")
plt.tight_layout()
plt.show