"""
                        Работа со списками

Посмотрим, как выглядит html для списка:

<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Python</option>
 <option value="2">Java</option>
 <option value="3">JavaScript</option>
</select>

from selenium import webdriver

browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()

Последняя строчка может выглядеть и так:

browser.find_element_by_css_selector("[value='1']").click()

Есть более удобный способ, для которого используется специальный класс Select
из библиотеки WebDriver. Вначале мы должны инициализировать новый объект,
передав в него WebElement с тегом select.
Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

Можно использовать еще два метода: select.select_by_visible_text("text")
и select.select_by_index(index). Первый способ ищет элемент по видимому тексту,
например, select.select_by_visible_text("Python") найдёт "Python"
для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру.
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
нужно использовать select.select_by_index(1),
так как опция с индексом 0 в данном примере имеет значение
по умолчанию равное "--".
"""

"""
                Метод execute_script

С помощью метода execute_script можно выполнить программу,
написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере.

from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

browser.execute_script("document.title='Script executing';")
browser.execute_script("document.title='Script executing';alert('Robots at work');")


          Пример задачи для execute_script

Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть
на элемент, который внезапно оказывается перекрыт другим элементом на странице.
https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

browser.execute_script("window.scrollBy(0, 100);")

"""

"""
               Загрузка файлов
https://docs.python.org/3/library/os.path.html


import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)

Элемент в форме, который выглядит, как кнопка добавления файла,
имеет атрибут type="file".
Мы должны сначала найти этот элемент с помощью селектора,
а затем применить к нему метод send_keys(file_path).
"""

