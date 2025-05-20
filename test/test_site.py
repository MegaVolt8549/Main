# запустить тест можно в консоли командой: pytest test_site.py если будет много тестов, они запустятся все
# запустить определенный тест из определенного файла: pytest test_site.py::test_open_s6

from selenium.webdriver.common.by import By  # импортируем методы поиска на странице, в скобках файнд.элемент
import time
from pages.homepage import HomePage      # импортируем из файла созданный класс
from  pages.product import ProductPage   # импортируем из файла созданный класс


def test_open_s6(browser):                                      # создаем функцию (тест) для открытия ссылки на телефон
    homepage = HomePage(browser)                                # сохраняем браузер класса в созданную переменную
    homepage.open()                                             # открываем страницу
    homepage.click_galaxy_s6()                                  # кликаем на ссылку
    product_page = ProductPage(browser)                         # появилась страница product принимает браузер
    product_page.check_title_is('Samsung galaxy s6')            # находим новый элемент на странице






def test_two_monitors(browser):                                          # создаем функцию (тест) для открытия ссылки мониторы
    browser.get('https://demoblaze.com/index.html')                      # открываем браузер с адресом сайта в скобках
    monitor_link = browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''') # находим ссылку на нужный элемент
    monitor_link.click()                                                 # кликаем на ссылку, найденную выше (мониторы)
    time.sleep(3)                                                        # делаем задержку в 3 секунды
    monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')     # находим элементы на новой странице
    assert len(monitors) == 2                                            # делаем проверку, что записей реально 2