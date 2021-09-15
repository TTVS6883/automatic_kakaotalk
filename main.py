from math import pi
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

# cmd cd C:\Program Files\Google\Chrome\Application
# cmd chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"

# variable
device_var = 5
port_var = 5
countries_var = "Angola"

# chrome launch
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"  # Your Chrome Driver path
driver = webdriver.Chrome(
    executable_path=chrome_driver, options=chrome_options)
driver.implicitly_wait(10)

# countries dropdown click
elem = driver.find_element_by_css_selector(
    '.statusBtn.btn.dropdown-toggle.btn-primary')
ActionChains(driver).click(elem).perform()

# countries search click and sendkeys
elem = driver.find_element_by_css_selector('.form-control.countriesSearch')
elem.clear()
ActionChains(driver).click(elem).send_keys(countries_var).perform()
time.sleep(1)

# countries choose click
elem = driver.find_element_by_css_selector('.countryChoose')
ActionChains(driver).click(elem).perform()

# service search click and sendkeys
service_var = "Kakao"
elem = driver.find_element_by_id('servicesSearch')
elem.clear()
ActionChains(driver).send_keys_to_element(elem, service_var).perform()
time.sleep(2)

# kakaotalk service click
elem = driver.find_element_by_css_selector(
    '.table.table-hover.table-stripped.table-condensed.table-small.tabbed')
ActionChains(driver).click(elem).perform()
time.sleep(0.5)

# kakaotalk service set
elem = driver.find_element_by_css_selector('.form-control.numbersToBuy')
elem.clear()
ActionChains(driver).click(elem).send_keys(device_var).perform()
time.sleep(0.5)

# kakaotalk service buy
elem = driver.find_element_by_css_selector(
    '#leftForm > table > tbody > tr.tabbed.cell.info > td.radiotd > label > div > a')
ActionChains(driver).move_to_element(elem).click().perform()
time.sleep(15)

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

# selenium page switch
driver.get("https://dashboard.soax.com/proxy")

# ip address click
elem = driver.find_element_by_css_selector(
    'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
ActionChains(driver).click(elem).perform()
time.sleep(0.5)

# add filter click
elem = driver.find_element_by_css_selector('.ip-port__add-new-text')
ActionChains(driver).click(elem).perform()
time.sleep(0.5)

# country click
elem = driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.content-mwrap.flex.flex--wrap.targets-container.ip-port-targets > div:nth-child(2) > div > div > div')
ActionChains(driver).click(elem).perform()

# country search click and sendkeys
elem = driver.find_element_by_css_selector(
    'div.tooltip__inner > div.sx-select__search > input')
ActionChains(driver).move_to_element(elem).send_keys(countries_var).perform()
time.sleep(2)

# searched country click
elem = driver.find_element_by_css_selector(
    'div.tooltip__inner > div.sx-select__list.ps')
ActionChains(driver).click(elem).perform()

# number of port set
elem = driver.find_element_by_css_selector(
    'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.lbl-param-list > div > div > input')
elem.clear()
ActionChains(driver).send_keys_to_element(elem, port_var).perform()

# save button click
elem = driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.flex.flex--justify.flex--wrap.content-mwrap > button.button.button--04.package__form-btn.margin--t.add-filter-save')
ActionChains(driver).click(elem).perform()
time.sleep(2)

# scraping country, port list
soup = BeautifulSoup(driver.page_source, "lxml")

country_port_list = []
rows = soup.find_all("div", {"class": "sx-form__item ip-port"})

for row in rows:

    country = row.find("div", {"class": "ip-port__country"}).get_text().strip()

    port = row.find("div", {"class": "ip-port__info"}).get_text().strip()

    if (countries_var == country):

        country_port_list.append(country)

        country_port_list.append(port.replace(" ", "").replace("-", ""))

# make minimum port, maximum port and country_port_list append
minimum_port = country_port_list[1][:5]
maximum_port = country_port_list[1][5:]
