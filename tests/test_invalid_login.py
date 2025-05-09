from pages.login_page import LoginPage
import pytest
import json


def load_test_data():
        with open("data/invalid_login_data.json") as file:
            return json.load(file)


@pytest.mark.parametrize("user_data", load_test_data())
def test_invalid_login(driver,user_data):
    driver.get("https://www.automationexercise.com")
    login_page = LoginPage(driver)
    login_page.login(user_data["email"],user_data["password"])
    assert driver.current_url == "https://www.automationexercise.com/login"

        

        

        
       
        

    
    
