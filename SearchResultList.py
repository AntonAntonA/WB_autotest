from selenium import webdriver
from selenium.webdriver.common.by import By

import WB_common
from ItemCardSearchResult import ItemCardSearchResult
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultList:
    def __init__(self, driver, page_num=1):
        self.driver = driver

        # CSS Классы товарных карточек
        self.card_classes = ['product-card j-card-item j-good-for-listing-event',
                             'product-card j-card-item']

        self.card_div_xpath = '(// div[@class =\'product-card__wrapper\'])'

        self.cur_page_num = page_num

        # Загружаем все содержимое страницы путем прокрутки ее до конца
        WB_common.scroll_page_to_end_and_return_to_start(self.driver)

        self.item_cards_count = len(self.driver.find_elements(By.XPATH, self.card_div_xpath))
        return

    def get_item_cards_count(self) -> int:
        return self.item_cards_count

    def get_item_card(self, index: int) -> ItemCardSearchResult:
        if 0 <= index <= self.get_item_cards_count():
            return ItemCardSearchResult(self.driver, index)
        else:
            raise ValueError(f'SearchResultPage.get_item(): bad index {index}')
