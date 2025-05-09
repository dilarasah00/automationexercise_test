from pages.signup_page import SignupPage
from pages.register_page import RegisterPage
import pytest
import json



def load_test_data():
        with open("data/invalid_register_data.json") as file:
            return json.load(file)


@pytest.mark.parametrize("user_data", load_test_data())
def test_invalid_register(driver,user_data):
    driver.get("https://www.automationexercise.com")
    signup_page = SignupPage(driver)
    register_page = RegisterPage(driver)
    signup_page.signup(user_data["name"],user_data["email"])


    register_page.register(user_data["password"],user_data["first_name"],user_data["last_name"],user_data["address"],user_data["country"],user_data["state"],user_data["city"],user_data["zipcode"],user_data["mobile_number"])

    assert driver.current_url =="https://www.automationexercise.com/signup"
    assert signup_page.get_signup_page_title() == "ENTER ACCOUNT INFORMATION"
            
        