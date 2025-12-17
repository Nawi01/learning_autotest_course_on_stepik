from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    ans = str(math.log(abs(12*math.sin(int(x)))))

    text = browser.find_element(By.ID, 'answer')
    text.send_keys(ans)

    checkbox_type = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_type.click()

    radiobutton_type = browser.find_element(By.ID, 'robotsRule')
    radiobutton_type.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
