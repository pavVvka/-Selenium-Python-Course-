import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

bros = webdriver.Chrome()
bros.get(link)
dat = ["Pavel", "Kuz", "Pavel@gml.com"]
name = bros.find_element(By.NAME, "firstname")
name.send_keys(dat[0])
sname = bros.find_element(By.NAME, "lastname")
sname.send_keys(dat[1])
email = bros.find_element(By.NAME, "email")
email.send_keys(dat[2])
dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir, 'lesson2_2_step08.txt')
btn = bros.find_element(By.ID, "file")
btn.send_keys(file_path)
sbmt = bros.find_element(By.TAG_NAME, "button")
sbmt.click()
time.sleep(6)
bros.quit()



# for elem_name in ["firstname", "lastname", "email"]:
#     browser.find_element_by_name(elem_name).send_keys(elem_name)