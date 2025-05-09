from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import re


def test_product_page(driver):
    driver.get("https://www.automationexercise.com")
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    login_page.login("emily.johnson123@example.com","TestPass!2025")
        

    assert product_page.is_category_visible(), f"Category alanı gözükmüyor."
    assert product_page.is_brands_visible(), f"Markalar gözükmüyor."
    assert product_page.is_product_list_visible(), f"Ürün listesi gözükmüyor."

    products = product_page.get_product_list()
    assert len(products) > 0, f"Hiç ürün bulunamadı."
       

    product_page.view_product()
    assert product_page.check_product_information()
    assert driver.current_url =="https://www.automationexercise.com/product_details/1"

    product_name, product_price = product_page.get_product_info()
    
    product_page.add_to_cart()
    cart_page.open_cart()
    assert driver.current_url == "https://www.automationexercise.com/view_cart"
    assert cart_page.is_cart_empty()>0

    cart_name,cart_price = cart_page.check_cart_inside()

    assert product_name == cart_name

    product_price_cleaned =re.sub(r'[^\d.]','',product_price)
    cart_price_cleaned = re.sub(r'[^\d.]','',cart_price)
    assert float(product_price_cleaned) == float(cart_price_cleaned)

    

        





        

    
    
