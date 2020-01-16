from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import time

def job_function():
    print("Hello World")


# sched = BlockingScheduler()
sched = BackgroundScheduler()


# sched.add_job(job_function, CronTrigger.from_crontab('21 17 * * *'), id='id')
sched.add_job(job_function, 'interval', seconds=5, id='id')

sched.start()


time.sleep(5)
# sched.remove_job('id')

time.sleep(5)