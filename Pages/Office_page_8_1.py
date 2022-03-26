import time

from Locators.locators import FooterLocators
from Pages.HomePage import HomePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = FooterLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def surface_pro_8(self, element):
        time.sleep(4)
        self.find_element(*self.locator.CLICK_SURFACE_PRO_8).click()
        time.sleep(3)
