"""
@Nombre del proyecto: Desarrollo de sitio web informativo y de demostración del funcionamiento de un sistema de inteligencia artificial con aplicación al turismo

Desarrollado por estudiantes del Instituto Tecnológico Superior de Guanajuato (ITESG)
para la institución del Centro de Investigación en Matemáticas (CIMAT)

@Asesor externo del proyecto: Adrían Pastor López Monroy
@Asesores internos del proyecto: Angélica González Páramo y Jorge Alberto López Barboza
@Autores del proyecto: Mendoza Salazar Héctor Armando y Ramírez Chávez Alfredo Josué
"""

#El siguiente código es muy importante debido a que es el motor principal de establecimiento de rutas del sistema web y el renderizado de los archivos html

#Librerías principales para el correcto funcionamiento del sistema web
from flask import Flask , request #Framework principal para el sistema web
from flask import render_template #Módulo principal para el renderizado de los archivos html
from dash_app import create_dash_aplication, create_dash_aplication2, algoritmoClasificador #Módulo creado por los desarrolladores en donde se crean funciones enfocadas en funciones principales del sistema, estas se encuentran en la carpeta dash_app
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #Módulo enfocado en el cálculo de los parámetros de los sentimientos
from nltk.sentiment.vader import SentimentIntensityAnalyzer #Módulo enfocado en el cálculo de los parámetros de los sentimientos
from nltk.corpus import stopwords #Módulo necesario para analizar los parámetros de los sentimientos
from deep_translator import GoogleTranslator #Módulo usado para la traducción de los comentarios ingresados en la demostración del sitio web
import nltk #Módulo enfocado en importar herramientas para el lenguaje


#nltk.download('vader_lexicon')

app = Flask(__name__)

#Rutas de las paginas principales del sitio web
@app.route("/")
def index():
    return render_template("./sitio/index.html") #Renderizado del archivo HTML para que se pueda mostrar en web

@app.route("/informacion")
def info():
    return render_template("./sitio/informacion.html") #Renderizado del archivo HTML para que se pueda mostrar en web

@app.route("/informacion2")
def infor():
    return render_template("./sitio/informacion2.html") #Renderizado del archivo HTML para que se pueda mostrar en web

#**********************Ruta con funcion del demo************************
#Se llama primero la funcion de la pagina estaticas

#nltk.download('stopwords') --> Se puede usar después

@app.route('/demo')
def demo():
    return render_template('./sitio/demo.html')

#Se llama a la funcion demo_post al momento de que el usuario interacciona
@app.route("/demo", methods=['POST'])
def demo_post():

    stops_word = set(stopwords.words('english'))

    traductor = GoogleTranslator(source='es', target='en') #Objeto para poder traducir de español a íngles, ya que la parte de los parámetros de los sentimientos analiza mejor en idioma íngles

    text1 = traductor.translate(request.form['text1'].lower()) #Se traduce el comentario introducido en el demo
    
    textEs = request.form['text1'] #Se almacena el comentario en español introducido en el demo
    
    text_final = ''.join(c for c in text1 if not c.isdigit()) #Se verifica y se filtra el comentario para hacer el análisis de sentimientos
  
    processed_doc1 = ' '.join([word for word in text_final.split() if word not in stops_word])

    sa = SentimentIntensityAnalyzer() #Se crea el objeto para dar los parámetros de los sentimientos
    dd = sa.polarity_scores(text=processed_doc1) #Se crea una nueva variable para guardar los parámetros de los sentimientos
    compound = round((1 + dd['compound'])/2, 2) #Se redondean los parámetros dados anteriormente
    
    prediccion_ok = algoritmoClasificador(textEs) #Se hace uso del clasificador creado por los programadores en el comentario en español

    return render_template("./sitio/demo.html", prediccion = prediccion_ok , final=compound, text1=textEs,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu']) #Se renderiza la página del demo y se pasan los valores calculados en las funciones anteriores para visualizarlos en los resultados de la demostración


#Las siguientes funciones crean los histogramas alojados en la página de información, hacen uso de los archivos que se compartieron en las sesiones con el asesor externo----------------------------------------------
create_dash_aplication(app, "./static/ubicaciones/alhondiga.csv", "Estadísticas de la Alhondiga: Clasificación dividida en Nacional ó Internacional","/dashBoardAlhondiga/")

create_dash_aplication2(app, "./static/ubicaciones/teatroJuarez.csv", "Estadísticas del Teatro Juárez: Clasificación dividida en Nacional ó Internacional","/dashBoardTeatroJuarez/") 

create_dash_aplication(app, "./static/ubicaciones/basilicaColegiata.csv", "Estadísticas de la Basílica Colegiata: Clasificación dividida en Nacional ó Internacional","/dashBoardBasilica/")

create_dash_aplication(app, "./static/ubicaciones/callejonBeso.csv", "Estadísticas del Callejón del Beso: Clasificación dividida en Nacional ó Internacional","/dashBoardCallejonBeso/")

create_dash_aplication(app, "./static/ubicaciones/casa_diego_rivera.csv", "Estadísticas de la Casa de Diego Rivera: Clasificación dividida en Nacional ó Internacional","/dashBoardCasaDiego/")

create_dash_aplication2(app, "./static/ubicaciones/jardinUnion.csv", "Estadísticas del Jardín Unión: Clasificación dividida en Nacional ó Internacional","/dashBoardJardinUnion/") 

create_dash_aplication(app, "./static/ubicaciones/mercado_hidalgo.csv", "Estadísticas del Mercado Hidalgo: Clasificación dividida en Nacional ó Internacional","/dashBoardMercadoHidalgo/")

create_dash_aplication(app, "./static/ubicaciones/monumentoPipila.csv", "Estadísticas del Monumento al Pípila: Clasificación dividida en Nacional ó Internacional","/dashBoardPipila/")

create_dash_aplication(app, "./static/ubicaciones/museoMomias.csv", "Estadísticas del Museo de las Momias: Clasificación dividida en Nacional ó Internacional","/dashBoardMomias/")

create_dash_aplication(app, "./static/ubicaciones/universidadGuanjauto.csv", "Estadísticas de la Universidad de Guanajuato: Clasificación dividida en Nacional ó Internacional","/dashBoardUniversidad/")

#Aquí se hace llamda a la aplicación y hace que funcione localmente
if __name__ == "__main__":
    app.run()