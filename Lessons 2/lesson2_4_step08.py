"""
    1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    3. Нажать на кнопку "Book"
    4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exc
link = "http://suninjuly.github.io/explicit_wait2.html"
bros = webdriver.Chrome()
bros.get(link)

btn = bros.find_element(By.ID, "book")

WebDriverWait(bros, 12).until(exc.text_to_be_present_in_element((By.ID, "price"), "100"))
btn.click()
bros.execute_script("return arguments[0].scrollIntoView(true);", btn)
num = bros.find_element(By.ID, "input_value")
print("num", num)
x = str(math.log(abs(12 * math.sin(int(num.text)))))
ans = bros.find_element(By.ID, "answer")
ans.send_keys(x)
bros.find_element(By.ID, "solve").click()

time.sleep(10)
bros.quit()

