class URL:
    """
    Список URL адресов, которые используются в проекте
    """
    WB_main_URL = 'https://www.wildberries.ru/'

class MPClass:
    """
    Список классов элементов галвной страницы
    """
    search_box = "a3aj search-bar-wrapper"
    wb_main_logo_btn = 'nav-element__burger j-menu-burger-btn j-wba-header-item'

class MPID:
    """
    Список айдишников элементов галвной страницы
    """
    search_box = 'searchInput'
    search_button = 'applySearchBtn'

class MPXPath:
    """
    Список Xpath элементов главной страницы
    """
    search_block = '//*[@id="searchBlock"]'
    search_box = '//*[@id="searchInput"]'
    search_button = '//*[@id="applySearchBtn"]'
    wb_main_logo_btn = '/html/body/div[1]/header/div/div[2]/div[1]/a'