from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.signupLogin_button = (By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.email_input = (By.CSS_SELECTOR,'[data-qa="login-email"]')
        self.password_input = (By.CSS_SELECTOR,'[data-qa="login-password"]')
        self.login_button = (By.CSS_SELECTOR,'[data-qa="login-button"]')
        self.form = (By.CLASS_NAME,'login-form')
        self.user_knowladge =(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
        self.logout_button = (By.CSS_SELECTOR,"a[href='/logout']")
        self.delete_button = (By.CSS_SELECTOR,"a[href='/delete_account']")
        self.message = (By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/p")
        

    def open_login_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.signupLogin_button))).click()
    def enter_email(self,useremail):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.email_input))).send_keys(useremail)
    def enter_password(self,password):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.password_input))).send_keys(password)
    def click_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.login_button))).click()
    def is_login_form_displayed(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.form))).is_displayed()
    def user_knowledge(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.user_knowladge))).is_displayed()
    def logoutButton(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.logout_button))).is_displayed()
    def delete_account(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.delete_button))).is_displayed()    
    def error_message(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.message))).text
   

    def login(self,email,password):
        self.open_login_page()
        assert self.driver.current_url == "https://www.automationexercise.com/login", "Login sayfası açılmadı."
        assert self.is_login_form_displayed(), "Login formu görünmüyor."
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

        
