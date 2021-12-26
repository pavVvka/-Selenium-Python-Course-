import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru es fr etc.")


@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    # chrome_options.add_argument("--user-data-dir=K:\\chrome_profiles\\qa_chrome")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(f"--lang={language}")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # driver = webdriver.Chrome('../../bin/chromedriver96.exe', options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
