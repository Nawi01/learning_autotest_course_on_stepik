from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.alert.accept()

    time.sleep(3)
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(ans)

    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()
