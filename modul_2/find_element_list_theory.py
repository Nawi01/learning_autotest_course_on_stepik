from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

#Неудобный способ рабоы со списками
# browser.find_element(By.TAG_NAME, 'select').click()
# browser.find_element(By.CSS_SELECTOR, '[value="1"]').click()

#Работа со списком через класс Select
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value("1")

# select.select_by_visible_text("text") - ищет элемент по видимому тексту
#select.select_by_index(index) - ищет элемент по его индексу или порядковому номеру