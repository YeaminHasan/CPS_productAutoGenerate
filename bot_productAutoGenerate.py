from selenium import webdriver
from pages.login_page import LoginPage
from pages.control_panel_page import Control_Panel_Page
from pages.control_panel.inventory_control_page import Inventory_Control_Page
from pages.control_panel.inventory_control_page import Add_Category_page
from pages.control_panel.inventory_control_page import Sub_Category_Handler_page
from pages.control_panel.inventory_control_page import Category_Handler_page
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.17.17.27/auth/login")

login_page = LoginPage(driver)
control_panel = Control_Panel_Page(driver)
inventory_control = Inventory_Control_Page(driver)
add_category = Add_Category_page(driver)
category = Category_Handler_page(driver)
subCategory = Sub_Category_Handler_page(driver)

# Login
login_page.enter_email("superadmin@gmail.com")
login_page.enter_password("12345678")
login_page.click_login_button()

time.sleep(3)
driver.get("http://172.17.17.27/editor/control-panel/category")
# Give Category Name to Auto Generating Products
selected_category_name = "House Keeping"
category.category_to_subCategory(selected_category_name)

# Store subCategory Name
sub_list = subCategory.store_all_subCategory_in_list()
# print(sub_list)

f = 81
f_max = 100
driver.get("http://172.17.17.27/editor/control-panel/category")
category.category_to_subCategory(selected_category_name)
for item in sub_list:
    print(f"Now creating {f} No subCategory Products")
    time.sleep(2)
    subCategory.generate_product(sub_list,f)
    if f == f_max:
        print(f"{f_max} == {f}")
        break
    f = f+1
    driver.get("http://172.17.17.27/editor/control-panel/category")
    # Give Category Name to Auto Generating Products
    category.category_to_subCategory(selected_category_name)