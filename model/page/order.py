from selene import have, be

from model.user import User
from utils import clear


class Page:
    def __init__(self):
        pass

    def complete_work(self, user: User):
        clear.warning(user)
        user.browser.all('.global-btn-wrapper button.btn').element_by(have.text('Приступить к работе')).click()
        user.browser.all('.global-btn-wrapper button.btn').element_by(have.text('Сохранить')).click()
        user.browser.element("input[type='checkbox']").click()
        user.browser.all('.global-btn-wrapper button.btn').element_by(have.text('Сформировать счет')).click()

    def sign_act_of_work(self, user: User):
        user.browser.element('.global-btn-wrapper button.btn').wait_until(have.text('Подписать акт'))
        clear.warning(user)
        user.browser.element('.global-btn-wrapper button.btn').click()

    def leave_comment(self, user: User):
        user.browser.element('.global-btn-wrapper button.btn').wait_until(have.text('Оставить отзыв'))
        clear.warning(user, force=True)
        user.browser.element('.global-btn-wrapper button.btn').click()
        rate_button = user.browser.all('.gas-secondary-rating button').element_by(have.text('5'))
        rate_button.wait_until(be.clickable)
        rate_button.click()
        user.browser.element("textarea[placeholder='Ваш отзыв']").click().set_value('Отлично! 5 звезд')
        user.browser.all('.btn-wrap button.btn').second.click()

    def send_contract(self, user: User):
        user.browser.element('.global-btn-wrapper  a.btn-link-custom').should(have.text('Передать договор')).click()

    def go_home(self, user: User):
        user.browser.element('.global-btn-wrapper button.btn').should(have.text('На главную')).click()

    def assert_order_status(self, user: User):
        clear.warning(user)
        user.browser.element('.gas-box p.text').should(have.text('Завершен'))
        user.browser.all('.order-details__prices--status span').even.should(have.texts(['Оплачено', 'Оплачено']))
