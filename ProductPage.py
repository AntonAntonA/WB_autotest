from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import WB_common


class ProductPage:
    """
    Класс, который описывает страницу с товаром
    """

    def __init__(self, driver):
        self.driver = driver
        self.basket_btn = None
        self.reviews_btn = None
        self.seller_btn = None
        self.similar_prods_btn = None
        self.promo_prods_btn = None
        self.also_buy_prods_btn = None

        # ----------------------------------------------------------------------------------
        # XPath для элементов страницы

        self.basket_btn_xpath = "//div[@class =\'product-page__aside-sticky\']" \
                                "//button[@class =\'btn-main\']"
        self.seller_btn_xpath = "//div[@class =\'seller-info__content\']" \
                                "//a[@class =\'seller-info__name seller-info__name--link\']"

        self.similar_prods_btn_xpath = "//div[@class =" \
                                       "\'product-page__goods-slider product-page__goods-slider--similar\']" \
                                       "//a[@class =\'goods-slider__see-all\']"
        self.promo_prods_btn_xpath = "//div[@class =" \
                                     "\'product-page__goods-slider product-page__goods-slider--promo j-adv-carousel-wrapper\']" \
                                     "//a[@class =\'goods-slider__see-all\']"
        self.also_buy_prods_btn_xpath = "//div[@class =" \
                                       "\'product-page__goods-slider product-page__goods-slider--also-buy\']" \
                                       "//a[@class =\'goods-slider__see-all\']"

        # ----------------------------------------------------------------------------------

        return

    # Получить URL страницы
    def get_URL(self):
        return self.driver.current_url

    # Добавить товар в корзину
    def add_to_basket(self):
        self.basket_btn = self.driver.find_element(By.XPATH, self.basket_btn_xpath)
        self.basket_btn.click()
        return

    # Получить все отзывы

    # Перейти к продавцу
    def go_to_seller(self):
        self.seller_btn = self.driver.find_element(By.XPATH, self.seller_btn_xpath)
        self.seller_btn.click()
        return

    # Получить описание товара с характеристиками
    def get_description(self):
        return

    # Перейти к похожим товарам
    def go_to_similar_prods(self):
        self.similar_prods_btn = self.driver.find_element(By.XPATH, self.similar_prods_btn_xpath)
        self.similar_prods_btn.click()
        return

    # Перейти к промотоварам
    def go_to_promo_prods(self):
        self.promo_prods_btn = self.driver.find_element(By.XPATH, self.promo_prods_btn_xpath)
        self.promo_prods_btn.click()
        return

    # Перейти к товарам, которые покупают вместе с данным
    def go_to_also_buy_prods(self):
        self.also_buy_prods_btn = self.driver.find_element(By.XPATH, self.also_buy_prods_btn_xpath)
        self.also_buy_prods_btn.click()
        return
