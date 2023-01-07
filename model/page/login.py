from selene import have

from model.user import User


class Page:
    def __init__(self):
        self.url = '/login'
        self.input_phone_selector = '.gas-input input[placeholder=Телефон]'
        self.input_email_selector = '.gas-input input[placeholder=E-mail]'
        self.input_password_selector = '.gas-input input[placeholder=Пароль]'

    def login(self, user: User):
        user.browser.open(self.url)
        user.browser.element(self.input_email_selector).set_value(user.email)
        user.browser.element(self.input_password_selector).set_value(user.password)
        user.browser.element('button.btn').should(have.text('Далее')).click()
        # user.browser.element('.header .title').should(have.text(f'{user.last_name}'))
