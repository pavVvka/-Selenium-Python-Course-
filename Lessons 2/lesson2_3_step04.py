import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/alert_accept.html"
bros = webdriver.Chrome()
bros.get(link)
bros.find_element(By.TAG_NAME, "button").click()
alert = bros.switch_to.alert
alert.accept()
num = bros.find_element(By.ID, "input_value")
x = str(math.log(abs(12 * math.sin(int(num.text)))))
bros.find_element(By.ID, "answer").send_keys(x)
bros.find_element(By.TAG_NAME, "button").click()

time.sleep(7)
bros.quit()

