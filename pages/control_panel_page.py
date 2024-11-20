from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
import time


class Control_Panel_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

        # Control Panel
        self.control_panel_button = (By.XPATH, "//span[normalize-space()='Control Panel']")

    # Control Panel
    def click_control_panel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.control_panel_button)).click()
    def is_control_panel_button_visible(self):
        button = self.wait.until(EC.element_to_be_clickable(self.control_panel_button))
        return button.is_displayed(), button.text

    # Sub-Menus List
    def is_sub_menus_displayed(self):
            submenus_text_set = {submenu.text for submenu in self.driver.find_elements(By.XPATH, "//mat-nested-tree-node[.//span[text()='Control Panel']]//mat-tree-node") if submenu.text}
            return submenus_text_set