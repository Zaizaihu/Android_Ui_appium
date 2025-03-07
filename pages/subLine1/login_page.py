from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class LoginPage(BasePage):
    # 元素定位
    USERNAME_INPUT = (AppiumBy.ID, "com.example:id/username_input")
    PASSWORD_INPUT = (AppiumBy.ID, "com.example:id/password_input")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example:id/login_btn")

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()