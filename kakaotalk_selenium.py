import time
import os
from math import pi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

# cmd cd C:\Program Files\Google\Chrome\Application
# cmd chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"

global country_var, device_var, port_var
country_var = "Angola"
device_var = 5
port_var = 5
main_country_list = ['Europe', 'Asia',
                     'Africa', 'North America', 'South America']
europe_list = ['Russia', 'Ukraine', 'Poland', 'England', 'Ireland', 'Serbia', 'Romania', 'Estonia', 'Germany', 'Lithuania', 'Croatia', 'Sweden', 'Netherlands', 'Latvia', 'Austria', 'Belarus', 'Spain', 'Slovenia', 'Czech', 'Cyprus', 'France',
               'Belgium', 'Bulgaria', 'Hungary', 'Moldova', 'Italy', 'Bosnia', 'Portugal', 'Georgia', 'Greece', 'Iceland', 'Slovakia', 'Monaco', 'Albania', 'Finland', 'Luxembourg', 'Montenegro', 'Denmark', 'Switzerland', 'Norway', 'Northmacedonia']
asia_list = ['Kazakhstan', 'China', 'Philippines', 'Myanmar', 'Indonesia', 'Malaysia', 'Vietnam', 'Kyrgyzstan', 'Israel', 'HongKong', 'Macao', 'India', 'Cambodia', 'Laos',
             'Yemen', 'Uzbekistan', 'Iraq', 'Thailand', 'Saudiarabia', 'Taiwan', 'Bangladesh', 'Turkey', 'Srilanka', 'Pakistan', 'Newzealand', 'Mongolia', 'Afghanistan', 'Papua', 'Nepal', 'Timorleste', 'Uae', 'Kuwait', 'Oman', 'Qatar', 'Jordan', 'Brunei', 'Tajikistan', 'Bahrain', 'Armenia', 'Lebanon', 'Bhutan', 'Maldives', 'Turkmenistan', 'Japan', 'Southkorea']
africa_list = ['Kenya', 'Tanzania', 'DCongo', 'Nigeria', 'Egypt', 'Ivory', 'Gambia', 'Southafrica', 'Morocco', 'Ghana', 'Cameroon', 'Chad', 'Algeria', 'Senegal', 'Guinea', 'Mali', 'Ethiopia', 'Uganda', 'Angola', 'Mozambique', 'Tunisia', 'Zimbabwe', 'Togo', 'Libyan', 'Swaziland', 'Mauritania', 'Sierraleone',
               'Burundi', 'Benin', 'Botswana', 'Caf', 'Guineabissau', 'Comoros', 'Liberia', 'Lesotho', 'Malawi', 'Namibia', 'Niger', 'Rwanda', 'Reunion', 'Zambia', 'Somalia', 'Congo', 'Furkinafaso', 'Gabon', 'Mauritius', 'Equatorialguinea', 'Djibouti', 'Eritrea', 'Southsudan', 'Saotomeandprincipe', 'Seychelles', 'Capeverde']
north_america_list = ['USA (virtual)', 'Canada', 'Mexico', 'Honduras', 'Nicaragua', 'Costarica', 'Guatemala', 'Puertorico', 'Salvador', 'Jamaica', 'Panama', 'Barbados',
                      'Bahamas', 'Belize', 'Dominica', 'Grenada', 'Saintkitts', 'Guadeloupe', 'Saintlucia', 'Antiguabarbuda', 'Caymanislands', 'Aruba', 'Montserrat', 'Anguilla', 'USA']
south_america_list = ['Haiti', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Brazil', 'Paraguay', 'Bolivia', 'Trinidad', 'Ecuador', 'Dominican', 'Guyana', 'Suriname', 'Chile', 'Uruguay', 'Frenchguiana',
                      'Saintvincentgrenadines']


def run_chrome():
    # run chrome(selenium) by cmd
    os.chdir('C:\Program Files\Google\Chrome\Application')
    os.system(
        'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')


def run_selenium():

    global driver

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(
        executable_path=chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)


def switch_tab(page_alias):

    global driver

    if page_alias == "sms":

        driver.get("https://sms-activate.ru/en/getNumber")

    elif page_alias == "proxy":

        driver.get("https://dashboard.soax.com/proxy")


def scrap_html():

    global soup

    soup = BeautifulSoup(driver.page_source, "lxml")


def scrap_target(target):

    global driver, soup, phone_list, sms_list, port_list, country_var, minimum_port, maximum_port

    # scraping and phone_list append
    if target == "number":

        scrap_html()

        phone_list = []
        rows = soup.find("table", {"id": "getNumberTable"}).find_all(
            "input", {"class": "form-control"})

        for row in rows:

            phone_list.append(row["value"])

    # scraping and sms_list append
    elif target == "sms":

        scrap_html()

        sms_list = []
        rows = soup.find("table", {"id": "getNumberTable"}).find_all("strong")

        for row in rows:

            sms_list.append(row.get_text())

    # scraping and port_list append
    elif target == "port":

        scrap_html()

        soup = BeautifulSoup(driver.page_source, "lxml")

        port_list = []
        rows = soup.find_all("div", {"class": "sx-form__item ip-port"})

        for row in rows:

            country = row.find(
                "div", {"class": "ip-port__country"}).get_text().strip()

            port = row.find(
                "div", {"class": "ip-port__info"}).get_text().strip()

            if (country_var == country):

                port_list.append(country)

                port_list.append(port.replace(" ", "").replace("-", ""))

                # make minimum port, maximum port by port_list
                minimum_port = port_list[1][:5]
                maximum_port = port_list[1][5:]


def add_phone():

    global driver, country_var, device_var

    # countries dropdown click
    elem = driver.find_element_by_css_selector(
        '.statusBtn.btn.dropdown-toggle.btn-primary')
    ActionChains(driver).click(elem).perform()

    # countries search click and sendkeys
    elem = driver.find_element_by_css_selector('.form-control.countriesSearch')
    elem.clear()
    ActionChains(driver).click(elem).send_keys(country_var).perform()
    time.sleep(2)

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


def add_port():

    global driver, country_var, port_var

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
    ActionChains(driver).move_to_element(elem).send_keys(country_var).perform()
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


# 기본 테스트셋
run_selenium()
add_phone()
switch_tab("proxy")
add_port()
time.sleep(3)
scrap_target("port")
switch_tab("sms")
time.sleep(20)
scrap_target("number")
scrap_target("sms")

# print("번호 리스트")
# print(phone_list)
# print("sms 리스트")
# print(sms_list)
# print("port 리스트")
# print(port_list)
# print("최소")
# print(minimum_port)
# print("최대")
# print(maximum_port)
