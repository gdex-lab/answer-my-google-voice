from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

# path to chrome driver
exec = "./chromedriver.exe"
#gmail
email_address = ""
#password
password = ""

from selenium.webdriver.chrome.options import Options

# Pass the argument 1 to allow and 2 to block
opt = Options()
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

driver = webdriver.Chrome(chrome_options=opt, executable_path=exec)

driver.get("https://voice.google.com/u/0/calls")
driver.find_elements_by_xpath("//*[contains(text(), 'Sign in')]")[0].click()

driver.switch_to.active_element.send_keys(email_address)
driver.switch_to.active_element.send_keys(Keys.RETURN)
time.sleep(2)
driver.switch_to.active_element.send_keys(password)
driver.switch_to.active_element.send_keys(Keys.RETURN)


def wait_for_call():
    incoming_call = False
    while not incoming_call:
        time.sleep(5)
        elem = driver.find_elements_by_xpath("//*[@aria-label='Answer call']")
        incoming_call = len(elem)
    print("Incomming call!")
    return elem[0]

while True:
    wait_for_call().click()
    time.sleep(10)

browser.quit()
