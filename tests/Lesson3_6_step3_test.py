"""
https://stepik.org/lesson/237240/step/3?unit=209628
реализовать автотест со следующим сценарием действий:

    открыть страницу
    ввести правильный ответ
    нажать кнопку "Отправить"
    дождаться фидбека о том, что ответ правильный
    проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

"""
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# answer = math.log(int(time.time()))
# print(answer)
t = "Correct!"
# link = "https://stepik.org/lesson/236895/step/1"
link_base = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestUfo:
    def test_send_num(self, driver):
        driver.implicitly_wait(7)
        link = f"https://stepik.org/lesson/236895/step/1"
        driver.get(link)
        # time.sleep(7)
        driver.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()))))
        driver.find_element(By.CLASS_NAME, "submit-submission").click()
        # time.sleep(5)
        message = driver.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert message.text in t
        pass


