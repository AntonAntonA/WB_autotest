import traceback
import inspect
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from WB_common_consts import MPXPath
from WB_common_consts import MPID
from WB_common_consts import MPClass
from ItemCardSearchResult import ItemCardSearchResult

# Список PageObjects:
# MainPage
# SearchResultPage
# LoginPopup
# RegistrationPage
from MainPage import MainPage
from WB_common_consts import URL
import WB_UnitTests

class App:
    def __init__(self):
        # Инициализация тестов
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(URL.WB_main_URL)
        self.driver.maximize_window()

        self.main_page = MainPage(self.driver)

        return

    def end(self):
        self.driver.quit()

    # Поиск товара
    def test_search_item(self, test_query):
        '''
        простой поиск товара по верному запросу и сравнение с результпатом запроса
        :param: test_query - поисковый запрос
        :return:
        '''

        def words_check(words, target_str):
            for word in words:
                if word in target_str:
                    continue
                else:
                    return False
            return True

        search_results_page = self.main_page.search_item(test_query)
        item = search_results_page.get_item(1)
        print(item.get_goods_name())

        test_words = test_query.split()
        if words_check(test_words, item.get_goods_name()):
            print(inspect.currentframe().f_code.co_name + ' passed')
        else:
            raise Exception(inspect.currentframe().f_code.co_name + ' failed')

        # (xpath родительского wrapper)[индекс]//(требуемый элемент с нужным атрибутом)

        # print(self.driver.find_element(By.XPATH, '// div[@class =\'product-card__wrapper\']//ins[@class=\'price__lower-price\']').text)

        # print(f'Общее количество найденных товаров на странице: {search_results_page.get_items_count_on_cur_page()}')

        # # Проверка на самом последнем элементе
        # item = search_results_page.get_item(search_results_page.get_items_count_on_cur_page() - 1)
        # # item = search_results_page.get_item(2)
        # item.add_to_basket()
        # print(item.get_brand_name())
        # print(item.get_goods_name())
        # print(item.get_old_price())
        # print(item.get_lower_price())
        # print('------------------------------------------------------------------------------------')

        # for i in range(1, 5):
        #     item = search_results_page.get_item(i)
        #     if i == 3:
        #         item.add_to_basket()
        #     print(item.get_brand_name())
        #     print(item.get_goods_name())
        #     print(item.get_old_price())
        #     print(item.get_lower_price())
        #     print('------------------------------------------------------------------------------------')

        # item = search_results_page.get_item(1)

        # print(item.get_brand_name())

    # Автотестирование покупки товара на WB

    # Логирование в систему

    # Выбор товара из строки поиска

    # Добавление товара в корзину
    def test_add_good_in_basket(self, goods_name):
        search_result_page = self.main_page.search_item(goods_name)
        item = search_result_page.get_item(1)

        # Добавляем товар в корзину
        item.add_to_basket()

        # Переходим на страницу с товаром и запоминаем ссылку
        item_page = item.go_to_item_page() # TODO: реализовать страницу товара и переход на нее
        item_page_URL = item_page.get_URL()

        # Переходим в корзину и щелкаем по добавленному товару
        basket_page = self.main_page.go_to_basket() # TODO: реализовать PageObject для корзины
        basket_item = basket_page.get_item(1) # TODO: реализовать PageObject для товарной позиции в корзине
        basket_item_page = basket_item.go_to_item_page()
        basket_item_page_URL = basket_item_page.get_URL()

        if item_page_URL == basket_item_page_URL:
            print(inspect.currentframe().f_code.co_name + ' passed')
        else:
            raise Exception(inspect.currentframe().f_code.co_name + ' failed')

        return

    # Оформление заказа


if __name__ == '__main__':
    try:
        app = App()

        b_unit_test = True

        if b_unit_test:
            WB_UnitTests.utest_add_item_to_basket(app)

        else:
            app.test_search_item('Doom Ps4')

    except Exception as e:
        print(f"Исключение: {type(e).__name__}")
        print(f"Содержимое: {str(e)}")
        traceback.print_exc()

        app.end()
