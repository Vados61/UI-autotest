import time

from selene import be

from model.user import User


def warning(user: User, force=False):
    read_all_button = user.browser.element('.notice-list-fixed button.btn')
    if force:
        while read_all_button.wait_until(be.visible):
            if read_all_button.wait_until(be.clickable):
                read_all_button.click()
                time.sleep(1.5)
    while read_all_button.matching(be.visible):
        if read_all_button.wait_until(be.clickable):
            read_all_button.click()
            time.sleep(1.5)
