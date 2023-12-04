"""
@Nombre del proyecto: Desarrollo de sitio web informativo y de demostración del funcionamiento de un sistema de inteligencia artificial con aplicación al turismo

Desarrollado por estudiantes del Instituto Tecnológico Superior de Guanajuato (ITESG)
para la institución del Centro de Investigación en Matemáticas (CIMAT)

@Asesor externo del proyecto: Adrían Pastor López Monroy
@Asesores internos del proyecto: Angélica González Páramo y Jorge Alberto López Barboza
@Autores del proyecto: Mendoza Salazar Héctor Armando y Ramírez Chávez Alfredo Josué
"""
#Los siguientes módulos sirven para crear los histogramas de cada sitío turísitico de la ciudad, el cual da información dinámica
import dash
from dash import dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
#---------------------------------------------------
import pandas as pd #Pandas es un módulo de manipulación y análisis de datos de código abierto
from dash_app.clasificadorSVM import * #Aquí se importan las funciones creadas por los desarrolladores para usar la clasificación con IA
from joblib import load #Este módulo sirve para llamar al modelo entrenado previamente guardado en un archivo .joblib

#En las siguientes variables se hacen llamar a las opiniones de los sitios, así como de sus etiquetas de clasificación para usarlas en el modelo clasificador
tr_txt = get_data_pk("./static/clasificacion/tr_txt.pckl")
tr_y = get_data_pk("./static/clasificacion/tr_y.pckl")
val_txt = get_data_pk("./static/clasificacion/val_txt.pckl")
val_y = get_data_pk("./static/clasificacion/val_y.pckl")

#-----------------------------------------Creación de los histogramas---------------- 
body = {
        "color": "white",
        "text-align": "center",
        "background-color": "#64293E",
        "display":"inline-block",
        "width":"100%",
        "margin":"0",
        "padding":"0",
        "margin-left": "0",
        "margin-right": "0"
    }

def create_dash_aplication(flask_app, csv, titulo, ruta):
    
    df = pd.read_csv(csv, delimiter = ',')
    
    #Crear una tabla dinámica
    pv = pd.pivot_table(df, index=['Nacional ó Internacional'], columns=["Calificación"], values=['Escala'], aggfunc=sum, fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('Escala', 'Pésimo')], name='Pésimo')
    trace2 = go.Bar(x=pv.index, y=pv[('Escala', 'Malo')], name='Malo')
    trace3 = go.Bar(x=pv.index, y=pv[('Escala', 'Regular')], name='Regular')
    trace4 = go.Bar(x=pv.index, y=pv[('Escala', 'Muy bueno')], name='Muy Bueno') 
    trace5 = go.Bar(x=pv.index, y=pv[('Escala', 'Excelente')], name='Excelente')
    
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=ruta, external_stylesheets=[dbc.themes.LUX])
    
    dash_app.layout = html.Div(style= body, children=[
    html.H1( titulo , style={"color": "white",'textAlign': 'center'}),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4, trace5],
            'layout':
            go.Layout(title='Histograma Estadístico de calificaciones', barmode='group') #barmode='group'
        }),
    html.Br(),
    html.A(children='Haz click aquí para volver a la página anterior', href='/informacion' , style={'text-align': 'center', 'text-decoration':'none',"color": "white", "font-size":"10"}),
    html.Br(),
    html.Br(),
    html.P(children='@Copyright 2023', style={'text-align': 'center', 'text-decoration':'none',"color": "white", "font-size":"10"})
    ])
    
    return dash_app

#-----------------------------------------------------------------------------------------------------

def create_dash_aplication2(flask_app, csv, titulo, ruta):
    
    df = pd.read_csv(csv, delimiter = ',')
    
    #Crear una tabla dinámica
    pv = pd.pivot_table(df, index=['Nacional ó Internacional'], columns=["Calificación"], values=['Escala'], aggfunc=sum, fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('Escala', 'Malo')], name='Malo')
    trace2 = go.Bar(x=pv.index, y=pv[('Escala', 'Regular')], name='Regular')
    trace3 = go.Bar(x=pv.index, y=pv[('Escala', 'Muy bueno')], name='Muy Bueno') 
    trace4 = go.Bar(x=pv.index, y=pv[('Escala', 'Excelente')], name='Excelente')
    
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=ruta, external_stylesheets=[dbc.themes.LUX])
    
    dash_app.layout = html.Div(style= body, children=[
    html.H1( titulo , style={"color": "white",'textAlign': 'center'}),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(title='Histograma Estadístico de calificaciones', barmode='group') #barmode='group'
        }),
    html.Br(),
    html.A(children='Haz click aquí para volver a la página anterior', href='/informacion' , style={'text-align': 'center', 'text-decoration':'none',"color": "white", "font-size":"10"}),
    html.Br(),
    html.Br(),
    html.P(children='@Copyright 2023', style={'text-align': 'center', 'text-decoration':'none',"color": "white", "font-size":"10"})
    ])
    
    return dash_app

#------------------------------------Creación del algoritmo clasificador-------------------------------
def algoritmoClasificador(text1): #Se hace llamar al comentario ingresado al sitio

    test_txt = get_texts(text1) #Se guarda el comentario en una lista vacia para poder manipularlo dentro del clasificador
    
    #A continuación se crean diversas variables para poder hacer el clasificado con el nuevo comentario introducido, además de hacer una comparación con los archivos llamados al inicio de este código
    train = tr_txt + val_txt
    test = test_txt
    labels = tr_y + val_y

    data = train + test
    ntrain = len(train)

    #Se hace el entrenamiento con la función ngrams y se utilizan las variables con la información y etiquetas anteriormente establecidas
    _,_,X_test2 = ngrams(data, labels, ntrain, 2, 2, 2000, donorm = True, verbose = True)
    _,_,X_test3 = ngrams(data, labels, ntrain, 3, 3, 1000,  donorm = True, verbose = True)
    _,_,X_test4 = ngrams(data, labels, ntrain, 4, 4, 3000, donorm = True, verbose = True, analyzer_char = True)    
    _,_,X_test5 = ngrams(data, labels, ntrain, 5, 5, 5000, donorm = True, verbose = True, analyzer_char = True)    
    _,_,X_test6 = ngrams(data, labels, ntrain, 3, 3, 2000, donorm = True, verbose = True, analyzer_char = True)
    _,_,X_test1 = ngrams(data, labels, ntrain, 1, 1, 5000, donorm = True, verbose = True)

    TEST = sp.hstack([X_test1,  X_test2,  X_test3, X_test4, X_test5, X_test6])

    #Esta función manda llamar al modelo ya entrenado para así pasarle la variable TEST con el comentario ingresado en la demostración
    clf = load("./static/clasificacion/modeloClasificadorTurismoCompleto.joblib")

    y_pred = clf.predict(TEST) #Aquí se hace la predicción del comentario, este arrojara 1 si es positivo el comentario, y 0 si es negativo
    
    prediccion = str(y_pred) #Aquí el resultado de la predicción se convierte en un string para poder hacer una validación con un if en el archivo HTML de la demostración
        
    return prediccion #Se regresa el resultado de la predicción convertido en string