from pages.signup_page import SignupPage

import time




def test_valid_signup(driver):
    driver.get("https://www.automationexercise.com")  
    signup_page = SignupPage(driver)
    signup_page.signup("Sophia Miller","sophia.miller789@example.com")
    time.sleep(5)
    assert driver.current_url == "https://www.automationexercise.com/signup"
    assert signup_page.get_signup_page_title() == "ENTER ACCOUNT INFORMATION"
        
        

    
    
