from enum import Enum
from typing import List

import requests
from apscheduler.job import Job

import apps.configs.variables as var
import apps.utils.scheduler_util as scheduler_util
from apps.configs.loggers import get_logger
from apps.models.errores import AppException
from apps.models.taiga import ReportesConfig, EmailTaiga
from apps.services.taiga.taiga_reportes_config_service import \
    obtener_json_config
from apps.services.taiga.taiga_service import generar_reporte_json

_sched = scheduler_util.crear_scheduler()


class Errores(Enum):
    SERVICIO_URL_REPORTE = 'SERVICIO_URL_REPORTE'


def _funcion():
    print('funcion vacia')


def iniciar_proceso_automatico():
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    for config in obtener_json_config():
        job = scheduler_util.agregar_job(_sched, _funcion,
                                         config.cron, config.nombre)
        job.args = [config]
        job.func = generar_reporte

    scheduler_util.inciar_scheduler(_sched)


def parar_proceso_automatico():
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    scheduler_util.parar_scheduler(_sched)


def actualizar_proceso_automatico(configs: List[ReportesConfig]):
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    parar_proceso_automatico(configs)
    iniciar_proceso_automatico(configs)


def generar_reporte(config: ReportesConfig):
    '''
    '''
    reporte_json = generar_reporte_json(config.uuid_csv, config.filtros)

    resultado = requests.post(
        url=config.url_generar_reporte, params=reporte_json)

    if resultado.status_code != 200:
        mensaje = f'Error servicio generar reporte -> URL: {config.url_generar_reporte}, STATUS: {resultado.status_code}, BODY: {resultado.get_data()}'
        app_exception = AppException(Errores.SERVICIO_URL_REPORTE, mensaje)
        get_logger().error(app_exception.to_dict())
        raise app_exception

    contenido_pdf = resultado.get_data()
    enviar_email(config.email_taiga, contenido_pdf)


def enviar_email(email_taiga: EmailTaiga, contenido_pdf: bytes):
    '''
    '''
    pass
