from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


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
    scheduler.start(paused=True)


def remover_job(scheduler: BackgroundScheduler, id: str):
    '''
    Crea el scheduler que se va a utilizar 
    '''
    return scheduler.remove_job(id)


def agregar_job(scheduler: BackgroundScheduler, funcion: function, cron: str,
                id: str):
    '''
    Agrega un job al scheduler mediante una funcion y un cron
    '''
    return scheduler.add_job(funcion, CronTrigger.from_crontab(cron), id=id)
