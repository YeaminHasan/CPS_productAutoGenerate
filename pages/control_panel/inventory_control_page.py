from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Category_Handler_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

        # Rows
        self.rows_element = (By.XPATH, "//tbody/tr")
        self.category_element = (By.XPATH, ".//td[contains(@class, 'cdk-column-categoryName')]")
        self.subcategory_count_element = (By.XPATH, ".//td[contains(@class, 'cdk-column-subcategoryCount')]")
        self.right_arrow_element = (By.XPATH, ".//mat-icon[text()='arrow_right_alt']")
        self.right_arrow_element_Dyn = (By.XPATH, ".//mat-icon[contains(@class, 'mat-icon') and text()='arrow_right_alt']") # Dynamic
        self.edit_icon_element = (By.XPATH, ".//mat-icon[text()='edit']")
        self.edit_icon_element_Dyn = (By.XPATH, ".//mat-icon[contains(@class, 'mat-icon') and text()='edit']") # Dynamic
        self.delete_icon_element = (By.XPATH, ".//mat-icon[text()='delete']")
        self.delete_icon_element_Dyn = (By.XPATH, ".//mat-icon[contains(@class, 'mat-icon') and text()='delete']") # Dynamic
        self.next_button_element = (By.XPATH, "//button[contains(@class, 'mat-mdc-paginator-navigation-next')]")

        self.empty_msg = "No data matching the filter."

    def category_search(self, category_text):
        while True:
            flag = 0
            # wait
            self.wait.until(EC.presence_of_all_elements_located(self.rows_element))
            rows = self.driver.find_elements(*self.rows_element)
            for row in rows:
                current_category_name = row.find_element(*self.category_element).text.strip()
                category = current_category_name.split(" - ")
                category_code = category[0]
                category_name = category[1]
                if category_name.lower() == category_text.lower():
                    # Action Area
                    print(f"Found the category: {category_name}\nCategory code: {category_code}")
                    flag = 1
                    break

            try:
                if flag == 0:
                    next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_element))
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                elif flag == 1:
                    break
            except Exception:
                break

    # def category_edit(self, category_text):
    #     while True:
    #         flag = 0
    #         # wait
    #         self.wait.until(EC.presence_of_all_elements_located(self.rows_element))
    #         rows = self.driver.find_elements(*self.rows_element)
    #         for row in rows:
    #             current_category_name = row.find_element(*self.category_element).text.strip()
    #             category = current_category_name.split(" - ")
    #             category_code = category[0]
    #             category_name = category[1]
    #             if category_name.lower() == category_text.lower():
    #                 # Action Area
    #                 edit_icon = row.find_element(*self.edit_icon_element_Dyn)
    #                 edit_icon.click()
    #                 flag = 1
    #                 break

    #         try:
    #             if flag == 0:
    #                 next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_element))
    #                 if next_button.is_enabled():
    #                     next_button.click()
    #                 else:
    #                     break
    #             elif flag == 1:
    #                 break
    #         except Exception:
    #             break

    # def category_delete(self, category_text):
        while True:
            flag = 0
            # wait
            self.wait.until(EC.presence_of_all_elements_located(self.rows_element))
            rows = self.driver.find_elements(*self.rows_element)
            for row in rows:
                current_category_name = row.find_element(*self.category_element).text.strip()
                category = current_category_name.split(" - ")
                category_code = category[0]
                category_name = category[1]
                if category_name.lower() == category_text.lower():
                    # Action Area
                    delete_icon = row.find_element(*self.delete_icon_element_Dyn)
                    delete_icon.click()
                    flag = 1
                    break

            try:
                if flag == 0:
                    next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_element))
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                elif flag == 1:
                    break
            except Exception:
                break

    def category_to_subCategory(self, category_text):
        while True:
            flag = 0
            # wait
            self.wait.until(EC.presence_of_all_elements_located(self.rows_element))
            rows = self.driver.find_elements(*self.rows_element)
            for row in rows:
                current_category_name = row.find_element(*self.category_element).text.strip()
                category = current_category_name.split(" - ")
                category_code = category[0]
                category_name = category[1]
                if category_name.lower() == category_text.lower():
                    # Action Area
                    right_arrow_icon = row.find_element(*self.right_arrow_element_Dyn)
                    right_arrow_icon.click()
                    flag = 1
                    break

            try:
                if flag == 0:
                    next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_element))
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                elif flag == 1:
                    break
            except Exception:
                break

