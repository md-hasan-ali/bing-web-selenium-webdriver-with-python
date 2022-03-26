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
        time.sleep(5)

    def click_signin_option(self):
        time.sleep(5)
        self.find_element(*self.locator.CLICK_SIGNIN_OPTION).click()

    def click_github(self):
        time.sleep(5)
        self.find_element(*self.locator.CLICK_GITHUB).click()

    def set_git_email(self, email):
        self.find_element(*self.locator.SET_GITHUB_EMAIL).send_keys(email)
        time.sleep(5)

    def set_github_password(self, password):
        self.find_element(*self.locator.SET_GITHUB_PASS).sendkeys(password)
        time.sleep(5)

    def click_github_signin(self):
        time.sleep(3)
        self.find_element(*self.locator.CLICK_GITHUB_SIGNIN).click()