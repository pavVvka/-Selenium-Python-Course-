import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
link = "http://suninjuly.github.io/redirect_accept.html"

bros = webdriver.Chrome()
bros.get(link)
bros.find_element(By.TAG_NAME, "button").click()
for i in bros.window_handles:
    print(i)
win1 = bros.window_handles[2]
win0 = bros.window_handles[0]
bros.switch_to.window(win1)
num = bros.find_element(By.ID, "input_value")
x = str(math.log(abs(12 * math.sin(int(num.text)))))
bros.find_element(By.ID, "answer").send_keys(x)
bros.find_element(By.TAG_NAME, "button").click()
time.sleep(7)
bros.quit()
