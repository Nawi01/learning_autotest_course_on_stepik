from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    browser.find_element(By.NAME, 'firstname').send_keys('Текст')
    browser.find_element(By.NAME, 'lastname').send_keys('Текст')
    browser.find_element(By.NAME, 'email').send_keys('Текст')

    file_path = 'C:\\Users\\PC\\Desktop\\autotests_on_stepik\\upload_file.txt'
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
