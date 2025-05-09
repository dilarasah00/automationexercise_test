from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class ContactPage:
    def __init__(self,driver):
        self.driver = driver
        self.contact_us_button=(By.CSS_SELECTOR,"a[href='/contact_us']")
        self.name_input =(By.NAME,"name")
        self.email_input =(By.NAME,"email")
        self.subject_input =(By.NAME,"subject")
        self.message_input =(By.NAME,"message")
        self.file = (By.NAME,"upload_file")
        self.submit_button =(By.NAME,"submit")
        self.message =(By.CSS_SELECTOR,".alert.alert-success")

    def click_contact_us_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.contact_us_button))).click()
    def enter_name(self,name):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.name_input))).send_keys(name)
    def enter_email(self,email):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.email_input))).send_keys(email)
    def enter_subject(self,subject):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.subject_input))).send_keys(subject)
    def enter_message(self,message):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.message_input))).send_keys(message)
    def upload_file(self,file):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.file))).send_keys(file)
    def click_submit_button(self):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.submit_button)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    def success_message(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.message))).text
    
    def alert_message(self):
        alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        alert_text =alert.text
        print(alert_text)
        alert.accept()

    def contact(self,name,email,subject,message):
        self.click_contact_us_button()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)
        self.click_submit_button()