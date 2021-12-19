"""
========================    Автоиспользование фикстур
https://stepik.org/lesson/237257/step/6?unit=209645

При описании фикстуры можно указать дополнительный параметр autouse=True,
который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:
test_fixture_autouse.py

 фикстура подготовки данных выполнилась без явного вызова.
 Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов.
 Без явной необходимости автоиспользованием фикстур лучше не пользоваться.
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\n-> start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\n-> quit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print(">>>>! preparing some critical data for every test")


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
