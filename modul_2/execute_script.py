from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
try:
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(ans)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()