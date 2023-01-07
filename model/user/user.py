from dataclasses import dataclass

from selene import Browser

from utils import sms_manager


@dataclass
class User:
    first_name: str
    last_name: str
    patronymic: str
    email: str
    phone_number: int
    password: str
    browser: Browser
    last_sms: dict = None
    order_num: str = None
    password_from_sms: str = None
    firm_name: str = None

    def wait_new_sms(self, seconds=40):
        self.last_sms = sms_manager.get_new_sms(self.phone_number, seconds)
        return self.last_sms

    def get_order_num_from_last_sms(self):
        if self.last_sms:
            self.order_num = self.last_sms['text'].split()[2]
        return self.order_num

    def get_last_sms(self):
        self.last_sms = sms_manager._get_last_sms(sms_manager._get_number_id(self.phone_number))

    def get_pass_from_sms(self):
        password = self.last_sms['text'].split()[-1]
        if len(password) != 6:
            self.wait_new_sms()
            assert self.last_sms is not None
            password = self.last_sms['text'].split()[-1]
        self.password_from_sms = password
