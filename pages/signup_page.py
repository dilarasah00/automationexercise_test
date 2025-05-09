from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self,driver):
        self.driver = driver
        self.signupLogin_button = (By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.name_input = (By.CSS_SELECTOR,'[data-qa="signup-name"]')
        self.email_input = (By.CSS_SELECTOR,'[data-qa="signup-email"]')
        self.signup_button = (By.CSS_SELECTOR,'[data-qa="signup-button"]')
        self.title = (By.XPATH,"//*[@id='form']/div/div/div/div[1]/h2/b")
        self.error =(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/p")
    def open_signup_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.signupLogin_button))).click()
    def enter_name(self,username):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.name_input))).send_keys(username)
    def enter_email(self,useremail):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.email_input))).send_keys(useremail)
    def click_signup_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.signup_button))).click()
    def get_signup_page_title (self):
       return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.title))).text
    def error_message(self):
       return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.error))).text

    def signup(self,username,email):
        self.open_signup_page()
        self.enter_name(username)
        self.enter_email(email)
        self.click_signup_button()

    
        


        
