from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html' #https://suninjuly.github.io/selects2.html
browser = webdriver.Chrome()
browser.get(link)
try:
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    ans = str(num1 + num2)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(ans)

    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()
