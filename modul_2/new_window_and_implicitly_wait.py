from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link)

try:
    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.window(browser.window_handles[1]) #browser.window_handles = массив открытых вкладок

    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(ans)

    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()