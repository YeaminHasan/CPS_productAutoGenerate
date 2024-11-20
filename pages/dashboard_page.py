from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitTime = 3

        # Dashboard Button
        self.dashboard_button = (By.XPATH, "//mat-tree-node[normalize-space()='Dashboard']")
        self.dashboard_header_text = (By.XPATH, "//h1[normalize-space()='Dashboard']")


    def click_dashboard_button(self):
        WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.dashboard_button)).click()
    def is_dashboard_button_visible(self):
        try:
            button = WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.dashboard_button))
            return button.is_displayed(), button.text
        except TimeoutException:
            return False
        
    def is_dashboard_displayed(self):
        try:
            header = WebDriverWait(self.driver, self.waitTime).until(EC.element_to_be_clickable(self.dashboard_header_text))
            return header.is_displayed(), header.text
        except TimeoutException:
            return False