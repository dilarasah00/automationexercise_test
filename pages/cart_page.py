from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.cart_button=(By.CSS_SELECTOR,"a[href ='/view_cart']")
        self.cart_detail=(By.ID,"cart_info_table")

    def open_cart(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.cart_button))).click()

    
    def is_cart_empty(self):
        tbody =WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((self.cart_detail))).find_element(By.TAG_NAME,"tbody")
        rows = tbody.find_elements(By.TAG_NAME,"tr")
        return len(rows)
    
    def check_cart_inside(self):
        name = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((self.cart_detail))).find_element(By.XPATH,"//*[@id='product-1']/td[2]/h4/a").text
        price = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((self.cart_detail))).find_element(By.XPATH,"//*[@id='product-1']/td[3]/p").text
        return name,price