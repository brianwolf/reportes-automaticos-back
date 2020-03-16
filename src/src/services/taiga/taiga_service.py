from datetime import date
from enum import Enum
from uuid import UUID

import pip._vendor.requests as requests

import src.configs.lector_variables as var
from src.configs.variables import Var
import src.utils.tareas_util as tareas_util
from src.configs.loggers import get_logger
from src.models.errores import AppException
from src.models.taiga import Filtros, ReportesConfig
from src.utils.csv_util import csv_a_diccionario

_TAIGA_HOST = var.get(Var.TAIGA_HOST)
_API_TAIGA_TAREAS = var.get(Var.API_TAIGA_TAREAS)
_API_TAIGA_SUB_TAREAS = var.get(Var.API_TAIGA_SUBTAREAS)


class Errores(Enum):
    ERROR_API_TAIGA = 'ERROR_API_TAIGA'


def _descargar_csv(url_completa: str) -> bytes:
    '''
    Descargar el csv de la pagina de taiga mediante un GET pasandole la URL
    '''
    get_logger().info(f'Descargando CSV con url -> {url_completa}')

    respuesta = requests.get(url_completa)

    if not respuesta.ok:
        mensaje = f'El servicio de Taiga no respondio un 200 -> http: {respuesta.status_code}, {respuesta.text}'
        raise AppException(Errores.ERROR_API_TAIGA, mensaje)

    return respuesta.content


def descargar_csv_tareas(uuid: UUID) -> bytes:
    '''
    Descarga el reporte de csv
    '''
    url_completa = _TAIGA_HOST + _API_TAIGA_TAREAS + str(uuid)
    return _descargar_csv(url_completa)


def descargar_csv_sub_tareas(uuid: UUID) -> bytes:
    '''
    Descarga el reporte de csv
    '''
    url_completa = _TAIGA_HOST + _API_TAIGA_SUB_TAREAS + str(uuid)
    return _descargar_csv(url_completa)


def descargar_csv_tareas_diccionario(uuid: UUID) -> dict:
    '''
    Descaga el csv de tareas en formato de diccionario
    '''
    contenido = descargar_csv_tareas(uuid)
    return csv_a_diccionario(contenido)


def descargar_csv_sub_tareas_diccionario(uuid: UUID) -> dict:
    '''
    Descaga el csv de sub tareas en formato de diccionario
    '''
    contenido = descargar_csv_sub_tareas(uuid)
    return csv_a_diccionario(contenido)


def generar_reporte_json(config: ReportesConfig) -> dict:
    '''
    Genera el reporte con la configuracion enviada
    '''
    proyectos = generar_reporte_proyectos_json(config.uuid_tareas,
                                               config.uuid_sub_tareas,
                                               config.filtros)

    return {
        'titulo': config.nombre,
        'fecha': str(date.today()),
        'proyectos': proyectos
    }


def generar_reporte_proyectos_json(uuid_tareas: UUID, uuid_sub_tareas: UUID,
                                   filtros: Filtros) -> dict:
    '''
    Genera un json con el formato de reporte, que es un diccionario 
    con claves iguales a los proyectos y sus valores las tareas de ese proyecto
    '''
    tareas = descargar_csv_tareas_diccionario(uuid_tareas)
    tareas = tareas_util.filtrar(tareas, filtros.tareas)

    subtareas = descargar_csv_sub_tareas_diccionario(uuid_sub_tareas)
    subtareas = tareas_util.filtrar_sub_tareas(subtareas, filtros.subtareas)

    tareas = tareas_util.agrupar_tareas_con_sub_tareas(tareas, subtareas)

    tareas_agrupadas = tareas_util.agrupar_por_proyectos(tareas)

    for proyecto in tareas_agrupadas:

        for tarea in proyecto['tareas']:
            tarea[tareas_util.
                  _CLAVE_SUB_TAREAS] = tareas_util.filtrar_campos_mostrados(
                      tarea[tareas_util._CLAVE_SUB_TAREAS],
                      filtros.subtareas.campos_mostrados)

        proyecto['tareas'] = tareas_util.filtrar_campos_mostrados(
            proyecto['tareas'], filtros.tareas.campos_mostrados)

    return tareas_agrupadas
