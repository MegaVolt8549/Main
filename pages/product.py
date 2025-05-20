from selenium.webdriver.common.by import By              # импортируем возможность искать элементы на странице



class ProductPage:


    def __init__(self, browser):                         # создаем функцию по переносу открытия браузера в тест
        self.browser = browser                           # сохраняем браузер для страницы



        def check_title_is(self, title):                                   # создаем функцию по проверке заголовка
            page_title = self.browser.find_element(By.CSS_SELECTOR,value='h2')  # находим новый элемент на новой странице (заголовок названия телефона)
            assert page_title.text == title                                     # делаем проверку, что название заголовка соответствует результату после == (которое передается в функцию)
