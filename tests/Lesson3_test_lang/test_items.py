import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link1 = "https://google.com"  # линк без кнопки - для проверки сообщения от assert


def test_button_add_to_cart(browser):
    browser.get(link)
    ast = None
    time.sleep(5)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except:
        assert ast, ">!< There is no button 'Add To Cart' at page"

    # buttons = browser.find_elements_by_css_selector(".btn-add-to-basket")
    # assert len(buttons) > 0, "No button for add"
