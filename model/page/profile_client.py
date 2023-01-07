from selene import have, be

from model.controls.date_picker import set_tomorrow_date
from model.user import User
from utils import clear


class Page:
    def __init__(self):
        self.task_btn_selector = '#gas__content-header button'
        self.dispatcher_button_order_list_selector = '.action-btn.list-type'
        self.dispatcher_order_headers_selector = '.order-card p.h5'
        self.order_buttons_selector = '.global-btn-wrapper>button'

    def create_order(self, user: User):
        user.browser.all(self.task_btn_selector).element_by(have.text('Создать заказ')).click()

    def open_order_list(self, user: User):
        user.browser.element(self.dispatcher_button_order_list_selector).click()

    def choose_order_by_number(self, user: User, order_num):
        user.browser.all(self.dispatcher_order_headers_selector).element_by(have.text(order_num)).click()

    def confirm_order(self, user: User):
        clear.warning(user)
        user.browser.all(self.order_buttons_selector).element_by(have.text('Принять заказ')).click()

    def appoint_master_for_the_order(self, user: User):
        user.browser.element(self.order_buttons_selector).wait_until(have.text('Назначить время'))
        clear.warning(user, force=True)
        if not user.browser.element(self.order_buttons_selector).wait_until(be.clickable):
            clear.warning(user)
        user.browser.element(self.order_buttons_selector).click()
        set_tomorrow_date(user, 'title')
        user.browser.all('.selected-order-date button').element_by(have.text('Назначить')).click()
        clear.warning(user)
        user.browser.element(self.order_buttons_selector).should(have.text('Выбрать мастера')).click()
        user.browser.all('ol.content.list>li button').first.click()

    def open_order_by_number(self, user: User, order_num):
        clear.warning(user)
        user.browser.all('ul.sidebar-nav a').element_by(have.text('История заказов')).click()
        user.browser.all('.dropdown-menu .link').element_by(have.text('Заказы новые')).click()
        user.browser.all('.order-card p.h5').element_by(have.text(order_num)).click()



