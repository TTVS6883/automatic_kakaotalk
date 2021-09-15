# LIBRARY OR MODULE
# emulator
from time import time
import pyautogui
import keyboard
import time
import pyperclip

# selenium
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

# gui
from tkinter import *
import tkinter.ttk as ttk

# VALUES
# emlator

# selenium
global country_var, device_var
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

# gui
global country_list
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
device_var_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# METHOD
# emulator


def interval_short():

    time.sleep(0.5)


def interval_middle():

    time.sleep(3)


def interval_long():

    time.sleep(6)


def launch_exit_kakao():

    # launch kakaotalk
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # exit kakaotalk
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def del_kakao():

    # launch kakaotalk setting
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.dragRel(3, 0, 0.5, button='left')
    interval_short()

    # click stop
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_exit.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click ok
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()
    interval_short()

    # click repository
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_repository.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click delete
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_delete.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click ok
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_ok2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # exit kakaotalk setting
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def del_proxy():

    # launch proxy setting
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.dragRel(0, 3, 0.5, button='left')
    interval_short()

    # click repository
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_repository.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click delete
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_delete.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click ok
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # exit proxy setting
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def launch_proxy():

    # launch proxy
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_long()

    # scrolldown
    pyautogui.press('down', 7)
    interval_short()

    # click host
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_host.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # insert host value
    pyautogui.typewrite('proxy.soax.com')
    interval_short()

    # click ok
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # scrolldown
    pyautogui.press('down', 5)
    interval_short()

    # click port
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click input
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_input.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # delete default value
    pyautogui.press('backspace', 10)

    # deactivate multicommand
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short
    pyautogui.hotkey('ctrl', '9')
    interval_short

    # insert port value
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/proxy_port2.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.typewrite('56789')

    interval_short()

    # active multicommand
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short
    pyautogui.hotkey('ctrl', '9')
    interval_short

    # click ok
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # scrollup
    pyautogui.press('up', 7)

    # active proxy
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_active.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # exit proxy
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def launch_sim():

    # launch sim operator
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # active IMEI
    pyautogui.press('down', 3)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_active.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click random/refresh
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_random.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click mobile_no edit
    pyautogui.press('down', 20)
    pyautogui.press('left', 1)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_edit1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click input
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_input.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # delete default value
    pyautogui.press('backspace', 25)
    interval_short()

    # deactive multicommand
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_mobile.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short
    pyautogui.hotkey('ctrl', '9')
    interval_short

    # insert mobile_no value
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/sim_mobile.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.typewrite('1234567891')

    interval_short()

    # active multicommand
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_mobile.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short
    pyautogui.hotkey('ctrl', '9')
    interval_short

    # click save
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_save.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click sim operator edit
    pyautogui.press('down', 30)
    pyautogui.press('up', 2)
    pyautogui.press('left', 1)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_edit2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # click country
    pyautogui.press('down', 2)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_country.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

# selenium


def run_chrome():
    # run chrome(selenium) by cmd
    os.chdir('C:\Program Files\Google\Chrome\Application')
    os.system(
        'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')


def run_selenium():
    pass


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

    global driver, country_var, device_var

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
    ActionChains(driver).send_keys_to_element(elem, device_var).perform()

    # save button click
    elem = driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.flex.flex--justify.flex--wrap.content-mwrap > button.button.button--04.package__form-btn.margin--t.add-filter-save')
    ActionChains(driver).click(elem).perform()

# gui


def set_country_list():

    country_list = []

    if main_country_value.get() == 1:

        country_list = europe_list

    elif main_country_value.get() == 2:

        country_list = asia_list

    elif main_country_value.get() == 3:

        country_list = africa_list

    elif main_country_value.get() == 4:

        country_list = north_america_list

    elif main_country_value.get() == 5:

        country_list = south_america_list

    country_list_combobox['values'] = country_list


# MAIN
# run selenium
global driver
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "macro_kakaotalk/date_version/chromedriver.exe"
driver = webdriver.Chrome(
    executable_path=chrome_driver, options=chrome_options)
driver.implicitly_wait(10)

# main gui
window = Tk()
window.title("카카오톡 계정생성기")

# frame_main
frame_main = Frame(window)
frame_main.pack()

# frame_top / setting
frame_top = LabelFrame(frame_main, text="설정")
frame_top.pack(fill="x", padx=5, pady=5)

# frame_top1 / main_country
frame_top1 = LabelFrame(frame_top, text="대륙")
frame_top1.pack(fill="x", padx=5, pady=5)

main_country_value = IntVar()
main_country_list_radiobtn1 = Radiobutton(
    frame_top1, text="Europe", value=1, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn2 = Radiobutton(
    frame_top1, text="Asia", value=2, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn3 = Radiobutton(
    frame_top1, text="Africa", value=3, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn4 = Radiobutton(
    frame_top1, text="North America", value=4, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn5 = Radiobutton(
    frame_top1, text="South America", value=5, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn1.pack(side="left")
main_country_list_radiobtn2.pack(side="left")
main_country_list_radiobtn3.pack(side="left")
main_country_list_radiobtn4.pack(side="left")
main_country_list_radiobtn5.pack(side="left")

# frame_top2 / country
frame_top2 = LabelFrame(frame_top, text="국가")
frame_top2.pack(fill="x", padx=5, pady=5)

country_list_combobox = ttk.Combobox(frame_top2, height=20, state="readonly")
country_list_combobox.pack(fill="x", padx=5, pady=5)
country_var = country_list_combobox.get()

# frame_top3 / device_var
frame_top3 = LabelFrame(frame_top, text="생성수")
frame_top3.pack(fill="x", padx=5, pady=5)

device_var_combobox = ttk.Combobox(
    frame_top3, height=20, state="readonly", values=device_var_list)
device_var_combobox.pack(fill="x", padx=5, pady=5)
device_var = device_var_combobox.get()

# frame_bottom / button
frame_bottom = LabelFrame(frame_main, text="실행")
frame_bottom.pack(fill="x", padx=5, pady=5)

btn1 = Button(frame_bottom, text="번호/포트 생성")
btn1.pack(side="left", padx=5, pady=5)

btn2 = Button(frame_bottom, text="LD실행 1단계")
btn2.pack(side="left", padx=5, pady=5)

btn3 = Button(frame_bottom, text="LD실행 2단계")
btn3.pack(side="left", padx=5, pady=5)

# launch gui
window.resizable(False, False)
window.mainloop()
