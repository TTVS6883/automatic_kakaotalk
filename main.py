from math import pi
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

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
countries_var = "Andorra"
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

# html scarping
soup = BeautifulSoup(driver.page_source, "lxml")

# scraping and phone_list append
phone_list = []
rows = soup.find("table", {"id": "getNumberTable"}).find_all(
    "input", {"class": "form-control"})

for row in rows:
    phone_list.append(row["value"])

# scraping and sms_list append
sms_list = []
rows = soup.find("table", {"id": "getNumberTable"}).find_all("strong")

for row in rows:
    sms_list.append(row.get_text())

# chrome tabs switch
driver.switch_to_window(driver.window_handles[1])
# driver.switch_to_window(driver.window_handles[0])
time.sleep(0.5)

# ip address click
driver.find_element_by_css_selector(
    'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)').click()
time.sleep(1)

# country click
driver.find_element_by_css_selector(
    'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div:nth-child(1) > div.sx-form__row-content > div > button').click()
time.sleep(1)

# country search click and sendkeys
driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.content-mwrap.flex.flex--wrap.targets-container.ip-port-targets > div:nth-child(2) > div > div > div').click()
time.sleep(1)
driver.find_element_by_css_selector(
    'div.tooltip__inner > div.sx-select__search > input').clear()
driver.find_element_by_css_selector(
    'div.tooltip__inner > div.sx-select__search > input').send_keys(countries_var)
driver.find_element_by_css_selector(
    'div.tooltip__inner > div.sx-select__list.ps').click()

# number of ports set
port_var = 3
driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.lbl-param-list > div > div > input').clear()
driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.lbl-param-list > div > div > input').send_keys(port_var)

# save button click
driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.flex.flex--justify.flex--wrap.content-mwrap > button.button.button--04.package__form-btn.margin--t.add-filter-save').click()

# scraping port list
soup = BeautifulSoup(driver.page_source, "lxml")

# scraping and port list append
rows = soup.find_all("div", {"class": "sx-form__item ip-port"})
port_list = []
port_index = 0

for row in rows:

    country_rows = row.find_all("div", {"class": "ip-port__country"})

    for country_row in country_rows:

        if (countries_var == country_row.get_text().strip()):
            print("같음")
            break
        print("반복중")
        port_index += 1

    port_rows = row.find_all("div", {"class": "ip-port__info"})

    for port_row in port_rows:

        port_list.append(port_row.get_text().strip())

print(port_index)

print(port_list[port_index])
