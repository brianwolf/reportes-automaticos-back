import csv
import os

DIRECTORIO_TMP = '/tmp/'


def csv_a_diccionario(csv_contenido: bytes) -> dict:
    '''
    Convierte los bytes correspondientes a un CSV a un diccionario de python
    '''
    ruta_archivo_tmp = DIRECTORIO_TMP + 'temp_csv.csv'

    resultado = []
    with open(ruta_archivo_tmp, 'wb+') as archivo_python:
        archivo_python.write(csv_contenido)

    reader = csv.reader(open(ruta_archivo_tmp, 'r'))

    encabeazados = []
    for fila in reader:
        if reader.line_num == 1:
            encabeazados = fila
        else:
            resultado.append(_generar_diccionario(encabeazados, fila))

    os.remove(ruta_archivo_tmp)
    return resultado


def _generar_diccionario(encabezados: list, datos: list):

    resultado = {}
    for i in range(len(encabezados)):

        clave = encabezados[i]
        valor = datos[i]
        resultado[clave] = valor

    return resultado
