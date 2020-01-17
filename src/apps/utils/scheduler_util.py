from typing import Callable

from apscheduler.triggers.cron import CronTrigger
from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler

_MAX_HILOS_POR_JOB = 3


def crear_scheduler() -> BackgroundScheduler:
    '''
    Crea el scheduler que se va a utilizar 
    '''
    return BackgroundScheduler()


def parar_scheduler(scheduler: BackgroundScheduler):
    '''
    Crea el scheduler que se va a utilizar 
    '''
    scheduler.shutdown(wait=False)


def inciar_scheduler(scheduler: BackgroundScheduler):
    '''
    Crea el scheduler que se va a utilizar 
    '''
    scheduler.start()


def remover_job(scheduler: BackgroundScheduler, id: str) -> Job:
    '''
    Crea el scheduler que se va a utilizar 
    '''
    return scheduler.remove_job(id)


def agregar_job(scheduler: BackgroundScheduler, funcion: Callable, cron: str,
                id: str) -> Job:
    '''
    Agrega un job al scheduler mediante una funcion y un cron
    '''
    job = scheduler.add_job(funcion, CronTrigger.from_crontab(cron), id=id)
    job.modify(max_instances=_MAX_HILOS_POR_JOB)

    return job
