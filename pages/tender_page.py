from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
import time


class Tender_Page:
    def __init__(self, driver):
        self.driver = driver

        # Tender
        self.tender_button = (By.XPATH, "//span[normalize-space()='Tender']")
        self.header_text = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[2]/aes-editor-navbar/h1")

        # RFQ
        self.rfq_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[3]/div[2]/mat-tree-node[1]")

        # PO
        self.po_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[3]/div[2]/mat-tree-node[4]")

    # Tender
    def click_tender_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.tender_button)).click()
    def is_tender_button_visible(self):
        try:
            button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.tender_button))
            return button.is_displayed(), button.text
        except TimeoutException:
            return False
    
    def is_header_text_displayed(self):
        header = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.header_text))
        return header.is_displayed(), header.text
    
    # RFQ
    def click_rfq_button(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.rfq_button)).click()
    def is_rfq_button_visible(self):
        button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.rfq_button))
        return button.is_displayed(), button.text
    
    # PO
    def click_po_button(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.po_button)).click()
    def is_po_button_visible(self):
        text = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.po_button))
        return text.is_displayed(), text.text
