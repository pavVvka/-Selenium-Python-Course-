import math
import time
from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"


def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    el = browser.find_element_by_xpath("//img[@valuex]")
    # el = browser.find_element_by_css_selector("[valuex]")
    # el = browser.find_element_by_css_selector("img")
    print(el.get_attribute("valuex"))
    code = el.get_attribute("valuex")
    x = calc(code)
    print("code= ", code, type(code))
    answ = browser.find_element_by_id("answer")

    answ.send_keys(x)

    chbx = browser.find_element_by_css_selector("#robotCheckbox")
    chbx.click()
    rule = browser.find_element_by_css_selector('[id="robotsRule"]')
    rule.click()
    buttn = browser.find_element_by_css_selector("button")
    buttn.click()

    # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
    # for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
    #     browser.find_element_by_css_selector(selector).click()


    time.sleep(7)
finally:
    browser.quit()




