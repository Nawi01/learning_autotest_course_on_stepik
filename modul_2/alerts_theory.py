from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ''
browser = webdriver.Chrome()
browser.get(link)

#Получить текст из алерта
alert = browser.switch_to.alert
alert_text = alert.text
#Принять алерт
alert = browser.switch_to.alert
alert.accept()
#Отказ, если есть
confirm = browser.switch_to.alert
confirm.dismiss()
#Ввод в окно алерта
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()