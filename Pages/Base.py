import time
import unittest

from selenium import webdriver


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/driver/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.office.com/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Test Complete")
