from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    ans = str(math.log(abs(12*math.sin(int(x)))))

    text = browser.find_element(By.ID, 'answer')
    text.send_keys(ans)

    checkbox_type = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_type.click()

    #Проверим значение по-умолчанию
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute('checked')
    #<input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>
    # Напечатает ruler, т.е. текстовое значение аттрибута
    print(people_radio.get_attribute("name"))

    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.
    print(people_radio.get_attribute("checked"))
    
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.
    print(people_radio.get_attribute("href"))
    
    assert people_checked is not None, "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    radiobutton_type = browser.find_element(By.ID, 'robotsRule')
    radiobutton_type.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
