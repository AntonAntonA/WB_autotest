from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from ProductPage import ProductPage
import WB_common


class ItemCardSearchResult:
    def __init__(self, driver, index: int):
        self.driver = driver
        self.index = index
        self.brand_name = ''
        self.goods_name = ''
        self.raiting = 0
        self.reviews_count = 0
        self.lower_price = 0.
        self.old_price = 0.

        # Поиск элемента: (xpath родительского wrapper)[индекс]//(требуемый элемент с нужным атрибутом)
        self.xpath_parent_div = '(// div[@class =\'product-card__wrapper\'])'

        self.xpath_brand_name = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                                'span[@class =\'product-card__brand\']'

        self.xpath_goods_name = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                                'span[@class =\'product-card__name\']'

        self.xpath_lower_price = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                                 'span[@class=\'price__lower-price\']'

        self.xpath_lower_price_2 = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                                   'ins[@class=\'price__lower-price\']'

        self.xpath_old_price = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                               'del'

        self.xpath_add_to_basket_btn = self.xpath_parent_div + '[' + str(self.index) + ']' + '//' + \
                                       'a[@class="product-card__add-basket j-add-to-basket btn-main-sm"]'

        # ---------------------------------------------------------------------------------------------------------------
        self.brand_name = driver.find_element(By.XPATH, self.xpath_brand_name).text
        self.goods_name = driver.find_element(By.XPATH, self.xpath_goods_name).text.lstrip('/ ')

        self.lower_price = ''
        try:
            self.lower_price = driver.find_element(By.XPATH, self.xpath_lower_price).text
        except NoSuchElementException:
            self.lower_price = driver.find_element(By.XPATH, self.xpath_lower_price_2).text

        self.old_price = ''
        try:
            self.old_price = driver.find_element(By.XPATH, self.xpath_old_price).text
        except NoSuchElementException:
            self.old_price = ''

        # self.add_to_basket_btn = driver.find_element(By.XPATH, self.xpath_add_to_basket_btn)
        return

    def add_to_basket(self):
        # Наводимся на нужную карточку
        item_card_div = self.driver.find_element(By.XPATH, self.xpath_parent_div + '[' + str(self.index) + ']')

        # Скроллимся до товарной карточки, чтобы она стала видна на экране
        WB_common.scroll_to_element(self.driver, item_card_div)

        action = ActionChains(self.driver)
        action \
            .move_to_element(item_card_div) \
            .perform()

        # Получаем элемент кнопки добавления в корзину
        add_to_basket_btn = self.driver.find_element(By.XPATH, self.xpath_add_to_basket_btn)

        # Наводимся на нее и кликаем
        action = ActionChains(self.driver)
        action \
            .move_to_element(add_to_basket_btn) \
            .click() \
            .perform()
        return

    def go_to_item_page(self):
        # Наводимся на нужную карточку и кликаем по ней
        item_card_div = self.driver.find_element(By.XPATH, self.xpath_parent_div + '[' + str(self.index) + ']')

        # Скроллимся до товарной карточки, чтобы она стала видна на экране
        WB_common.scroll_to_element(self.driver, item_card_div)

        action = ActionChains(self.driver)
        action \
            .move_to_element(item_card_div) \
            .click() \
            .perform()

        # Вернуть page object для страницы с товаром
        return ProductPage(self.driver)

    def get_brand_name(self):
        return self.brand_name

    def get_goods_name(self):
        return self.goods_name

    def get_lower_price(self):
        return self.lower_price

    def get_old_price(self):
        return self.old_price
