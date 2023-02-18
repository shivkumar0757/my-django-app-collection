from celery import shared_task
# from staking_status_app.models import StatusCheck
from staking_status_app.dbService import save_staking_log
from staking_status_app.staking_status_service import get_status

from datetime import datetime

@shared_task
def check_and_save_status():
    status = get_status()
    print('in scheduled tasks: ', status[0])
    save_staking_log(status)
    # print('----- saved: ')

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"
