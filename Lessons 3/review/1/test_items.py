import time


def test_find_add_to_cart_button(browser):
    # browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.get("https://google.com")

    assert browser.find_element_by_css_selector('.btn-add-to-basket')
    time.sleep(5)
