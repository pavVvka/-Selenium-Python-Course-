"""
https://stepik.org/lesson/237240/step/3?unit=209628
реализовать автотест со следующим сценарием действий:

    открыть страницу
    ввести правильный ответ
    нажать кнопку "Отправить"
    дождаться фидбека о том, что ответ правильный
    проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

Используйте осмысленное сообщение об ошибке в проверке текста,
а также настройте нужные ожидания, чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания.
Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!"
Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том,
что у вас установлено правильное локальное время (https://time.is/ru/).
Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.

"""
# Через WebDriverWait EC.element_to_be_clickable находим класс кнопку


import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# answer = math.log(int(time.time()))
# print(answer)
t = "Correct!"
link_dat = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
answer = []


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print("\nUFO message: ", "".join(answer))


@pytest.mark.parametrize("datalink", link_dat)
class TestUfo:
    def test_send_num(self, browser, datalink):
        browser.implicitly_wait(7)
        link = f"https://stepik.org/lesson/{datalink}/step/1"
        browser.get(link)
        browser.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        if message not in t:
            answer.append(message)
        assert message in t, "UFO activity detected... recording incoming message"

