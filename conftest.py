from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None, help='Choose browser')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name=='Chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'Firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    browser.quit()

# commands:
# >pytest --browser=Chrome  --alluredir=allure_report  test_make_report.py
# >allure serve allure_report










