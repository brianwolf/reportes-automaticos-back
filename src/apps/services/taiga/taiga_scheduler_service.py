import json
from datetime import date
from enum import Enum
from typing import List

import requests
from apscheduler.job import Job

import apps.configs.variables as var
import apps.utils.email_util as email_util
import apps.utils.scheduler_util as scheduler_util
from apps.configs.loggers import get_logger
from apps.models.emails import EmailModelo
from apps.models.errores import AppException
from apps.models.taiga import EmailTaiga, ReportesConfig
from apps.services.taiga.taiga_reportes_config_service import \
    obtener_json_config
from apps.services.taiga.taiga_service import generar_reporte_json

_sched = scheduler_util.crear_scheduler()

_EMAIL_ENVIADOR = var.get('EMAIL_ENVIADOR')
_EMAIL_PASS = var.get('EMAIL_PASS')
_GENERADOR_PDF_HOST = var.get('GENERADOR_PDF_HOST')


class Errores(Enum):
    SERVICIO_URL_REPORTE = 'SERVICIO_URL_REPORTE'


def _funcion():
    print('funcion vacia')


def generar_todos_los_reportes_manualmente():
    configs = obtener_json_config()

    for config in configs:
        generar_reporte(config)


def iniciar_proceso_automatico():
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    configs = obtener_json_config()
    get_logger().info(
        f'Iniciando proceso automatico con la siguiente config: {configs}')

    for config in obtener_json_config():
        job = scheduler_util.agregar_job(_sched, _funcion, config.cron,
                                         config.nombre)
        job.args = [config]
        job.func = generar_reporte

    scheduler_util.inciar_scheduler(_sched)


def parar_proceso_automatico():
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    scheduler_util.parar_scheduler(_sched)


def actualizar_proceso_automatico():
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    parar_proceso_automatico()
    iniciar_proceso_automatico()


def generar_reporte(config: ReportesConfig):
    '''
    Genera el reporte pdf y envia el email al finalizar
    '''
    reporte_json = generar_reporte_json(config)

    url_completa = _GENERADOR_PDF_HOST + config.url_generar_reporte
    get_logger().info(f'Ejecutando REST con url -> {url_completa}')
    
    headers = {'content-type': 'application/json'}
    resultado = requests.post(url_completa, data=json.dumps(reporte_json), headers=headers)

    if resultado.status_code != 200:
        mensaje = f'Error servicio generar reporte -> URL: {url_completa}, STATUS: {resultado.status_code}, BODY: {resultado.text}'
        app_exception = AppException(Errores.SERVICIO_URL_REPORTE, mensaje)
        get_logger().error(app_exception.to_dict())
        raise app_exception

    contenido_pdf = resultado.content
    _enviar_email(config, contenido_pdf)


def _enviar_email(config: ReportesConfig, contenido_pdf: bytes):
    '''
    Envia el email para terminar con el proceso
    '''
    nombre_archivo = f'reporte-{config.nombre}-{date.today()}.pdf'
    encabezado = f'Entrega reporte mensual de {config.nombre} a la fecha {date.today()}'
    cuerpo = f'Muy buenos dias, mediante la presente les hago entrega del reporte mensual, saludos cordiales.'

    email_a_enviar = EmailModelo(de=_EMAIL_ENVIADOR,
                                 contrasenia=_EMAIL_PASS,
                                 para=config.email_taiga.destinatarios,
                                 encabezado=encabezado,
                                 cuerpo=cuerpo,
                                 copia=config.email_taiga.copiados,
                                 adjuntos=[(
                                     nombre_archivo,
                                     contenido_pdf,
                                 )])

    email_util.enviar_email(email_a_enviar)
