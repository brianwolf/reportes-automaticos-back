from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def intervalo():
    print("intervalo")


def cronos():
    print("cron")


def con_parametros(nombre: str):
    print(f"hola {nombre}")


sched = BackgroundScheduler()

job1 = sched.add_job(intervalo, 'interval', seconds=1, id='id')
job1 = job1.modify(max_instances=2)
# job1.args = ['lobezZzno']
# job1.func = con_parametros

# job2 = sched.add_job(cronos, CronTrigger.from_crontab('* * * * *'), id='id2')

sched.start()
