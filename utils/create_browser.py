from selene import Browser, Config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

from utils import config


def chrome():
    return Browser(
        Config(
            driver=Chrome(ChromeDriverManager().install()),
            base_url=config.BASE_URL,
            window_width=1400,
            window_height=1080
        )
    )
