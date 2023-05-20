import time
from WB_common_consts import MPXPath
from WB_common_consts import MPID
from WB_common_consts import MPClass
from WB_common_consts import URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SearchResultPage import SearchResultPage

'''
TODO: вопросы:
1) стоит ли делать поисковую строку отдельным классом?
2)
'''


class SearchBar:
    """
    Класс, описывающий поисковую строку и ее функционал
    """
    def __init__(self, driver: webdriver):
        self.driver = driver

        '''
        while driver.execute_script("return document.readyState") != 'complete':
            print('not now')
            continue

        print('loaded')
        '''

        time.sleep(5) #TODO: костыль, который предотвращает сбрасывание текста из текстового поля после загрузки страницы
                        # Позволяет таким образом дождаться полной загрузки страницы

        self.search_block = driver.find_element(By.XPATH, MPXPath. search_block)
        self.search_box = driver.find_element(By.XPATH, MPXPath.search_box)
        self.search_button = driver.find_element(By.XPATH, MPXPath.search_button)

    def search_item(self, search_string: str) -> SearchResultPage:
        self.search_box.send_keys(search_string)
        self.search_button.click()

        # Инициализируем страницу с результатами поисковой выдачи
        search_page = SearchResultPage(self.driver)
        return search_page

class MainPage:
    """
    PageObject для главной страницы WB
    """

    def __init__(self, driver: webdriver):
        self.driver = driver
        driver.get(URL.WB_main_URL)

        # Инициализация элементов страницы
        self.search_bar = SearchBar(driver)
        # self.wb_logo_btn = driver.find_element(By.CLASS_NAME, MPClass.wb_main_logo_btn)

    # Сервисы, которые предоставляет главная страница WB
    def go_to_main_page(self):
        """
        Переход на главную страницу по клику на лого WB
        :return:
        """
        self.driver.get(URL.WB_main_URL)
        return

    def show_catalog(self):
        """
        Показать каталог по клике на кнопку Каталог
        :return:
        """
        return

    def search_item(self, search_title: str) -> SearchResultPage:
        """
        Поиск товара
        :param search_title: строка, по которой осуществляется поиск
        :return: PageObject для страницы с поисковой выдачей
        """
        return self.search_bar.search_item(search_title)

    def login(self):
        """
        Залогиниться в систему
        :return:
        """
        return

    def go_to_my_orders(self):
        """
        Переход на страницу моих заказов
        :return:
        """
        return

    def go_to_favourites(self):
        """
        Переход в категорию 'Избранное'
        :return:
        """
        return

    def go_to_basket(self):
        """
        Переход в корзину товаров
        :return:
        """
        return
