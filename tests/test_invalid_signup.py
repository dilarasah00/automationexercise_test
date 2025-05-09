from pages.signup_page import SignupPage
import pytest
import json


def load_test_data():
        with open("data/invalid_signup_data.json") as file:
            return json.load(file)

class TestinvalidSignup:
    @pytest.mark.parametrize("user_data", load_test_data())
    def test_invalid_signup(self,driver,user_data):
        driver.get("https://www.automationexercise.com") 
        signup_page = SignupPage(driver)
        signup_page.signup(user_data["username"],user_data["email"],)
        assert driver.current_url == "https://www.automationexercise.com/login"
    
    def test_signup_with_existing_email(self,driver):
        driver.get("https://www.automationexercise.com")
        signup_page = SignupPage(driver)
        signup_page.signup("Emily Johnson", "emily.johnson123@example.com")
        assert signup_page.error_message() == "Email Address already exist!"

        
        

        

        
       
        

    
    
