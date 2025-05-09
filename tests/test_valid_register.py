from pages.signup_page import SignupPage
from pages.register_page import RegisterPage
import pytest
import json



def load_test_data():
        with open("data/register_data.json") as file:
            return json.load(file)


@pytest.mark.parametrize("user_data", load_test_data())
def test_valid_register(driver,user_data):
    driver.get("https://www.automationexercise.com")  
    signup_page = SignupPage(driver)
    register_page = RegisterPage(driver)
    signup_page.signup(user_data["name"],user_data["email"])


    assert register_page.get_full_name() == user_data["name"]
    assert register_page.get_email() == user_data["email"]

    register_page.register(user_data["password"],user_data["first_name"],user_data["last_name"],user_data["address"],user_data["country"],user_data["state"],user_data["city"],user_data["zipcode"],user_data["mobile_number"])

    assert driver.current_url =="https://www.automationexercise.com/account_created"
    assert register_page.message() == "ACCOUNT CREATED!"
    assert register_page.is_continue_button_visible()
        