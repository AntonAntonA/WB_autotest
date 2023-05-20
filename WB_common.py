import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def is_element_visible(driver, element):
    """
    Функция проверяет, видим ли елемент в окне браузера. Предполагается, что элемент предварительно получен
    с помощью find_element и уже прогрузился на странице
    :param
        element: элемент, видимость которого нужно узнать
        driver: Selenium веб драйвер
    :return:
        True если элемент виден в окне
        False если элемент не виден в окне
    """

    script = """
    function isElementVisible(element) {
      var rects = element.getClientRects();
      for (var i = 0; i < rects.length; i++) {
        var rect = rects[i];
        if (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        ) {
          return true;
        }
      }
      return false;
    }

    // Вызов функции и возврат результата
    return isElementVisible(arguments[0]);
    """

    # Выполнение скрипта и получение результата
    return driver.execute_script(script, element)


def scroll_to_element(driver, element):
    """
    Метод скроллит страницу до того момента, пока нужный элемент страницы не будет виден
    :param:
        element: элемент, видимость которого нужно узнать
        driver: Selenium веб драйвер
    :return:
    """

    script = """
        function scrollPage(element) {
            var rect = element.getBoundingClientRect();

            // Получаем текущие координаты позиции просмотра страницы
            var xPosition = window.pageXOffset;
            var yPosition = window.pageYOffset;
            
            window.scrollBy(rect.left - xPosition, rect.top - yPosition);
        }
        
        // Вызов функции и возврат результата
        scrollPage(arguments[0]);
        """

    action = ActionChains(driver)
    action.send_keys(Keys.HOME).perform()
    driver.execute_script(script, element)

    # Прокручиваем страницу вниз до тех пор, пока элемент не окажется виден в окне
    # while not is_element_visible(driver, element):
    #     # Прокрутить страницу вниз на одну страницу
    #     driver.execute_script(script, element)

    return

    # actions = ActionChains(driver)
    #
    # while not is_element_visible(driver, element):
    #     # Прокрутить страницу вниз на одну страницу
    #     actions.send_keys(Keys.PAGE_DOWN).perform()

    # return

def scroll_page_to_end_and_return_to_start(driver):
    '''
    Функция скроллит страницу до самого конца, пока не подгрузится все ее содержимое, а потом возвращает
    позицию в начало страницы. Таким образом мы загрузим все содержимое страницы.
    :param driver: объект веб-драйвер
    :return:
    '''

    action = ActionChains(driver)
    i = 0
    while True:
        print('scroll num = {i}')
        # Запоминаем текущую позицию прокрутки страницы
        old_position = driver.execute_script("return window.pageYOffset;")

        # Прокручиваем страницу вниз
        action.send_keys(Keys.PAGE_DOWN).perform()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        # Ждем некоторое время, чтобы страница загрузила новое содержимое
        # Вместо time.sleep() можно использовать явное ожидание на ваше усмотрение
        time.sleep(2)

        # Запоминаем новую позицию прокрутки страницы
        new_position = driver.execute_script("return window.pageYOffset;")

        # Если новая и старая позиции прокрутки равны, значит, достигнут конец страницы
        if new_position == old_position:
            break
        i += 1

    print('boom')
    # Возвращаемся в начало страницы
    action.send_keys(Keys.HOME).perform()
