from selenium.webdriver.common.by import By


class ProductPageLocators():
    # для теста добавления в корзину и названия в корзине
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn:nth-child(3)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    #для сравнения стоимости товара
    PRODUCT_PRICE_SITE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_PRICE_IN_BUSKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
