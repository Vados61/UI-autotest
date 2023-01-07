from selene import have, be

from model.controls.date_picker import set_tomorrow_date
from model.user import User
from utils import clear


class Page:
    def __init__(self):
        self.order_button_selector = '.text-wrap>button'
        self.next_btn_selector = '.gas-box button'
        self.change_object_btn_selector = '.card-object button'
        self.date_input_selector = '.custom-date>.custom-date__btn'
        self.confirm_date_btn_selector = '.daterangepicker button'
        self.time_input_selector = '.gas-select-wrap'
        self.item_firm_selector = '[id^=company-item-company]'

    def change_order(self, user: User, text):
        user.browser.all(self.order_button_selector).element_by(have.text(text)).click()

    def click_to_next_btn(self, user: User):
        user.browser.element(self.next_btn_selector).click()

    def click_to_change_object_btn(self, user: User):
        user.browser.element(self.change_object_btn_selector).click()

    def set_tomorrow_date(self, user: User):
        user.browser.element(self.date_input_selector).click()
        set_tomorrow_date(user, 'data-date')
        user.browser.all(self.confirm_date_btn_selector).element_by(have.text('Ок')).click()

    def set_time(self, user: User):
        user.browser.element(self.time_input_selector).click()
        user.browser.all(self.time_input_selector + ' .item').first.click()

    def submit_order(self, user: User):
        user.browser.element('.row .btn').should(have.text('Отправить заказ')).click()

    def choose_company(self, user: User, firm_name):
        firm_card = user.browser.all(self.item_firm_selector).element_by(have.text(firm_name))
        firm_card.wait_until(have.text('Выбрать'))
        firm_card.element('button').click()
        user.browser.element('.gas-box .text-center>button').should(have.text('Выбрать')).click()
        user.browser.element("input[placeholder='Номер паспорта']").wait_until(have.value('123456'))
        user.browser.element('.btn-wrap button').should(have.text('Оформить договор')).click()

    def pay_for_order(self, user: User):
        user.browser.all('.col>.logo-wrap').second.click()
        user.browser.element("[name='_do_next']").click()

    def sign_contract_by_sms_code(self, user: User):
        user.browser.all('.code-input input').first.click().type(user.password_from_sms)

    def click_pay_for_order(self, user: User):
        user.browser.all('.recovery-box button.btn').element_by(have.text('К заказу')).click()
        button = user.browser.all('.global-btn-wrapper button.btn').second
        button.wait_until(have.text('Оплатить счет'))
        clear.warning(user)
        # if not button.wait_until(be.clickable):
        #     clear.warning(user)
        button.click()

    def sign_act_of_work(self, user: User):
        button = user.browser.all('.global-btn-wrapper button.btn').second
        button.wait_until(have.text('Подписать акт'))
        clear.warning(user, force=True)
        button.click()
