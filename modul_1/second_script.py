from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'https://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)
#Прописать заполнение полей
    first_name = browser.find_element(By.CLASS_NAME, 'first')
    first_name.send_keys('Имя')
    second_name = browser.find_element(By.CLASS_NAME, 'second')
    second_name.send_keys('Фамилия')
    third_name = browser.find_element(By.CLASS_NAME, 'third')
    third_name.send_keys('Email')
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    #accert - это проверка 
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(2)
    browser.quit()

