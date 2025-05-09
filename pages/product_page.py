from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.category = (By.ID,'accordian')
        self.brands = (By.CLASS_NAME,'brands_products')
        self.products = (By.CLASS_NAME,'features_items')
        self.product_list = (By.CLASS_NAME,"col-sm-4")
        self.product_link = (By.CSS_SELECTOR, "a[href='/product_details/1']")
        self.add_to_cart_button = (By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
        self.product_information=(By.CLASS_NAME,"product-information")

    def is_category_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.category))).is_displayed()
    def is_brands_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.brands))).is_displayed()
    def is_product_list_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.products))).is_displayed()
    def get_product_list(self):
        return WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((self.product_list)))

    
    def add_to_cart(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.add_to_cart_button))).click()
    
    def get_product_info(self):
        element_item =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.product_information)))
        name = element_item.find_element(By.TAG_NAME,"h2").text
        price = element_item.find_element(By.TAG_NAME,"span").text
        return name,price

    def view_product(self):
        
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.product_link)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def check_product_information(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.product_information))).is_displayed()
    
        
    
    

   


    





   

        
          

 

        
