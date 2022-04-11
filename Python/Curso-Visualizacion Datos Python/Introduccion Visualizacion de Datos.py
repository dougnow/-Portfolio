#!/usr/bin/env python
# coding: utf-8

# # Curso de visualizacion de Datos 

# **Estudiante : Richard Douglas Grijalba**
# 
# **Modalidad : virtual**

# ## Este coresponde a un curso de la especialidad de Ciencia Datos con python. Grow up

# In[1]:


1+1


# In[2]:


2*6


# In[3]:


5/8


# In[4]:


import os


# In[5]:


os.getcwd()


# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import matplotlib.ticker as ticker

path = r'C:\Users\Rdouglas\Documents\Python Scripts\curso Grow Up\Visualizacion Datos'
list_orders = pd.read_csv(path+'\List of Orders.csv', sep=';',header=0, index_col=False,
                encoding='latin-1', engine = 'python')
orders_details = pd.read_csv(path+'\Order Details.csv', sep=',', header=0, index_col=False,
                            encoding='latin-1',engine='python')


# In[7]:


list_orders.head()


# In[8]:


orders_details.head()


# ## Transformacion de Datos

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[10]:


import warnings
warnings.filterwarnings("ignore")


# In[11]:


list_orders['Order Date'] = pd.to_datetime(list_orders['Order Date'])  #  para cambiar a formato de fecha


# In[12]:


# unir las bases
df = pd.merge(orders_details, list_orders,
             left_on= 'Order ID',
             right_on= 'Order ID')


# In[13]:


# Creamos las columas de Mes y Año
df['Mes'] = df['Order Date'].dt.month
df['Anio'] = df['Order Date'].dt.year
df.head()


# In[14]:


# **Crear una agrupacion**
df_mes = pd.DataFrame(df.groupby(['Mes'])[['Amount','Quantity']].sum()).reset_index()


# In[15]:


print(df_mes)


# ## 2.4 Crear una carcaza en donde se ubicaran los gráficos

# In[16]:


fig, ax = plt.subplots()
plt.show;


# In[17]:


# Este corresponde a la creación del primer gráfico

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'])
plt.show()


# **Probar tipos de markers**

# In[18]:


#Crear un graico de lineas 
# se va a trabajar los marcadores 'o', 'v', tipo de linea '--', 'None', color = 'r'

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='o')
plt.show()


# In[19]:


#Crear un graico de lineas 
# se va a trabajar los marcadores 'o', 'v', tipo de linea '--', 'None', color = 'r'

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='v')
plt.show()


# In[20]:


#Crear un graico de lineas 
# se va a trabajar los marcadores 'o', 'v', tipo de linea '--', 'None', color = 'r'

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='.')
plt.show()


# In[21]:


#Crear un graico de lineas 
# se va a trabajar los marcadores 'o', 'v', tipo de linea '--', 'None', color = 'r'

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='x')
plt.show()


# In[22]:


#Crear un graico de lineas 
# se va a trabajar los marcadores 'o', 'v', tipo de linea '--', 'None', color = 'r'

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h')
plt.show()


# **Probar tipos de lineas**

# In[23]:


# probar varios tipos de lineas
fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = '--')
plt.show()


# In[24]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = '-.')
plt.show()


# In[25]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':')
plt.show()


# In[26]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':', color = 'r')
plt.show()


# In[27]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':', color = 'b')
plt.show()


# In[28]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':', color = 'g')
plt.show()


# In[29]:


fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':', color = 'g')
plt.show()


# ### Personalizar el grafico de lineas

# In[30]:


# agregando un eje secundario

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'],
       marker='h', linestyle = ':', color = 'b')
ax.plot(df_mes['Mes'],df_mes['Quantity'],
       marker='v', color= 'g')
ax.set_xlabel ('Mes') # nmbre del eje x
ax.set_ylabel ('Venta vs cantidad') # nombre del eje y
ax.set_title('Analisis de Venta y Cantidad por Mes') # agrega el titulo
plt.show()


# ### matplotlib.colors
# b: blue
# 
# g: green
# 
# r: red
# #
# c: cyan
# 
# m: magenta
# 
# y: yellow
# 
# k: black
# 
# w: white    # https://matplotlib.org/2.0.1/api/colors_api.html

# ## Varios graficos en una Figura

# In[31]:


# se desea agregar diferentes graficos en un espacio
fig, ax = plt.subplots(2,1)
plt.show;


# In[32]:


fig, ax = plt.subplots(2,1, sharex = True)

#sharex o sharey = True  esto indica que los eje son iguales o compartidos

ax[0].plot(df_mes['Mes'], df_mes['Amount'],
          marker= '.', linestyle = '-.', color ='b')

ax[1].plot(df_mes['Mes'], df_mes['Quantity'],
          marker='v', linestyle= None, color = 'g')

