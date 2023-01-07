import allure

from model.page import profile_client, login, create_order, order
from model.user import User
from utils import create_browser

login_page = login.Page()
profile_client_page = profile_client.Page()
creating_order_page = create_order.Page()
order_page = order.Page()
client = User(
    first_name='Клиент4',
    last_name='Клиентов4',
    patronymic='Клиентович4',
    email='test_client@test.com',
    phone_number=79778967484,
    password='QK4821',
    browser=create_browser.chrome()
)
dispatcher = User(
    first_name='ДиспетчерСССР1',
    last_name='ДиспетчеровCCCР1',
    patronymic='ДиспетчеровичСССР1',
    email='test_gw_dispatcher_sssr1@rambler.ru',
    phone_number=21313131313,
    password='123456',
    browser=create_browser.chrome(),
    firm_name='ООО "СССР"'
)
master = User(
    first_name='МастерCCCР1',
    last_name='МастеровCCCР1',
    patronymic='МастеровичCCCР1',
    email='test_gw_master_sssr1@rambler.ru',
    phone_number=79673723185,
    password='123456',
    browser=create_browser.chrome()
)


def test_registration_client():

    with allure.step(f'Логинимся за клиента {client.last_name}'):
        login_page.login(client)

    with allure.step('Создаем заказ ТО'):
        profile_client_page.create_order(client)
        creating_order_page.change_order(client, 'Заключение договора на ТО')
        creating_order_page.click_to_next_btn(client)
        creating_order_page.click_to_change_object_btn(client)
        creating_order_page.set_tomorrow_date(client)
        creating_order_page.set_time(client)
        creating_order_page.submit_order(client)
    with allure.step('Получаем смс за клиента'):
        client.wait_new_sms()
        client.get_order_num_from_last_sms()
        assert client.last_sms is not None
        assert client.order_num is not None

    with allure.step(f'Логинимся за диспетчера {dispatcher.last_name}'):
        login_page.login(dispatcher)

    with allure.step('Принимаем заказ от клиента'):
        profile_client_page.open_order_list(dispatcher)
        profile_client_page.choose_order_by_number(dispatcher, client.order_num)
        profile_client_page.confirm_order(dispatcher)
    with allure.step('Клиент выбирает компанию'):
        creating_order_page.choose_company(client, firm_name=dispatcher.firm_name)
        creating_order_page.pay_for_order(client)
        client.wait_new_sms()
        client.get_pass_from_sms()
        assert client.password_from_sms is not None
        creating_order_page.sign_contract_by_sms_code(client)
    with allure.step('Назначаем мастера для заказа'):
        profile_client_page.appoint_master_for_the_order(dispatcher)

    with allure.step(f'Логинимся за мастера {master.last_name}'):
        login_page.login(master)

    with allure.step('Мастер выполняет заказ'):
        profile_client_page.open_order_by_number(master, client.order_num)
        order_page.complete_work(master)
    with allure.step('Клиент платит за заказ'):
        creating_order_page.click_pay_for_order(client)
        creating_order_page.pay_for_order(client)
    with allure.step('Мастер подписывает акт'):
        order_page.sign_act_of_work(master)
        master.wait_new_sms()
        master.get_pass_from_sms()
        assert master.last_sms is not None
        assert master.password_from_sms is not None
        creating_order_page.sign_contract_by_sms_code(master)
    with allure.step('Клиент подписывает акт'):
        creating_order_page.sign_act_of_work(client)
        client.wait_new_sms()
        client.get_pass_from_sms()
        assert client.last_sms is not None
        assert client.password_from_sms is not None
        creating_order_page.sign_contract_by_sms_code(client)

    with allure.step('Клиент оставляет отзыв'):
        order_page.leave_comment(client)
        order_page.send_contract(client)
    with allure.step('Мастер оставляет отзыв'):
        order_page.leave_comment(master)
        order_page.go_home(master)

    with allure.step('Диспетчер убеждается что заказ выполнен'):
        order_page.assert_order_status(dispatcher)
