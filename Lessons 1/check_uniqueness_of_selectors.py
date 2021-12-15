import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля

# Заполнение поля "Имя"
nameInput = browser.find_element(By.CSS_SELECTOR, ".first_class [placeholder='Input your first name']")
nameInput.send_keys("Мария")

# Заполнение поля "Фамилия"
lastnameInput = browser.find_element(By.CSS_SELECTOR, ".second_class [placeholder='Input your last name']")
lastnameInput.send_keys("Марьина")

# Заполнение поля "Email"
emailInput = browser.find_element(By.CSS_SELECTOR, ".third_class [placeholder='Input your email']")
emailInput.send_keys("maria@testmail.com")

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
browser.close()
browser.quit()
