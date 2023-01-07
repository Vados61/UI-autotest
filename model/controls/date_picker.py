import datetime

from model.user import User


def set_tomorrow_date(user: User, parameter):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    user.browser.element(f"td[{parameter}='{tomorrow}']").click()
