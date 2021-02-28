import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def pruduct_successfully_added_to_basket(self):
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
        productNameInBasket = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert productName == productNameInBasket, "Наименования товара в корзине не совпадает с ожидаемым"

    def busket_price_equal_goods_price(self):
        productPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SITE).text
        productPriceInBusket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BUSKET).text
        print(f"{productPrice}\n {productPriceInBusket}")
        assert productPrice == productPriceInBusket, "Стоимость товара в корзине и на сайте не равна"


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
