from selenium import webdriver
from selenium.webdriver.common.by import By
from ItemCardSearchResult import ItemCardSearchResult
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SearchResultList import SearchResultList

class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

        #Кнопка, открывающяя следующую страницу поисковой выдачи
        self.next_page_btn_class = 'pagination-next pagination__next'

        #Формируем список из поисковой выдачи
        self.search_results = SearchResultList(driver)
        return

    def go_to_next_page(self):
        #Ищем кнопку "Следующая страница"
        self.next_page_btn.click()
        self.search_results = SearchResultList(self.driver)

    def go_to_page(self, page_num):
        '''
        Метод по номеру открывает определенную страницу поисковой выдачи
        :param page_num: номер страницы, на которую нужно перейти
        :return: страница поисковой выдачи SearchResultList, соотвествующая номеру page_num
        '''
        return

    def get_items_count_on_cur_page(self):
        return self.search_results.get_item_cards_count()

    def get_item(self, item_num):
        return self.search_results.get_item_card(item_num)
