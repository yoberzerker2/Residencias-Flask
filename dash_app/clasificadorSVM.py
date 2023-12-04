"""
@Nombre del proyecto: Desarrollo de sitio web informativo y de demostración del funcionamiento de un sistema de inteligencia artificial con aplicación al turismo

Desarrollado por estudiantes del Instituto Tecnológico Superior de Guanajuato (ITESG)
para la institución del Centro de Investigación en Matemáticas (CIMAT)

@Asesor externo del proyecto: Adrían Pastor López Monroy
@Asesores internos del proyecto: Angélica González Páramo y Jorge Alberto López Barboza
@Autores del proyecto: Mendoza Salazar Héctor Armando y Ramírez Chávez Alfredo Josué
"""

import pickle #Este módulo implementa protocolos binarios para serializar y deserializar una estructura de objetos de Python.
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer #Es una biblioteca de aprendizaje automático de software gratuito para el lenguaje de programación Python.
from sklearn.feature_selection import SelectKBest, chi2 #Es una biblioteca de aprendizaje automático de software gratuito para el lenguaje de programación Python.
import scipy.sparse as sp #SciPy es una biblioteca libre y de código abierto para Python. Se compone de herramientas y algoritmos matemáticos.
import numpy as np 
import pandas as pd

#Esta función solo guarda texto en una lista vacía
def get_texts(path_corpus):
    tr_txt = []
    tr_txt.append(path_corpus)
    return tr_txt

#Esta función obtiene datos de un fichero binario
def get_data_pk(file):
    fichero = open(file,'rb')
    lista = pickle.load(fichero)
    fichero.close()
    return lista

#Esta función obtiene datos de un archivo csv, solo de la columna de opinión
def get_texts_from_file(path_corpus):
    tr_txt = []
        
    datos = pd.read_csv(path_corpus, header=0)
    tr_txt = list(datos['Opinión'])
            
    return tr_txt

#Esta función hace los ngramas de los comentarios de los datos de las opiniones de los sítios turísticos de la ciudad
def ngrams(data, labels, ntrain, mn, mx, nm, binary = False, donorm = False, stopwords = False, verbose = True, analyzer_char = False):
        f = data
        
        ftrain = f[:ntrain]
        ftest  = f[ntrain:]
        y_train = labels[:ntrain]
        
        analyzer_type = 'word'
        if analyzer_char:
            analyzer_type = 'char'
            
        if binary:
            vectorizer = CountVectorizer(max_n=mx,min_n=mn,binary=True)
        elif stopwords:
            vectorizer = TfidfVectorizer(max_n=mx,min_n=mn,stop_words='english',analyzer=analyzer_type,sublinear_tf=True)
        else:
            vectorizer = TfidfVectorizer(ngram_range=(mn,mx),sublinear_tf=True,analyzer=analyzer_type,lowercase=True)
        
        X_train = vectorizer.fit_transform(ftrain)
        X_test = vectorizer.transform(ftest)

        y = np.array(y_train)    
        
        numFts = nm
        if numFts < X_train.shape[1]:
            ch2 = SelectKBest(chi2, k=numFts)
            X_train = ch2.fit_transform(X_train, y)
            X_test = ch2.transform(X_test)
            assert sp.issparse(X_train)        

        return X_train, y, X_test