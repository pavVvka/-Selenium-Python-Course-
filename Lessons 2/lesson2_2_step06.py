import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
bros = webdriver.Chrome()
bros.get(link)
num = bros.find_element_by_id("input_value")
print(int(num.text))
x = calc(int(num.text))
print(x)
btn = bros.find_element_by_tag_name("button")
bros.execute_script("return arguments[0].scrollIntoView(true);", btn)
ans = bros.find_element_by_css_selector("#answer")
ans.send_keys(x)
chk = bros.find_element_by_tag_name("label.form-check-label")
chk.click()
rule = bros.find_element_by_id("robotsRule")
bros.execute_script("return arguments[0].scrollIntoView(true);", rule)
rule.click()
btn = bros.find_element_by_tag_name("button")
btn.click()
time.sleep(5)
bros.quit()


