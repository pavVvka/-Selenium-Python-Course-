# Задание: уникальность селекторов
# Как запускаете? В pycharm же есть встроенный терминал, и оттуда очень удобно командой запускать.
# Либо если через UI пробуете, надо запускать стрелочкой, напротив класса
# https://stepik.org/lesson/138920/step/11?unit=196194
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     inp1 = browser.find_element_by_css_selector(".first_block .first")
#     inp1.send_keys("Patrick")
#     inp2 = browser.find_element_by_css_selector(".second")
#     inp2.send_keys("Patch")
#     inp3 = browser.find_element_by_css_selector(".form-control.third")
#     inp3.send_keys("Patrick@gmail.com")
#
#     button = browser.find_element_by_css_selector("button.btn")  # Отправляем заполненную форму
#     button.click()
#     time.sleep(1)  # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
#     welcome_text_elt = browser.find_element_by_tag_name("h1")  # находим элемент, содержащий текст
#     welcome_text = welcome_text_elt.text  # записываем текст из элемента welcome_text_elt
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(5)  # ожидание чтобы визуально оценить результаты прохождения скрипта
#     browser.quit()  # закрываем браузер после всех манипуляций
#


# link1 = "http://suninjuly.github.io/registration1.html"
# link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
# browser.get(link)


class test_inputs_submit(unittest.TestCase):
    def test_page1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element(By.CLASS_NAME, "first").send_keys("Patrick")
        browser.find_element(By.CLASS_NAME, "second").send_keys("Patch")
        browser.find_element(By.CLASS_NAME, "third").send_keys("Patrick@gmail.com")
        browser.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        txt = browser.find_element(By.TAG_NAME, "h1").text
        smpl = "Congratulations! You have successfully registered!"
        self.assertEqual(txt, smpl), "registration 1 not passed"
        browser.quit()


    def test_page2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element(By.CLASS_NAME, "first[required]").send_keys("Patrick")
        browser.find_element(By.CLASS_NAME, "second[required]").send_keys("Patch")
        browser.find_element(By.CLASS_NAME, "third[required]").send_keys("Patrick@gmail.com")
        browser.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        txt = browser.find_element(By.TAG_NAME, "h1").text
        smpl = "Congratulations! You have successfully registered!"
        self.assertEqual(txt, smpl), "registration 2 not passed"
        browser.quit()


if __name__ == "__main__":
    unittest.main()





