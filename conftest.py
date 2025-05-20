from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options  # импортирует фишки фаерфокса




@pytest.fixture()                   # создаем предусловия
def browser():                      # создаем функцию, обычно она называется driver
    options = Options()
    options.add_argument('--headless')  # делаем тесты без визуального вылета браузера
    browser = webdriver.Firefox(options=options)   # открываем браузер firefox
    browser.maximize_window()       # разворачиваем окно на весь экран
    browser.implicitly_wait(3)      # после открытия браузера делаем задержку в 3 секунды перед следующим действием
    yield browser                   # возращаем результат функции, браузер
    browser.close()                 # постусловия, закрываем браузер после выполнения тестов