from pages.login_page import LoginPage



def test_valid_login(driver):
    driver.get("https://www.automationexercise.com")
    login_page = LoginPage(driver)
    login_page.login("emily.johnson123@example.com","TestPass!2025")
    assert login_page.user_knowledge()
    assert login_page.logoutButton()
    assert login_page.delete_account()
        

        

        
       
        

    
    
