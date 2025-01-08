from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_HOME_LINK = (By.XPATH, """//*[@id="app"]/main/nav/a""")
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND_BTN = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[4]/button")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=5)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=8)
        text = user_field.text
        logging.info(f"We find text {text} in user field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def click_new_post_btn(self):
        logging.info("Click Create new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def click_save_post_btn(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_post_title_text(self):
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        text = title_field.text
        logging.info(f"We find text {text} in post title field {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        return text

    def click_home_link(self):
        logging.info("Click home link")
        self.find_element(TestSearchLocators.LOCATOR_HOME_LINK).click()

    def click_contact_link(self):
        logging.info("Click contact link")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def enter_contact_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_contact_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_contact_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_DESCRIPTION_FIELD[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)

    def click_contact_send_btn(self):
        logging.info("Click Contact Us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in alert field {alert}")
        return text
