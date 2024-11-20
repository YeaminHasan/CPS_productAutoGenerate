from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitTime = 5

        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//span[@class='mdc-button__label']")
        self.login_error_massage = (By.XPATH, '//*[@id="toast-container"]')
        self.email_field_error_masseage = (By.CLASS_NAME, "mat-mdc-form-field-error")

        

    def enter_email(self, email):
        WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.email_field)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver,self.waitTime).until(EC.element_to_be_clickable(self.password_field)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.login_button)).click()

    def is_error_message_displayed(self):
        element_is = WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.login_error_massage))
        return element_is.text, element_is.is_displayed()
    
    def is_email_Invalid_pattern_or_required(self):
        try:
            error = self.driver.find_element(*self.email_field_error_masseage)
            return error.is_displayed(), error.text
        except NoSuchElementException:
            return False