ax[0].set_ylabel('Sales')
ax[1].set_ylabel('Quantity')
ax[1].set_xlabel('Mes')
plt.show;


# ## 3.5 graficos de dos eje y diferentes escalas

# In[33]:


# los parametros correspondientes a cada uno de los ejes
# invertir ejes , cambiar escalas, cambiar valor de inicio de la escala
# limites de la escala

fig, ax = plt.subplots()

ax.plot(df_mes['Mes'], df_mes['Amount'], color = 'blue')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas', color= 'blue')
ax.tick_params('y', colors = 'blue')
ax2 = ax.twinx()
ax2.plot(df_mes['Mes'], df_mes['Quantity'], color = 'magenta')
ax2.set_ylabel('Cantidad Unidades', color= 'magenta')
ax2.tick_params('y', colors = 'magenta')
plt.show()


# In[34]:


# invertir los ejes  y modificar la escala 

fig, ax = plt.subplots()

ax.plot(df_mes['Mes'], df_mes['Amount'], color = 'blue')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas', color= 'blue')
ax.tick_params('y', colors = 'blue')
ax2 = ax.twinx()
ax2.plot(df_mes['Mes'], df_mes['Quantity'], color = 'magenta')
ax2.set_ylabel('Cantidad Unidades', color= 'magenta')
ax2.tick_params('y', colors = 'magenta')
ax.invert_yaxis()
ax.set_ylim(0,70000) # parametro d eescala
ax2.set_ylim(0,750)
plt.show()


# ## 4.1 Grafico Barras Horizontales

# In[35]:


# Agrupamos categora - ventas - cantidad

df_categoria = pd.DataFrame(df.groupby(['Category'])[['Amount','Quantity']].sum())
df_categoria.head()


# In[36]:


# Graficos de barras horizontales (barras)

fig, ax = plt.subplots()

ax.barh(df_categoria.index, df_categoria['Quantity'])
plt.show()


# ## Grafico Barras Verticales

# In[37]:


fig, ax = plt.subplots()

ax.bar(df_categoria.index, df_categoria['Amount'], label = 'Sales')
ax.legend()
ax.set_ylabel('Ventas por Categoria')
plt.show()


# ## Grafico de Barras Apiladas

# In[38]:


fig, ax = plt.subplots()
ax.bar(df_categoria.index, df_categoria['Amount'], label = 'Sales')
ax.bar(df_categoria.index, df_categoria['Quantity'],
      bottom= df_categoria['Amount'], label = 'Quantity')
ax.legend()
ax.set_ylabel('Ventas por Categoria')
plt.show()


# In[39]:


import warnings
warnings.filterwarnings("ignore")


# In[40]:


fig, ax = plt.subplots()
ax.bar(df_categoria.index, df_categoria['Amount'], label = 'Sales')
ax.bar(df_categoria.index, df_categoria['Quantity'],
      bottom= df_categoria['Amount'], label = 'Quantity')
ax.legend()
ax.set_xticklabels(df_categoria.index, rotation = 45)
ax.set_ylabel('Ventas por Categoria')
fig.savefig('grafico_bar1.png', dpi = 200)
plt.show()


# ## Graficos de Barras con Anotaciones

# In[41]:


# grafico de barras con anotaciones

width = 0.35   # el ancho de las barras
fig, ax = plt.subplots()

x=np.arange(len(df_categoria.index))

rects1= ax.bar(df_categoria.index,df_categoria['Amount'], width, label = 'Sales')
rects2= ax.bar(df_categoria.index,df_categoria['Quantity'], width, label = 'Quantity')
ax.legend()
ax.set_ylabel('Ventas')
ax.set_xlabel('Categorias')
ax.set_title('Grafico Apilado de Ventas y Unidades')
ax.set_xticklabels(df_categoria.index, rotation = 45)
ax.set_xticks(x)

