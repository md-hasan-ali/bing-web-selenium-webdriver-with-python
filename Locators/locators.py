from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    LOGIN_ICON = (By.ID, "mectrl_headerPicture")
    SET_EMAIL = (By.ID, "i0116")
    CLICK_NEXT_BTN = (By.ID, "idSIButton9")
    SET_PASS = (By.ID, "i0118")
    CLICK_SIGN = (By.ID, "idSIButton9")
    CLICK_YES_SIGN = (By.ID, "idSIButton9")
    CLICK_SIGNIN_OPTION = (By.CLASS_NAME, "table")
    CLICK_GITHUB = (By.XPATH, "//*[@id='credentialList']/div[2]/div[1]/div")
    SET_GITHUB_EMAIL = (By.XPATH, "//*[@id='login_field']")
    SET_GITHUB_PASS = (By.ID, "password")
    CLICK_GITHUB_SIGNIN = (By.XPATH, "//*[@id='login']/div[3]/form/div/input[12]")


class FooterLocators(object):
    CLICK_SURFACE_PRO_8 = (By.XPATH, "//*[@id='uhf-footer']/nav/div[1]/div[1]/ul/li[1]/a");
