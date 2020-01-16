import apps.configs.variables as var
import apps.utils.scheduler_util as scheduler_util
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apps.models.tareas import ReportesConfig
from apscheduler.job import Job
from apps.services.taiga_service import generar_reporte_json
from typing import List

_sched = scheduler_util.crear_scheduler()


def iniciar_proceso_automatico(configs: List[ReportesConfig]):
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    for config in configs:
        job = scheduler_util.agregar_job(_sched, generar_reporte_json,
                                         config.cron, config.nombre)
        job.args = [config.filtros]

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
    parar_proceso_automatico()
    iniciar_proceso_automatico(configs)
