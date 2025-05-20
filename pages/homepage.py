from selenium.webdriver.common.by import By              # импортируем возможность искать элементы на странице


class HomePage:                                          # создаем класс для главной страницы

    def __init__(self, browser):                         # создаем функцию по переносу открытия браузера в тест
        self.browser = browser                                    # сохраняем браузер для страницы

    def open(self):                                      # создаем функцию по открытию страницы
        browser.get('https://demoblaze.com/index.html')  # открываем браузер с адресом сайта в скобках

    def click_galaxy_s6(self):                                                               # создаем функцию по клику на s6
        galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')  # находим ссылку на нужный элемент на сайте, телефон галакси
        galaxy_s6.click()                                                                    # кликаем на ссылку, найденную выше