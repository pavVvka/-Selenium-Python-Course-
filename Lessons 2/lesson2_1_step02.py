# 2.1 Основные методы Selenium
# Как работать с элементами типа checkbox и radiobutton?
# https://stepik.org/lesson/165493/step/2?unit=140087


# Checkbox (чекбокс или флажок) - мультивыбор
# radiobutton (радиобаттон или переключатель)

"""
<input type="checkbox" checked>
<input type="radio" name="language" value="python" checked>
<input type="radio" name="language" value="selenium">


Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию из
группы radiobuttons, надо указать WebDriver метод поиска элемента и
выполнить для найденного элемента метод click():

option1 = browser.find_element_by_css_selector("[value='python']")
option1.click()

Также вы можете увидеть тег label рядом с input.
Этот тег используется, чтобы сделать кликабельным текст,
который отображается рядом с флажком. Этот текст заключен внутри тега label.
Элемент label связывается с элементом input с помощью атрибута for,
в котором указывается значение атрибута id для элемента input:

<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
<div>
  <input type="radio" id="java" name="language">
  <label for="java">Java</label>
</div>

В этом случае можно также отметить нужный пункт с помощью WebDriver,
выполнив метод click() на элементе label.

option1 = browser.find_element_by_css_selector("[for='java']")
option1.click()

"""

"""
атрибут .text для найденного элемента:

x_element = browser.find_element_by_ ...(selector)
x = x_element.text
y = calc(x)

Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
Например, text для элемента <div class="message">У вас новое сообщение.</div> вернёт строку: 
    "У вас новое сообщение".

"""

"""
> проверить значение атрибута checked у элемента radiobuttons. 
Вот HTML-код элемента:
<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

> Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element_by_id("peopleRule")

> Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

Т.к. у данного атрибута значение не указано явно, то метод get_attribute вернёт "true". 
( "true" написано с маленькой буквы, — все методы WebDriver 
взаимодействуют с браузером с помощью JavaScript, 
в котором булевые значения пишутся с маленькой буквы, а не с большой, как в Python. )

Мы можем написать проверку другим способом, сравнив строки:
assert people_checked == "true", "People radio is not selected by default"

Если атрибута нет, то метод get_attribute вернёт значение None. 
Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует.

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None


Так же мы можем проверять наличие атрибута disabled, который определяет, 
может ли пользователь взаимодействовать с элементом. 
Например, в предыдущем задании на странице с капчей для роботов JavaScript 
устанавливает атрибут disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.

<button type="submit" class="btn btn-default" disabled>Submit</button>

"""

#  <input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

people_radio = browser.find_element_by_id("peopleRule")

print(people_radio.get_attribute("name"))
# Напечатает ruler, т.е. текстовое значение аттрибута

print(people_radio.get_attribute("checked"))
# Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

print(people_radio.get_attribute("href"))
# Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.


#  >>.>


from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла