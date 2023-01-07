import datetime
import time

from smsactivate.api import SMSActivateAPI

from utils import config

sa = SMSActivateAPI(config.APIKEY)


def _get_number_id(number):
    number = str(number)
    for item in sa.getRentList()['values'].values():
        if item['phone'] == number:
            return item['id']


def _get_sms_count(number_id):
    return sa.getRentStatus(number_id)['quantity']


def _get_last_sms(number_id):
    return sa.getRentStatus(number_id)['values']['0']


def get_new_sms(number, seconds):
    number_id = _get_number_id(number)
    start_sms_count = _get_sms_count(number_id)
    start_time = datetime.datetime.now()
    timer = datetime.datetime.now() - start_time
    while timer < datetime.timedelta(seconds=seconds):
        current_sms_count = _get_sms_count(number_id)
        if current_sms_count > start_sms_count:
            return _get_last_sms(number_id)
        timer = datetime.datetime.now() - start_time
        time.sleep(0.5)
