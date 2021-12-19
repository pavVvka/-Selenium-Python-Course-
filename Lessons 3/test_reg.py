# Задание: уникальность селекторов
# Как запускаете? В pycharm же есть встроенный терминал, и оттуда очень удобно командой запускать.
# Либо если через UI пробуете, надо запускать стрелочкой, напротив класса
# https://stepik.org/lesson/138920/step/11?unit=196194
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "first[required]").send_keys("Patrick")
    browser.find_element(By.CLASS_NAME, "second[required]").send_keys("Patch")
    browser.find_element(By.CLASS_NAME, "third[required]").send_keys("Patrick@gmail.com")
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    answer = browser.find_element(By.TAG_NAME, "h1").text
    browser.quit()
    return answer


class TestRegistrations(unittest.TestCase):
    def test_page1(self):
        lnk = "http://suninjuly.github.io/registration1.html"
        smpl = "Congratulations! You have successfully registered!"
        self.assertEqual(fill_form(lnk), smpl), "registration 1 not passed"

    def test_page2(self):
        lnk = "http://suninjuly.github.io/registration2.html"
        smpl = "Congratulations! You have successfully registered!"
        self.assertEqual(fill_form(lnk), smpl), "registration 2 not passed"


if __name__ == "__main__":
    unittest.main()





