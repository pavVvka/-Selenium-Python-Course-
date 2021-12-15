import math
import time
from selenium import webdriver
link = "http://suninjuly.github.io/find_link_text"
print(str(math.ceil(math.pow(math.pi, math.e)*10000)))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    lnk = browser.find_element_by_link_text("224592")
    lnk.click()
    inp1 = browser.find_element_by_tag_name("input")
    inp1.send_keys("Ivan")
    inp2 = browser.find_element_by_name("last_name")
    inp2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
