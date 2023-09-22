'''
TODO:

Vamos a sacar información de un sitio web que muestra la tabla de clasificatorias CONCACAF para el Mundial de Qatar

Primero, hay que importar las librerías necesarias para incluirlas en nuestro proyecto

Definimos la URL del sitio al que queremos realizar el scraping

Hay que guardar el contenido del sitio web en una variable en memoria utilizando la librería requests

Cuando obtenemos el contenido de la página, creamos una "sopa" con el contenido y con el atributo "html.parser" para indicar que vamos a sacar información de un sitio web
El resultado de la "sopa" lo genera la librería bs4

Ahora hay que buscar todos los elementos que cumplan con las características que buscamos extraer

Los elementos encontrados los tenemos que pasar a una lista, así será más fácil trabajar con la información

Un buen consejo es eliminar posibles espacios en blanco que puedan venir del sitio web. Además, cuando se trabajen con datos numéricos, es debido hacer la conversión al tipo de dato correcto

Se puede hacer un filtro para mostrar una cantidad específica de datos

Para obtener los puntos de cada equipo, se puede repetir la misma operación, ahora con las etiquetas y elementos correspondientes en el sitio web

Ya tenemos toda la información lista. Ahora podemos generar una Tabla para que se pueda entender mejor la información
Para esto, definimos una nueva variable que va a implementar el método de la librería Panda.
Este método necesita dos elementos: 1. La lista de equipos y sus puntos correspondientes 2. Inicio y fin del índice que enumera cada registro

La tabla se genera con la instrucción pd.DataFrame({"Equipo": equipos, "Puntos": puntos}, index=list(range(1, 6)))

Esta tabla se puede guardar en un archivo
df.to_excel("Clasificacion.xlsx", index=False) -> guarda en formato excel
df.to_csv("Clasificacion.csv", index=False) -> guarda en formato csv

Una buena manera de apreciar el resultado, es generando gráficos de barras o de cualquier tipo. Así será más fácil entender los datos mostrados
Para eso se pueden utilizar las instrucciones:

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6)) # Se crea una nueva figura

plt.bar(df['Equipo'], df['Puntos'])     # Se indican los datos para los ejes (x,y)
plt.xlabel('Equipo')                    # Se dan títulos a los ejes
plt.ylabel('Puntos')
plt.title('Puntos de los 5 primeros equipos en la clasificación de la CONCACAF Qatar 2023')

plt.xticks(rotation=45)         # Se da un estilo a las etiquetas del eje x, que se vea una rotación de 45 grados

plt.tight_layout()          # Se acomoda la figura automáticamente para que se muestren bien los datos
plt.show()          # Se muestra el resultado

'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://us.as.com/resultados/futbol/clasificacion_mundial_concacaf/clasificacion/?omnil=mpal"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

teams_data = soup.find_all("span", class_="nombre-equipo")
equipos = []

count = 0       # Llevemos un contador para mostrar un número especifico de equipos

for i in teams_data:
    if count < 5:       # Cuantos equipos quiero mostrar
        equipos.append(i.text.strip())  # Quitamos posibles espacios en blanco que hagan ruido innecesario
    else:
        break
    count += 1

score_data = soup.find_all("td", class_="destacado")
puntos = []

count = 0

for i in score_data:
    if count < 5:
        puntos.append(int(i.text.strip()))  # Contemplar el cambio de tipo porque los puntos son datos numéricos. Int es el tipo de dato numérico en Python
    else:
        break
    count += 1

df = pd.DataFrame({"Equipo": equipos, "Puntos": puntos}, index=list(range(1, 6)))

plt.figure(figsize=(10, 6))
plt.bar(df['Equipo'], df['Puntos'])     # Se indican los datos para los ejes (x,y)
plt.xlabel('Equipo')                    # Se dan títulos a los ejes
plt.ylabel('Puntos')
plt.title('Puntos de los 5 primeros equipos en la clasificación de la CONCACAF Qatar 2023')

plt.xticks(rotation=45)         # Se da un estilo a las etiquetas del eje x, que se vea una rotación de 45 grados

plt.tight_layout()          # Se acomoda la figura automáticamente para que se muestren bien los datos
plt.show()          # Se muestra el resultado
