from selenium import webdriver
from login_page import LoginPage
from dashboard_page import DashboardPage
from control_panel_page import Control_Panel_Page
from vendor_management_page import Vendor_Management_page
from control_panel.inventory_control_page import Inventory_Control_Page
from control_panel.inventory_control_page import Add_New_Category_page
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.17.17.27/auth/login")

def login():
    login_page = LoginPage(driver)
    control_panel = Control_Panel_Page(driver)
    inventory_control = Inventory_Control_Page(driver)
    add_category = Add_New_Category_page(driver)
    
    login_page.enter_email("superadmin@gmail.com")
    login_page.enter_password("12345678")
    login_page.click_login_button()

    control_panel.click_control_panel_button()
    inventory_control.click_inventory_control_button()
    add_category.click_add_new_category_button()
    time.sleep(3)
    # add_category.select_dropdown_option("Own Product")
    add_category.select_dropdown_option()
    time.sleep(5)


    

    



login()