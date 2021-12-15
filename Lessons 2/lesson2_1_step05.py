# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# https://stepik.org/lesson/165493/step/5?unit=140087
import math
from selenium import webdriver


def calc(n):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # inp1 = browser.find_element_by_css_selector("#answer")
    x_element = browser.find_element_by_css_selector("span#input_value")
    # print("x_element= ", x_element)
    x = x_element.text
    y = calc(x)
    # print(y)
    inp1 = browser.find_element_by_css_selector("#answer")
    inp1.send_keys(y)

    ch_box = browser.find_element_by_css_selector("#robotCheckbox")
    ch_box.click()

    option = browser.find_element_by_css_selector("[for='robotsRule']")
    option.click()

    but = browser.find_element_by_css_selector("button")
    but.click()


finally:
    browser.quit()