class Sub_Category_Handler_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

        self.sub_rows_element = (By.XPATH, "//tbody/tr")
        self.sub_category_name_element = (By.XPATH, ".//td[contains(@class, 'cdk-column-subCategoryName')]")
        self.sub_right_arrow_element_Dyn = (By.XPATH, ".//mat-icon[contains(@class, 'mat-icon') and text()='arrow_right_alt']") # Dynamic
        self.generate_product_button_element = (By.XPATH, "//img[@src='./assets/images/generate-product.svg']")
        self.generate_button = (By.XPATH, "//span[normalize-space()='Generate']")
        self.all_select = (By.XPATH, "//th[@role='columnheader']//input[@type='checkbox']")
        self.active_element = (By.XPATH, "//span[normalize-space()='Active']")


        self.sub_next_button_element = (By.XPATH, "//button[contains(@class, 'mat-mdc-paginator-navigation-next')]")

    def store_all_subCategory_in_list(self):
        sub_category_name_list = []
        while True:
            flag = 0
            # wait
            self.wait.until(EC.presence_of_all_elements_located(self.sub_rows_element))
            time.sleep(2)
            rows = self.driver.find_elements(*self.sub_rows_element)
            for row in rows:
                current_sub_category_name = row.find_element(*self.sub_category_name_element).text.strip()            
                sub_category_name_list.append(current_sub_category_name)
                
            time.sleep(1)
            
            try:
                if flag == 0:
                    next_button = self.wait.until(EC.element_to_be_clickable(self.sub_next_button_element))
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                elif flag == 1:
                    break
            except Exception:
                break
        
        print(len(sub_category_name_list))
        print(sub_category_name_list)
        self.driver.get("http://172.17.17.27/editor/control-panel/category")
        return sub_category_name_list

   
    def generate_product(self, subC_list, f, f2):
        sub_category_name_list = subC_list
        
        # Page Count
        result = f // 10
        if result>0:
            for i in range(result):
                print(f"Page = {i+1}")
                time.sleep(2)
                next_button = self.wait.until(EC.element_to_be_clickable(self.sub_next_button_element))
                if next_button.is_enabled():
                    next_button.click()

        # Product Generate function
        while True:
            flag = 0
            # wait
            self.wait.until(EC.presence_of_all_elements_located(self.sub_rows_element))
            time.sleep(2)

            rows = self.driver.find_elements(*self.sub_rows_element)
            
            for row in rows:
                current_sub_category_name = row.find_element(*self.sub_category_name_element).text.strip()
                
                if (current_sub_category_name == sub_category_name_list[f]) and (f <= f2):
                    print(current_sub_category_name)
                    right_arrow_icon = row.find_element(*self.sub_right_arrow_element_Dyn)
                    right_arrow_icon.click()
                    flag = 1
                    auto_generate_product = self.wait.until(EC.element_to_be_clickable(self.generate_product_button_element))
                    auto_generate_product.click()
                    self.generate_card()
                    # f = f+1
                    break


            time.sleep(1)
            # print(sub_category_name_list)
            try:
                if flag == 0:
                    next_button = self.wait.until(EC.element_to_be_clickable(self.sub_next_button_element))
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                elif flag == 1:
                    break
            except Exception:
                break




    def generate_card(self):
            # category = Category_Handler_page(self.driver)
            # generate product Card page
            try:
                actions = ActionChains(self.driver)
                time.sleep(1)
                elements_with_placeholder = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, "//mat-select[@placeholder='Enter Value']")
                    )
                )

                # print(f"Found {len(elements_with_placeholder)} elements with placeholder 'Enter Value'.")

                # Iterate through each element
                for index, element in enumerate(elements_with_placeholder):
                    # print(f"Interacting with element {index + 1}")
                    time.sleep(1)
                    element.click()  # Click the element to open the dropdown

                    # Wait for dropdown options to appear
                    options = self.wait.until(
                        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//mat-option"))
                    )
                    
                    # print(f"Found {len(options)} options for element {index + 1}.")

                    # Print and interact with dropdown options
                    for option in options:
                        option_text = option.text
                        # print(f"Option: {option_text}")
                        option.click()  # Select the option
                        time.sleep(0.5)  # Small delay between selections

                    # Simulate TAB key action to move focus out of the dropdown
                    actions.send_keys(Keys.TAB).perform()
                    actions.send_keys(Keys.TAB).perform()
                    actions.send_keys(Keys.TAB).perform()
                    time.sleep(0.5)

            except Exception as e:
                print(f"An error occurred: {e}")


            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                # Navigate to the page

                # Wait for the "Select Brand" element to be visible
                time.sleep(0.5)
                select_brand_element = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//mat-select[@placeholder='Select Brand']")
                    )
                )
                # print("Found the 'Select Brand' element.")

                # Interact with the element
                select_brand_element.click()
                # print("Clicked on the 'Select Brand' element.")

                # Wait for the dropdown options to appear
                options = self.wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//mat-option"))
                )

                # print(f"Found {len(options)} options.")

                # Print and interact with dropdown options
                for option in options:
                    option_text = option.text
                    # print(f"Option: {option_text}")
                    option.click()
                    time.sleep(0.5)  # Small delay between selections
                actions.send_keys(Keys.TAB).perform()

            except Exception as e:
                print(f"An error occurred: {e}")

            # Condition is-enable
            try:
                g_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.generate_button))
                if g_button.is_enabled():
                    time.sleep(0.5)
                    g_button.click()

                    try:
                        time.sleep(5)
                        a_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.all_select))
                        if a_button.is_enabled():
                            a_button.click()

                            try:
                                time.sleep(2)
                                active = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.active_element))
                                if active.is_enabled():
                                    active.click()
                                    print("product Created Successfully")
                            except Exception:
                                print("Active button not Active")
                                print("Product not Generate")

                    except Exception:
                        print("All Select not Active")
                        print("Product not Generate")


            except Exception:
                print("Generate Button not Active")
                print("Product not Generate")

        