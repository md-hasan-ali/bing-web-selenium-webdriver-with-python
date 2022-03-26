from Pages.Office_page_2_5 import LoginPage
from Pages.Base import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.click_signin_option()
        loginPage.click_github()
        LoginPage.set_git_email('hasanaliringku@gmail.com')
        LoginPage.set_github_password("hasan300483")
        loginPage.click_github_signin()

