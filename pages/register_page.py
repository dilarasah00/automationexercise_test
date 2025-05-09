from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
        self.name_input =(By.ID,"name")
        self.email_input =(By.ID,"email")
        self.password_input =(By.ID,"password") 
        self.first_name_input =(By.ID,"first_name")
        self.last_name_input =(By.ID,"last_name") 
        self.address1_input =(By.ID,"address1")
        self.country_input =(By.ID,"country")
        self.state_input =(By.ID,"state")
        self.city_input =(By.ID,"city")
        self.zipcode_input =(By.ID,"zipcode")
        self.mobile_number_input =(By.ID,"mobile_number")
        self.button =(By.CSS_SELECTOR,'[data-qa="create-account"]')
        self.register_message = (By.CSS_SELECTOR,'[data-qa="account-created"]')
        self.continue_button = (By.CSS_SELECTOR,'[data-qa="continue-button"]')


    def get_full_name(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.name_input)).get_attribute("value")
    def get_email(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.email_input)).get_attribute("value")
    def enter_password(self,password):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.password_input))).send_keys(password)
    def enter_first_name(self,first_name):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.first_name_input))).send_keys(first_name)
    def enter_last_name(self,last_name):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.last_name_input))).send_keys(last_name)
    def enter_address(self,address):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.address1_input))).send_keys(address)
    def enter_country(self,country):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.country_input))).send_keys(country)
    def enter_state(self,state):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.state_input))).send_keys(state)
    def enter_city(self,city):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.city_input))).send_keys(city)
    def enter_zipcode(self,zipcode):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.zipcode_input))).send_keys(zipcode)
    def enter_number(self,number):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.mobile_number_input))).send_keys(number)
    def create_account(self):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.button)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    def message (self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.register_message))).text
    def is_continue_button_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.continue_button))).is_displayed()

    def register(self,password,firstName,lastName,address,country,state,city,zipcode,number):
        self.enter_password(password)
        self.enter_first_name(firstName)
        self.enter_last_name(lastName)
        self.enter_address(address)
        self.enter_country(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_number(number)
        self.create_account()

        

