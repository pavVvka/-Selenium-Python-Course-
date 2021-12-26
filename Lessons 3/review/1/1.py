# https://github.com/itsanti/stepik_courses/tree/master/course_575/lesson36_shop




"""
============================================== short test summary info ==============================================
ERROR test_items.py::test_find_add_to_cart_button - selenium.common.exceptions.WebDriverException: Message: 'chrome...

================================================= 1 error in 0.53s ==================================================



E                       selenium.common.exceptions.WebDriverException: Message: 'chromedriver96.exe' executable needs
to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home


далее могли бы быть все оценки нолями...
- пришлось переписывать все ссылки с путями
- игры с .add_argument() в данном задании лишние


В таком варианте assert никак не вызовется.
Если интересно, я сделал так:
a = None
    try:
        browser.find_element_.........
    except:
        assert a, "no button"


"""



