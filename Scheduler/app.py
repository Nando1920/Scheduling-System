import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from common import yaml_commons
from jobs.check_pending_blood_tests import notify_blood_tests_pending
from jobs.pickup_job import patient_pickup

config = yaml_commons.load_from_file('config.yml')

app = Flask(__name__)
app.secret_key = config['app_secret_key']

scheduler = BackgroundScheduler()


def register_scheduled_tasks():
    interval_minutes = int(config['interval_minutes'])
    scheduler.add_job(func=patient_pickup, trigger="interval", minutes=interval_minutes)
    scheduler.add_job(func=notify_blood_tests_pending, trigger="interval", minutes=interval_minutes)
    scheduler.start()


if __name__ == '__main__':
    register_scheduled_tasks()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    app.run()
