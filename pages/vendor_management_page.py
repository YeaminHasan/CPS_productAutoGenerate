from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
import time


class Vendor_Management_page:
    def __init__(self, driver):
        self.driver = driver

        # Vendor Management
        self.vendor_management_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[2]/div[1]/div")
        self.header_text = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[2]/aes-editor-navbar/h1")

        # Pending Vendors
        self.pending_vendors_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[2]/div[2]/mat-tree-node[1]")


    # Vendor Management
    def click_vendor_management_button(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.vendor_management_button)).click()
    def is_vendor_management_button_visible(self):
        try:
            button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.vendor_management_button))
            return button.is_displayed(), button.text
        except TimeoutException:
            return False
    def is_header_text_displayed(self):
        try:
            text = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.header_text))
            return text.is_displayed(), text.text
        except TimeoutException:
            return False
    
    # Pending Vendors
    def click_pending_vendors_button(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.pending_vendors_button)).click()
    def is_pending_vendors_button_visible(self):
        button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.pending_vendors_button))
        return button.is_displayed(), button.text