import time

from Locators.locators import SignInPageLocators
from Pages.HomePage import HomePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_login(self):
        self.find_element(*self.locator.LOGIN_ICON).click()
        time.sleep(7)

    def set_email(self, email):
        self.find_element(*self.locator.SET_EMAIL).send_keys(email)
        time.sleep(5)

    def click_next(self):
        self.find_element(*self.locator.CLICK_NEXT_BTN).click()
        time.sleep(5)

    def set_password(self, password):
        time.sleep(5)
        self.find_element(*self.locator.SET_PASS).send_keys(password)

    def click_signin(self):
        self.find_element(*self.locator.CLICK_SIGN).click()
        time.sleep(5)
