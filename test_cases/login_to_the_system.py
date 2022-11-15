import os
import time
import unittest
from selenium import webdriver

from pages.add_new_player_page import AddNewPlayerPage
from pages.dashboard.dashboard import Dashboard
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        # os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        # self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login.wait_on_login()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_add_player_in_button()
        add_new_player = AddNewPlayerPage(self.driver)
        add_new_player.type_in_email('user15@getnada.com')
        add_new_player.type_in_name('Sasha')
        add_new_player.type_in_surname('Sashko')
        add_new_player.type_in_age('11.11.1999')
        add_new_player.type_in_main_position('fall')
        add_new_player.click_on_the_submit_button()
        add_new_player.wait_on_add()
        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()