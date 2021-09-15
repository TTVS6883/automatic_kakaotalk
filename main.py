import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# cmd cd C:\Program Files\Google\Chrome\Application
# cmd chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"

# chrome launch
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"  # Your Chrome Driver path
driver = webdriver.Chrome(
    executable_path=chrome_driver, options=chrome_options)
driver.implicitly_wait(10)

# countries dropdown click
driver.find_element_by_css_selector(
    '.statusBtn.btn.dropdown-toggle.btn-primary').click()
time.sleep(2)

# countries search click and sendkeys
countries_var = "Mexico"
driver.find_element_by_css_selector('.form-control.countriesSearch').clear()
driver.find_element_by_css_selector(
    '.form-control.countriesSearch').send_keys(countries_var)
time.sleep(2)

# countries choose click
driver.find_element_by_css_selector('.countryChoose').click()
time.sleep(2)

# service search click and sendkeys
service_var = "Kakao"
driver.find_element_by_css_selector('#servicesSearch').clear()
driver.find_element_by_css_selector('#servicesSearch').send_keys(service_var)
time.sleep(5)

# kakaotalk service click
driver.find_element_by_css_selector('#leftForm').click()
driver.find_element_by_css_selector(
    '.table.table-hover.table-stripped.table-condensed.table-small.tabbed').click()

# kakaotalk service set and buy
device_var = 2
driver.find_element_by_css_selector('.form-control.numbersToBuy').click()
driver.find_element_by_css_selector(
    '.form-control.numbersToBuy').send_keys(Keys.BACKSPACE)
driver.find_element_by_css_selector(
    '.form-control.numbersToBuy').send_keys(device_var)
driver.find_element_by_css_selector(
    '.table.table-hover.table-stripped.table-condensed.table-small.tabbed').click()

# phonenumber copy
