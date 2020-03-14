from selenium.webdriver.common.by import By
import time

def test_guest_can_register(browser):
    browser.implicitly_wait(3)
    browser.maximize_window()
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()
    email = str(time.time())+"@fakemail.org"
    passw = "GhbdtnCntgbr123"
    browser.find_element(By.ID, "id_registration-email").send_keys(email)
    browser.find_element(By.ID, "id_registration-password1").send_keys(passw)
    browser.find_element(By.ID, "id_registration-password2").send_keys(passw)
    browser.find_element(By.NAME, "registration_submit").click()
    text = browser.find_element(By.CSS_SELECTOR, ".alertinner.wicon").text
    assert text == "Спасибо за регистрацию!" or text == "Thanks for registering!", "Unsuccessful registration"

