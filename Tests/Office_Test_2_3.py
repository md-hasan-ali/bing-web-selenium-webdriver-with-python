from Pages.Office_page_2_1 import LoginPage
from Pages.Base import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.set_email("+880 1322-035726")
        loginPage.click_next()
        loginPage.set_password("hasan300485")
        loginPage.click_signin()
