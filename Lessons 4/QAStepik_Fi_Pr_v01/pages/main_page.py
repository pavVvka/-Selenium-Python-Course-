from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # def go_to_login_page(self):
    #     # login_link = browser.find_element_by_css_selector("#login_link")
    #     # login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     # login_link.click()
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы
        # с браузером, а в качестве url передаем текущий адрес.

    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is absent"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
