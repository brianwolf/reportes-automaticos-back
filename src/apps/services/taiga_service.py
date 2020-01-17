from enum import Enum
from uuid import UUID

import pip._vendor.requests as requests

import apps.configs.variables as var
import apps.utils.tareas_util as tareas_util
from apps.configs.loggers import get_logger
from apps.models.errores import AppException
from apps.models.taiga import Filtros
from apps.utils.csv_util import csv_a_diccionario

_TAIGA_HOST = var.get('TAIGA_HOST')
_API_TAIGA_TAREAS = var.get('API_TAIGA_TAREAS')


class Errores(Enum):
    ERROR_API_TAIGA = 'ERROR_API_TAIGA'


def descargar_csv_tareas(uuid: UUID) -> bytes:
    '''
    Descarga el reporte de csv
    '''
    url_completa = _TAIGA_HOST + _API_TAIGA_TAREAS + str(uuid)
    get_logger().info(f'Descargando CSV con url -> {url_completa}')

    respuesta = requests.get(url_completa)

    if not respuesta.ok:
        mensaje = f'El servicio de Taiga no respondio un 200 -> http: {respuesta.status_code}, {respuesta.text}'
        raise AppException(Errores.ERROR_API_TAIGA, mensaje)

    return respuesta.content


def descargar_csv_tareas_diccionario(uuid: UUID) -> dict:
    '''
    Descaga el csv en formato de disccionario
    '''
    contenido = descargar_csv_tareas(uuid)
    return csv_a_diccionario(contenido)


def generar_reporte_json(uuid: UUID, filtros: Filtros) -> dict:
    '''
    Genera un json con el formato de reporte, que es un diccionario 
    con claves iguales a los proyectos y sus valores las tareas de ese proyecto
    '''
    tareas = descargar_csv_tareas_diccionario(uuid)
    tareas = tareas_util.filtrar(tareas, filtros)

    tareas_agrupadas = tareas_util.agrupar_por_proyectos(tareas)

    for proyecto in tareas_agrupadas:
        for clave, valor in proyecto.items():
            proyecto[clave] = tareas_util.filtrar_campos_mostrados(
                valor, filtros.campos_mostrados)

    return tareas_agrupadas