def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor de cada barra  """
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                   xy= (rect.get_x() + rect.get_width()/2, height),
                   xytext = (0,5), 
                   textcoords= 'offset points',
                   ha = 'center', va = 'bottom')

#añadir las etiquetas para cada barra
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()


# In[42]:


# darle un color distinto  a cada barra segun la categoria 
fig, ax = plt.subplots()

ax.bar(df_categoria.index, df_categoria['Amount'], label = 'Sales',color=['blue','red','green'])
ax.set_ylabel('Ventas por Categoria')

plt.show()


# ## Grafico de dispersion

# In[43]:


df.head()


# In[44]:


# segmentar el dataframe en 2  años
df_fecha = pd.DataFrame(df.groupby(['Order Date','Anio'])[['Amount','Quantity']].sum()).reset_index()

per_19= df_fecha[df_fecha['Anio']==2019]
per_18= df_fecha[df_fecha['Anio']==2018]
df_fecha.head()


# In[45]:


# grafio de dispersion

fig, ax = plt.subplots()

ax.scatter(per_18['Quantity'],per_18['Amount'],
          color= 'red', label='2018')
ax.scatter(per_19['Quantity'],per_19['Amount'],
          color= 'blue', label='2019')
plt.show()


# ## Crear Anotaciones en el Grafico de Dispersion

# In[46]:


# grafio de dispersion

fig, ax = plt.subplots()

ax.scatter(per_18['Quantity'],per_18['Amount'],
          color= 'red', label='2018')
ax.scatter(per_19['Quantity'],per_19['Amount'],
          color= 'blue', label='2019')
ax.annotate('Venta Max', xy = (130,14000), xycoords = 'data',
           xytext = (0.8,0.95), textcoords = 'axes fraction',
           arrowprops= dict(facecolor ='black', shrink = 0.05),
           horizontalalignment= 'right', verticalalignment = 'top') # esto modifica la ubicacion de la flecha
ax.set_xlabel('Cantidad')
ax.set_ylabel('Ventas')
ax.legend() # esto agrega la leyenda de los años 
plt.show()


# In[47]:


# grafio de dispersion

# cambiar el fondo del grafico

plt.style.use('default')
plt.style.use('ggplot') # esto agrega el estilo de grafico fondo tipo ggplot
fig, ax = plt.subplots()

ax.scatter(per_18['Quantity'],per_18['Amount'],
          color= 'red', label='2018')
ax.scatter(per_19['Quantity'],per_19['Amount'],
          color= 'blue', label='2019')
ax.annotate('Venta Max', xy = (130,14000), xycoords = 'data',
           xytext = (0.8,0.95), textcoords = 'axes fraction',
           arrowprops= dict(facecolor ='black', shrink = 0.05),
           horizontalalignment= 'right', verticalalignment = 'top')
ax.set_xlabel('Cantidad')
ax.set_ylabel('Ventas')
ax.legend()
plt.show()


# ## Graficos Estilo Boxplot

# In[48]:


plt.style.use('default')

fig, ax = plt.subplots()

ax.boxplot(per_19['Quantity'])
plt.show()


# ## Introduccion a Seaborn

# **Iniciar** con la importacion de un dataset corresponde a estadisticas de los pokemon

# In[49]:


import os
os.getcwd()


# In[50]:



path = r'C:\Users\Rdouglas\Documents\Python Scripts\curso Grow Up\Visualizacion Datos\Video_Games.csv'
video_games= pd.read_csv(path,sep=';',header=0, index_col=False, encoding='latin-1',
                         engine ='python')

path1 = r'C:\Users\Rdouglas\Documents\Python Scripts\curso Grow Up\Visualizacion Datos\Pokemon.csv'
pokemon= pd.read_csv(path1, sep=';',header=0, index_col=False, encoding='latin-1', engine = 'python')


# In[51]:


# eplorar el dataset
#video games
video_games.head()


# In[52]:


video_games.info()


# In[53]:


video_games.describe()


# In[54]:


# Pokemon
pokemon.head()


# In[55]:


pokemon.info()


# In[56]:


pokemon.describe()


# ### Los histogramas
# Los histogramas muestran la forma de sus datos. El eje horizontal muestra sus valores de datos, 
# con cada barra correspondiendo a un rango de valores. El eje vertical muestra cuántos puntos de
# datos tienen valores en el rango de cada barra

# **Una equeña guía de como interpretar los histogramas**
# 
# Paso 1: Evaluar las características clave : Identifique los picos, que son los conglomerados más altos de las barras. Los picos representan los valores más comunes. Evalúe la dispersión de su muestra para entender qué tanto varían sus datos.
# 
# Paso 2: Buscar indicadores de datos inusuales o no normales : Los datos asimétricos y los datos multimodales indican que los datos podrían ser no normales. Los valores atípicos pueden indicar otras condiciones en sus datos.
# 
# Paso 3: Evaluar el ajuste de una distribución: Si su histograma tiene una línea de distribución ajustada, evalúe que tan cerca siguen las alturas de las barras la forma de la línea. Si las barras siguen de cerca la línea de distribución ajustada, entonces los datos se ajustan adecuadamente a la distribución.
# 
# Paso 4: Evaluar y comparar los grupos: Si su histograma tiene grupos, evalúe y compare el centro y la dispersión de los grupos.
# 
# https://support.minitab.com/es-mx/minitab/19/help-and-how-to/graphs/histogram/interpret-the-results/key-results/

# ![image.png](attachment:image.png)

# In[57]:


# Ver distribuciones , primero crear un histograma 
sns.histplot(video_games['Critic_Score'], kde= False, bins= 15, fill= False, element = 'step')
plt.show()

#fill= False quita el color o relleno de las barras
# element = 'step'   quita las lineas divisorias de las barras


# In[58]:


sns.histplot(video_games['Critic_Score'], kde= True) # con la opcion kde= true permite ver la linea
plt.show()


# In[59]:


sns.histplot(pokemon['Attack'], kde= True, color = 'r') # con la opcion kde= true permite ver la linea
plt.show()


# In[60]:


sns.histplot(pokemon['Speed'], kde= True, color = 'gold') # con la opcion kde= true permite ver la linea
plt.show()


# ### Graficos de Densidad

# Un gráfico de densidad visualiza la distribución de datos en un intervalo continuo.
# todo aquello que se dibuje debajo de los curva es el 100% de los datos

# In[61]:


fig, ax = plt.subplots()
sns.distplot(video_games['Critic_Score'])
ax.set(xlabel= 'Puntaje Critico', 
      xlim=(20,100),
      title= 'Video Juegos')
ax.set(ylabel= 'Densidad')
plt.show()

# esta version de grafico será remobida en este paquete y se tendrá que generar de forma diferente


# In[62]:


# para crear el grafico con paquetes recientes
# visualizar la frecuencia de la informacion 

sns.displot(data= video_games['Critic_Score'], kind= 'kde', fill = True)
plt.show()


# In[63]:


sns.displot(data= video_games['Critic_Score'], kind= 'kde', fill = True, color= 'dimgray')
plt.show()


# In[64]:


sns.displot(data= video_games['Critic_Score'], kind= 'kde', fill = True, color= 'springgreen')
plt.show()


# ### Grafico de Enjambre

# In[65]:


pokemon.head()


# In[66]:


#Un gráfico de enjambre es un tipo de gráfico de dispersión que se utiliza para representar valores categóricos
# permite ver la distribucion de los datos

sns.swarmplot(data = pokemon, 
             x= 'Type 1',
             y='Total')
plt.show()


# In[67]:


sns.swarmplot(data = pokemon, 
             x= 'Type 1',
             y='Total',
             s= 3) # agregando el criterio s=3  esto baja la cantidad de los puntos por defaul genera en 5
plt.show()


# ### Grafico de Banda

# In[68]:


# este grafico muestra la distribucion de los datos y pemrite ver los datos
# atipicos

sns.stripplot(data = pokemon,
             x= 'Type 1',
             y= 'Total',
             jitter = True)
plt.show()


# ### Crear Boxplots con SEABORN

# Para ver las paletas predefinidas 
# https://matplotlib.org/stable/gallery/color/named_colors.html

# In[69]:


sns.boxenplot(data = pokemon,
             x= 'Type 1',
             y= 'Total',
             palette= 'Paired')
plt.show()


# In[70]:


sns.boxenplot(data = pokemon,
             x= 'Type 1',
             y= 'Total',
             palette= 'Accent')  # aplicar una variacion a la paleta
plt.show()


# In[71]:


sns.boxenplot(data = pokemon,
             x= 'Type 1',
             y= 'Total',
             palette= 'tab10') # aplicar una variacion a la paleta
plt.show()


# In[72]:


# boxplot

sns.boxplot(data= pokemon,
           x='Type 1',
           y='Total')

plt.show()
plt.clf() # esto permite observar la calidad de la imagen del grafico


# ### Grafico de Violin

# In[73]:


sns.violinplot(data= pokemon,
           x='Type 1',
           y='Total')
plt.show()


# In[74]:


sns.violinplot(data= pokemon,
           x='Type 1',
           y='Total',
              bw = 0.25) # este criterio altera los anchos de los violines
plt.show()


# ## 6.1. Graficos Dinamicos

# In[75]:


## verificar la instalacion de los paquetes necesarios
## pip install bar_chart_race

import bar_chart_race as bcr
from IPython.display import HTML
path = r'C:\Users\Rdouglas\Documents\Python Scripts\curso Grow Up\Visualizacion Datos'
units_sales = pd.read_csv(path+'\Dinamico.csv', sep=';',header=0, index_col=False,
                encoding='latin-1', engine = 'python')

units_sales.set_index('Order Date', inplace=True) # definimos Order Date como indice
units_sales_acum = units_sales.cumsum(axis=0) # se acumulan las ventas por region
units_sales.head()


# In[76]:


units_sales_acum


# In[77]:


# Grafico Dinamico
bcr.bar_chart_race(df= units_sales_acum, filename = None,
                  figsize = (3.5,3), title = 'Venta Acumulada Enero 2014')


# ## Informacion Util 

# ![image.png](attachment:image.png)

# Para ver las paletas predefinidas https://matplotlib.org/stable/gallery/color/named_colors.html

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)
