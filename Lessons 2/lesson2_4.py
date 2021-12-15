# https://stepik.org/lesson/181384/step/5?unit=156009

#  ===========   Selenium Waits (Implicit Waits)
#                   browser.implicitly_wait(5)

# Ожидание называется неявным (Implicit wait), так как его не надо явно указывать
# каждый раз, когда мы выполняем поиск элементов, оно автоматически будет
# применяться при вызове каждой последующей команды

# exceptions:

# >>> Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
# >>> Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
# то получим StaleElementReferenceException. Например, мы нашли элемент
# Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click.
# Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно
# — элемент "устарел" (stale) и мы увидим исключение.
# >>> Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.




#   ================ Explicit Waits (WebDriverWait и expected_conditions)
#                             явные ожидания

# Однако методы find_element проверяют только то, что элемент появился на странице.
# В то же время элемент может иметь дополнительные свойства
#
#    Кнопка может быть неактивной, то есть её нельзя кликнуть;
#    Кнопка может содержать текст, который меняется;
#    Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.

# Чтобы тест был надежным, нам нужно дождаться, когда кнопка станет кликабельной.
# Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных ожиданий

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))

# # говорим Selenium проверять в течение 5 секунд пока кнопка станет НЕактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

# # WebDriverWait используется функция until, в которую передается правило ожидания, элемент,
# # а также значение, по которому мы будем искать элемент.
# В модуле expected_conditions есть много других правил, которые позволяют реализовать
# необходимые ожидания:
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

#     title_is
#     title_contains
#     presence_of_element_located
#     visibility_of_element_located
#     visibility_of
#     presence_of_all_elements_located
#     text_to_be_present_in_element
#     text_to_be_present_in_element_value
#     frame_to_be_available_and_switch_to_it
#     invisibility_of_element_located
#     element_to_be_clickable
#     staleness_of
#     element_to_be_selected
#     element_located_to_be_selected
#     element_selection_state_to_be
#     element_located_selection_state_to_be
#     alert_is_present

import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
# time.sleep(1)
browser.implicitly_wait(5)  # искать каждый элемент в течение 5 секунд

button = browser.find_element_by_id("verify")
button.click()

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))



message = browser.find_element_by_id("verify_message")
print(message, type(message))
time.sleep(7)
assert "successful" in message.text

browser.quit()

