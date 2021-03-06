import json
import os
from datetime import date
from enum import Enum
from typing import List

import requests
from apscheduler.job import Job

import apps.configs.lector_variables as var
import apps.utils.email_util as email_util
import apps.utils.git_util as git_util
import apps.utils.scheduler_util as scheduler_util
from apps.configs.loggers import get_logger
from apps.configs.variables import Var
from apps.models.emails import EmailModelo
from apps.models.errores import AppException
from apps.models.taiga import EmailTaiga, ReportesConfig
from apps.services.taiga.taiga_reportes_config_service import \
    obtener_json_config
from apps.services.taiga.taiga_service import generar_reporte_json

_sched = scheduler_util.crear_scheduler()

_EMAIL_ENVIADOR = var.get(Var.EMAIL_ENVIADOR)
_EMAIL_PASS = var.get(Var.EMAIL_PASS)
_GENERADOR_PDF_HOST = var.get(Var.GENERADOR_PDF_HOST)


class Errores(Enum):
    SERVICIO_GENERAR_REPORTE = 'SERVICIO_GENERAR_REPORTE'


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

    try:
        headers = {'content-type': 'application/json'}
        resultado = requests.post(url_completa,
                                  data=json.dumps(reporte_json),
                                  headers=headers)
    except Exception as e:
        mensaje = 'Error desconocido en el servicio de para generar el reporte'
        get_logger().error(mensaje, exc_info=True)
        get_logger().exception(e)
        raise AppException(Errores.SERVICIO_GENERAR_REPORTE, mensaje)

    if resultado.status_code != 200:
        mensaje = f'Error servicio generar reporte -> URL: {url_completa}, STATUS: {resultado.status_code}, BODY: {resultado.text}'
        raise AppException(Errores.SERVICIO_GENERAR_REPORTE, mensaje)

    contenido_reporte = resultado.content

    _enviar_email(config, contenido_reporte)
    _guardar_reporte_en_git(config, contenido_reporte)


def _enviar_email(config: ReportesConfig, contenido_reporte: bytes):
    '''
    Envia el email para terminar con el proceso
    '''
    encabezado = f'Entrega de reporte mensual de {config.nombre} a la fecha {date.today()}'
    cuerpo = f'Muy buenos dias, mediante la presente les hago entrega del reporte mensual, saludos cordiales.'

    email_a_enviar = EmailModelo(de=_EMAIL_ENVIADOR,
                                 contrasenia=_EMAIL_PASS,
                                 para=config.email_taiga.destinatarios,
                                 encabezado=encabezado,
                                 cuerpo=cuerpo,
                                 copia=config.email_taiga.copiados,
                                 adjuntos=[(
                                     _nombre_reporte_final(config),
                                     contenido_reporte,
                                 )])

    email_util.enviar_email(email_a_enviar)


def _nombre_reporte_final(config: ReportesConfig) -> str:
    '''
    Devuelve el nombre del reporte
    '''
    return f'{date.today()} - {config.nombre}.md'


def _guardar_reporte_en_git(config: ReportesConfig, contenido_reporte: bytes):
    '''
    Guarda el reporte en git clonando el proyecto, creando el archivo de reporte,
    commiteando y pusheando
    '''
    repo = git_util.clonar_repo_git(config.git)
    get_logger().info(
        f'Repo clonado en la ruta: {repo.working_dir} con la url: {config.git.url_repo}')

    nombre_reporte = _nombre_reporte_final(config)
    ruta_reporte = os.path.join(repo.working_dir, nombre_reporte)

    with open(ruta_reporte, 'wb') as reporte_archivo:
        reporte_archivo.write(contenido_reporte)

    mensaje_commit = f'Se sube reporte de forma automatica con nombre: {nombre_reporte}'
    git_util.pushear_a_master(repo, mensaje_commit)

    git_util._borrar_carpeta_si_existe(repo.working_dir)
