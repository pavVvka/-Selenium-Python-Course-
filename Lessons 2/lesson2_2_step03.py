from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
# <span class="nowrap" id="num1">29</span>

link = "http://suninjuly.github.io/selects1.html"
bro = webdriver.Chrome()
bro.get(link)
# n1 = int(bro.find_element_by_css_selector("#num1").text)
# n2 = int(bro.find_element_by_css_selector("#num2").text)
num = 0
for el in ["#num1", "#num2"]:
    num += int(bro.find_element_by_css_selector(el).text)
print(num, type(num))

select = Select(bro.find_element_by_tag_name("select"))
select.select_by_value(str(num))
btn = bro.find_element_by_css_selector("button").click()
# btn.click()

time.sleep(5)
bro.quit()

