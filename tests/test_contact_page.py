from pages.login_page import LoginPage
from pages.contact_page import ContactPage


def test_contact_page(driver):
    driver.get("https://www.automationexercise.com")
    login_pages = LoginPage(driver)
    contact_page = ContactPage(driver)
    login_pages.login("emily.johnson123@example.com","TestPass!2025")
    contact_page.contact("Emily Johnson","emily.johnson123@example.com","Test","Contact Page Test")
    contact_page.alert_message()
    assert contact_page.success_message() == "Success! Your details have been submitted successfully."