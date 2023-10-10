import csv
from collections import namedtuple
from datetime import datetime

def leer_entrenos(fichero):
    Entrenos = namedtuple('Entrenos', 'tipo fechaHora ubicacion duracion calorias distancia frecuencia compartido')
    listaValores = [] 
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            tipo = str(linea[0])
            fechaHora = datetime.strptime(linea[1], '%d/%m/%Y %H:%M')
            ubicacion = str(linea[2])
            duracion = int(linea[3])
            calorias = int(linea[4])
            distancia = float(linea[5])
            frecuencia = int(linea[6])
            compartido = parsea_booleano(linea[7])
            tupla = Entrenos(tipo, fechaHora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            listaValores.append(tupla)
    return listaValores

def parsea_booleano(valor):
    return valor == 'S'