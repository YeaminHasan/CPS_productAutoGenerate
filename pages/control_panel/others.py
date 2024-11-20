from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Control_Panel_Page:
    def __init__(self, driver):
        self.driver = driver

        self.header_text = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[2]/aes-editor-navbar/h1")

        # Organization
        self.organization_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[1]/div[2]/mat-tree-node[1]")


        # All Partner
        self.all_partner_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[1]/div[2]/mat-tree-node[6]")

        # Registration
        self.registration_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[1]/div[2]/mat-tree-node[7]")

        # Pending Product Request
        self.pending_product_req_button = (By.XPATH, "/html/body/aes-editor-root/aes-page/div[1]/aes-sidebar/section/mat-tree/mat-nested-tree-node[1]/div[2]/mat-tree-node[8]")



   
    def is_header_text_displayed(self):
        header = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.header_text))
        return header.is_displayed(), header.text
    
    # Organization
    def click_organization_button(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.organization_button)).click()
    def is_organization_button_visible(self):
        button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.organization_button))
        return button.is_displayed(), button.text

    
    # All Partner
    def click_all_partner_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.all_partner_button)).click()
    def is_all_partner_button_visible(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.all_partner_button))
        return button.is_displayed(), button.text
    
    # Registration
    def click_registration_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.registration_button)).click()
    def is_registration_button_visible(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.registration_button))
        return button.is_displayed(), button.text
    
    # Pending Product Request
    def click_pending_product_req_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.pending_product_req_button)).click()
    def is_pending_product_req_button_visible(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.pending_product_req_button))
        return button.is_displayed(), button.text