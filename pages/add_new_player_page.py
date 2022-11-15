from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddNewPlayerPage(BasePage):
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[ @ name = 'age']"
    main_position_field_xpath = "//*[@name = 'mainPosition'] "
    submit_button_xpath = "//*[text()='Submit']"
    add_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    expected_title = "Add player"
    title_of_box_xpath = "//*[text()='Add player'] "
    header_of_box = "Add Player"

    def wait_on_add(self):
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[text()="Added player."]'))
        )

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
