# from ctypes import sizeof
from tkinter import *
import tkinter.ttk as ttk
import time
import os
from math import pi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from time import time
from datetime import datetime
from datetime import timedelta
import pyautogui
import time
import tkinter.messagebox as msgbox


# cmd cd C:\Program Files\Google\Chrome\Application
# cmd chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"

# 변수 선언
global country_list, country, device, delay_page_var, delay_sms_var, delay_openchat_var
main_country_list = ['Africa', 'Asia',
                     'Europe', 'North America', 'South America']
# ['Europe', 'Asia', 'Africa', 'North America', 'South America']
europe_list = ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
               'Latvia', 'Lithuania', 'Luxembourg', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Northmacedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine']
# ['Russia', 'Ukraine', 'Poland', 'England', 'Ireland', 'Serbia', 'Romania', 'Estonia', 'Germany', 'Lithuania', 'Croatia', 'Sweden', 'Netherlands', 'Latvia', 'Austria', 'Belarus', 'Spain', 'Slovenia', 'Czech', 'Cyprus', 'France', 'Belgium', 'Bulgaria', 'Hungary', 'Moldova', 'Italy', 'Bosnia', 'Portugal', 'Georgia', 'Greece', 'Iceland', 'Slovakia', 'Monaco', 'Albania', 'Finland', 'Luxembourg', 'Montenegro', 'Denmark', 'Switzerland', 'Norway', 'Northmacedonia']
asia_list = ['Afghanistan', 'Armenia', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'HongKong', 'India', 'Indonesia', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macao', 'Malaysia', 'Maldives',
             'Mongolia', 'Myanmar', 'Nepal', 'Newzealand', 'Oman', 'Pakistan', 'Papua', 'Philippines', 'Qatar', 'Saudiarabia', 'Southkorea', 'Srilanka', 'Taiwan', 'Tajikistan', 'Thailand', 'Timorleste', 'Turkey', 'Turkmenistan', 'Uae', 'Uzbekistan', 'Vietnam', 'Yemen']
# ['Kazakhstan', 'China', 'Philippines', 'Myanmar', 'Indonesia', 'Malaysia', 'Vietnam', 'Kyrgyzstan', 'Israel', 'HongKong', 'Macao', 'India', 'Cambodia', 'Laos', 'Yemen', 'Uzbekistan', 'Iraq', 'Thailand', 'Saudiarabia', 'Taiwan', 'Bangladesh', 'Turkey', 'Srilanka', 'Pakistan', 'Newzealand', 'Mongolia', 'Afghanistan', 'Papua', 'Nepal', 'Timorleste', 'Uae', 'Kuwait', 'Oman', 'Qatar', 'Jordan', 'Brunei', 'Tajikistan', 'Bahrain', 'Armenia', 'Lebanon', 'Bhutan', 'Maldives', 'Turkmenistan', 'Japan', 'Southkorea']
africa_list = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burundi', 'Caf', 'Cameroon', 'Capeverde', 'Chad', 'Comoros', 'Congo', 'DCongo', 'Djibouti', 'Egypt', 'Equatorialguinea', 'Eritrea', 'Ethiopia', 'Furkinafaso', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guineabissau', 'Ivory', 'Kenya', 'Lesotho', 'Liberia',
               'Libyan', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Reunion', 'Rwanda', 'Saotomeandprincipe', 'Senegal', 'Seychelles', 'Sierraleone', 'Somalia', 'Southafrica', 'Southsudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
# ['Kenya', 'Tanzania', 'DCongo', 'Nigeria', 'Egypt', 'Ivory', 'Gambia', 'Southafrica', 'Morocco', 'Ghana', 'Cameroon', 'Chad', 'Algeria', 'Senegal', 'Guinea', 'Mali', 'Ethiopia', 'Uganda', 'Angola', 'Mozambique', 'Tunisia', 'Zimbabwe', 'Togo', 'Libyan', 'Swaziland', 'Mauritania', 'Sierraleone', 'Burundi', 'Benin', 'Botswana', 'Caf', 'Guineabissau', 'Comoros', 'Liberia', 'Lesotho', 'Malawi', 'Namibia', 'Niger', 'Rwanda', 'Reunion', 'Zambia', 'Somalia', 'Congo', 'Furkinafaso', 'Gabon', 'Mauritius', 'Equatorialguinea', 'Djibouti', 'Eritrea', 'Southsudan', 'Saotomeandprincipe', 'Seychelles', 'Capeverde']
north_america_list = ['Anguilla', 'Antiguabarbuda', 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Caymanislands', 'Costarica', 'Dominica', 'Grenada', 'Guadeloupe',
                      'Guatemala', 'Honduras', 'Jamaica', 'Mexico', 'Montserrat', 'Nicaragua', 'Panama', 'Puertorico', 'Saintkitts', 'Saintlucia', 'Salvador', 'USA', 'USA (virtual)']
# ['USA (virtual)', 'Canada', 'Mexico', 'Honduras', 'Nicaragua', 'Costarica', 'Guatemala', 'Puertorico', 'Salvador', 'Jamaica', 'Panama', 'Barbados', 'Bahamas', 'Belize', 'Dominica', 'Grenada', 'Saintkitts', 'Guadeloupe', 'Saintlucia', 'Antiguabarbuda', 'Caymanislands', 'Aruba', 'Montserrat', 'Anguilla', 'USA']
south_america_list = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Dominican', 'Ecuador', 'Frenchguiana',
                      'Guyana', 'Haiti', 'Paraguay', 'Peru', 'Saintvincentgrenadines', 'Suriname', 'Trinidad', 'Uruguay', 'Venezuela']
# ['Haiti', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Brazil', 'Paraguay', 'Bolivia', 'Trinidad', 'Ecuador', 'Dominican', 'Guyana', 'Suriname', 'Chile', 'Uruguay', 'Frenchguiana', 'Saintvincentgrenadines']
device_var_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# 함수 선언 (에뮬레이터)
def interval_short():  # 대기시간 0.5초

    time.sleep(0.5)


def interval_middle():  # 대기시간 3초

    time.sleep(3)


def interval_long():  # 대기시간 6초

    time.sleep(6)


def launch_kakao():  # 카카오톡 실행 및 종료

    global delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    # 카카오톡 실행
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # 카카오톡 종료
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/home_icon.png', confidence=0.87, region=(0,0,240,338)))
        
        except TypeError:

            pass
        
        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 카카오톡 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_middle()

    # # 카카오톡 종료
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/home_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def del_kakao():  # 카카오톡 강제종료 및 데이터 삭제

    global delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    # 카카오톡 앱 정보 실행
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.dragRel(3, 0, 0.5, button='left')
    interval_short()
    interval_short()

    # # 카카오톡 앱 정보 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.dragRel(3, 0, 0.5, button='left')
    # interval_short()
    # interval_short()

    # 강제종료 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_exit.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 강제종료 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_exit.png', confidence=0.86))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 확인 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_ok1.png', confidence=0.87, region=(0,0,240,338)))
        
        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()
    interval_short()

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_ok1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()
    # interval_short()

    # 저장소 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_repository.png', confidence=0.87, region=(0,0,240,338)))
        
        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 저장소 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_repository.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 데이터 지우기 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_delete.png', confidence=0.87, region=(0,0,240,338)))


        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 데이터 지우기 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_delete.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 확인 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_ok2.png', confidence=0.87, region=(0,0,240,338)))
        
        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_ok2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 홈 화면 복귀
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/home_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 홈 화면 복귀
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/home_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def del_proxy():  # 프록시 데이터 삭제

    global delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    # 프록시 앱 정보 실행
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.dragRel(0, 3, 0.5, button='left')
    interval_short()

    # # 프록시 앱 정보 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.dragRel(0, 3, 0.5, button='left')
    # interval_short()

    # 저장소 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_repository.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 저장소 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_repository.png', confidence=0.86))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 데이터 지우기 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_delete.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 데이터 지우기 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_delete.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 확인 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_ok1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_ok1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 홈 화면 복귀
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/home_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 홈 화면 복귀
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/home_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def launch_proxy():  # 프록시 실행 및 설정

    global minimum_port, delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    # 프록시 실행
    start_time = datetime.now()
    pos = None

    while pos is None:
        
        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_long()

    # # 프록시 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_middle()

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_label.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 각 에뮬레이터마다 하단 스크롤
    pos_list = pyautogui.locateAllOnScreen(
        "images/proxy_label.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.press('down', 7)
        interval_short()

    interval_middle()

    # 호스트 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/proxy_host.png", confidence=0.90)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # # 1번 에뮬레이터 클릭
    # start_time = datetime.now()
    # pos = None

    # while pos is None:

    #     try:

    #         pos = pyautogui.center(pyautogui.locateOnScreen(
    #         'images/proxy_label.png', confidence=0.87, region=(0,0,240,338)))

    #     except TypeError:

    #         pass

    #     if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
    #         break

    # pyautogui.moveTo(pos)
    # pyautogui.click()

    # # 1번 에뮬레이터 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_label.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # # 하단 스크롤
    # pyautogui.press('down', 7, 0.1)
    # interval_middle()

    # # 호스트 클릭
    # start_time = datetime.now()
    # pos = None

    # while pos is None:

    #     try:

    #         pos = pyautogui.center(pyautogui.locateOnScreen(
    #         'images/proxy_host.png', confidence=0.87, region=(0,0,240,338)))

    #     except TypeError:

    #         pass

    #     if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
    #         break

    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # # 호스트 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_host.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_host1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 호스트 입력
    pyautogui.typewrite('proxy.soax.com')
    interval_short()

    # 확인 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_ok1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_ok1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 하단 스크롤
    pyautogui.press('down', 2)
    interval_short()

    # 포트 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_port1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 포트 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_port1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 포트 입력 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_input.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 포트 입력 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_input.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 기본값(3128) 제거
    pyautogui.press('backspace', 10)

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_port2.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 비활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_port2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 포트 입력
    pos_list = pyautogui.locateAllOnScreen(
        "images/proxy_port2.png", confidence=0.87)
    pos_list = list(pos_list)
    port_value = minimum_port

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.typewrite(port_value)
        port_value = str(int(port_value)+1)

    interval_short()

    # 멀티커맨드 활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_port2.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_port2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 확인 클릭
    start_time = datetime.now()
    pos = None

    pyautogui.press('down')
    pyautogui.press('right')

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_ok1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 확인 클릭
    # pyautogui.press('down')
    # pyautogui.press('right')
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_ok1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 상단 스크롤
    pyautogui.press('up', 7)

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_label.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 비활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_label.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 프록시 Enable / 광고 나오는 경우 때문에 locateAllOnScreen으로 처리
    pos_list = pyautogui.locateAllOnScreen(
        "images/proxy_active.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_middle()

    # 멀티커맨드 활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/proxy_label.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/proxy_label.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 홈 화면 복귀
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/home_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 홈 화면 복귀
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/home_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def launch_sim():  # 디바이스 에뮬레이터 실행 및 설정

    global phone_list, delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    # 디바이스 에뮬레이터 실행
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()
    pyautogui.press('up', 30)

    # # 디바이스 에뮬레이터 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_middle()
    # pyautogui.press('up', 30)

    # IMEI 활성화 / 예외처리
    start_time = datetime.now()
    pos = None
    
    pyautogui.press('down', 2)

    while pos is None:

        try:  # IMEI 비활성화 상태인 경우

                #IMEI 활성화
                pos = pyautogui.center(pyautogui.locateOnScreen(
                'images/sim_active.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:  # IMEI 활성화 상태인 경우

            break

        # if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
        #     break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # IMEI 활성화 / 예외처리
    # try:  # IMEI 비활성화 상태인 경우

    #     # IMEI 활성화
    #     pyautogui.press('down', 2)
    #     pos = pyautogui.center(pyautogui.locateOnScreen(
    #         'images/sim_active.png', confidence=0.87))
    #     pyautogui.moveTo(pos)
    #     pyautogui.click()
    #     interval_short()

    # except TypeError:  # IMEI 활성화 상태인 경우

    #     pass

    # 랜덤 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_random.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 랜덤 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_random.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 핸드폰 번호 클릭
    start_time = datetime.now()
    pos = None

    pyautogui.press('down', 24)
    pyautogui.press('up', 4)
    pyautogui.press('left', 1)

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_edit2.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 핸드폰 번호 클릭
    # pyautogui.press('down', 24)
    # pyautogui.press('up', 4)
    # pyautogui.press('left', 1)
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_edit2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 입력창 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_input.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 입력창 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_input.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 기본값 제거
    pyautogui.press('backspace', 25)
    interval_short()

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_mobile.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 비활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_mobile.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 핸드폰 번호 입력
    pos_list = pyautogui.locateAllOnScreen(
        "images/sim_mobile.png", confidence=0.87)
    pos_list = list(pos_list)
    phone_list_index = 0

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.typewrite(phone_list[phone_list_index])
        phone_list_index += 1

    interval_short()

    # 멀티커맨드 활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_mobile.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_mobile.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 저장 클릭
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_save1.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 저장 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_save1.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 국가 설정 진입
    start_time = datetime.now()
    pos = None

    pyautogui.press('down', 30)
    pyautogui.press('up', 2)
    pyautogui.press('left', 1)

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_edit2.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 국가 설정 진입
    # pyautogui.press('down', 30)
    # pyautogui.press('up', 2)
    # pyautogui.press('left', 1)
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_edit2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 국가 클릭
    start_time = datetime.now()
    pos = None

    pyautogui.press('down', 2)

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_country.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 국가 클릭
    # pyautogui.press('down', 2)
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_country.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def exit_sim():  # 디바이스 에뮬레이터 국가 설정 저장

    global delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    run_selenium()

    # 저장 클릭
    start_time = datetime.now()
    pos = None

    pyautogui.press('tab', 3)

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/sim_save2.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 저장 클릭
    # pyautogui.press('tab', 3)
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/sim_save2.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 홈 화면 복귀
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/home_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # # 홈 화면 복귀
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/home_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()


def register_kakao_1():  # 디바이스 에뮬레이터 국가 설정 저장, 카카오톡 실행, 권한허용, 회원가입 진입

    global delay_page_var

    delay_page_var = int(delay_page_var_combobox.get())

    state_update("카카오톡 가입을 시작합니다.")

    # launch_sim() 종료 후 exit_sim()으로 설정 저장 및 홈 화면 복귀
    exit_sim()

    # 카카오톡 실행
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_icon.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # # 카카오톡 실행
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_icon.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_middle()

    # 이용안내 페이지 넘어갔는지 확인
    state_update("권한허용을 진행합니다.")

    global device, delay_sms_var, delay_openchat_var

    delay_page_var = int(delay_page_var_combobox.get())
    delay_sms_var = int(delay_sms_var_combobox.get())

    start_time = datetime.now()
    allow_bool = True

    device = device_var_combobox.get()
    device_count = int(device)

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_1.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == device_count:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False


    # 하단 스크롤
    pyautogui.press('down', 5)

    # 멀티커맨드 비활성화
    start_time = datetime.now()
    pos = None

    while pos is None:

        try:

            pos = pyautogui.center(pyautogui.locateOnScreen(
            'images/kakao_label2_7.png', confidence=0.87, region=(0,0,240,338)))

        except TypeError:

            pass

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
           
            break

    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # # 멀티커맨드 비활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'images/kakao_label2_7.png', confidence=0.87))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 허용하기 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow1.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 전화 걸기 및 관리 허용 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow2_2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 기기 사진, 미디어, 파일 액세스 허용 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow2_2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 주소록 액세스 허용 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow2_2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 가입화면 넘어갔는지 확인\
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_2.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == device_count:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 새로운 카카오계정 만들기 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_register.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 이용약관 페이지 넘어갔는지 확인
    state_update("이용약관동의를 진행합니다.")

    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_allow_main.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == device_count:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 모두 동의합니다 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow3.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 멀티커맨드 활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'images/kakao_allow_main.png', confidence=0.87))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 하단 스크롤
    pyautogui.press('down', 10)

    # 멀티커맨드 비활성화
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 선택항목 해제1
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow3_5.png", confidence=0.89)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 선택항목 해제2
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow3_6.png", confidence=0.89)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 선택항목 해제3
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow3_7.png", confidence=0.89)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 동의하고 계속 진행합니다 클릭
    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow7.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 전화번호 입력 페이지 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_3.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # # [필수]16세 이상 이용자입니다 클릭
    # try:

    #     # [필수]16세 이상 이용자입니다 클릭
    #     pos_list = pyautogui.locateAllOnScreen(
    #         "images/kakao_allow8.png", confidence=0.87)
    #     pos_list = list(pos_list)

    #     for i in pos_list:

    #         pos = pyautogui.center(i)
    #         pyautogui.moveTo(pos)
    #         pyautogui.click()

    #     interval_short()

    # except TypeError:

    #     pass

    # # 확인 클릭
    # pos_list = pyautogui.locateAllOnScreen(
    #     "images/kakao_ok3.png", confidence=0.87)
    # pos_list = list(pos_list)

    # for i in pos_list:

    #     pos = pyautogui.center(i)
    #     pyautogui.moveTo(pos)
    #     pyautogui.click()

    # interval_short()

     # 전화번호 확인 클릭
    try:  # 확인 버튼 나오는 경우

        # 확인 클릭
        pos_list = pyautogui.locateAllOnScreen(
            "images/kakao_ok3.png", confidence=0.87)
        pos_list = list(pos_list)

        for i in pos_list:

            pos = pyautogui.center(i)
            pyautogui.moveTo(pos)
            pyautogui.click()

        interval_short()

    except TypeError:  # [필수]16세 이상 이용자입니다 나오는 경우

        # [필수]16세 이상 이용자입니다 클릭
        pos_list = pyautogui.locateAllOnScreen(
            "images/kakao_allow8.png", confidence=0.87)
        pos_list = list(pos_list)

        for i in pos_list:

            pos = pyautogui.center(i)
            pyautogui.moveTo(pos)
            pyautogui.click()

        interval_short()

        # 확인 클릭
        pos_list = pyautogui.locateAllOnScreen(
            "images/kakao_ok3.png", confidence=0.87)
        pos_list = list(pos_list)

        for i in pos_list:

            pos = pyautogui.center(i)
            pyautogui.moveTo(pos)
            pyautogui.click()

        interval_short()

    # 확인 클릭
    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_ok4.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # # 확인 클릭
    # page_var = 0
    # pos_list = pyautogui.locateAllOnScreen(
    #     "images/kakao_ok4.png", confidence=0.87)
    # pos_list = list(pos_list)

    # for i in pos_list:

    #     pos = pyautogui.center(i)
    #     pyautogui.moveTo(pos)
    #     pyautogui.click()

    #     page_var += 1

    # interval_short()

    # # 인증번호 에러 뜨는 에뮬레이터 종료 / + 셀레니움에서 해당 sms 번호 어떻게 지울건지?
    # try: # 인증요청 제한횟수 나오는 경우

    #     # 확인 클릭
    #     pos_list = pyautogui.locateAllOnScreen(
    #         "images/kakao_ok4.png", confidence=0.87)
    #     pos_list = list(pos_list)

    #     for i in pos_list:

    #         pos = pyautogui.center(i)
    #         pyautogui.moveTo(pos)
    #         pyautogui.click()
    #         interval_short()

    #         # 에뮬레이터 종료
    #         pyautogui.hotkey("alt", "f4")
    #         interval_short()
    #         pos = pyautogui.center(pyautogui.locateOnScreen(
    #                 'images/exit.png', confidence=0.87))
    #         pyautogui.moveTo(pos)
    #         pyautogui.click()
    #         interval_short()

    # except TypeError: # 인증요청 제한횟수 없는 경우

    #     pass

    # 인증번호 입력 페이지 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_4.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # sms 전송 대기시간
    state_update(str(delay_sms_var) + "초동안 대기합니다.")

    time.sleep(delay_sms_var)

    global sms_list

    # 인증번호 가져오기
    state_update("인증번호 리스트를 가져옵니다.")

    get_sms()

    state_update("인증번호를 입력합니다.")

    # 인증번호 입력 (절대값 버전)
    sms_list_index = 0

    pyautogui.moveTo(90, 132)
    pyautogui.click()
    pyautogui.typewrite(sms_list[sms_list_index])
    time.sleep(0.1)

    sms_list_index += 1

    for_var = device_count - 1

    if for_var > 7:

        for i in range(7):

            pyautogui.dragRel(240)
            pyautogui.click()
            pyautogui.typewrite(sms_list[sms_list_index])
            time.sleep(0.1)

            sms_list_index += 1

        pyautogui.moveTo(90, 470)
        pyautogui.click()
        pyautogui.typewrite(sms_list[sms_list_index])
        time.sleep(0.1)

        sms_list_index += 1

        for i in range(for_var - 8):

            pyautogui.dragRel(240)
            pyautogui.click()
            pyautogui.typewrite(sms_list[sms_list_index])
            time.sleep(0.1)

            sms_list_index += 1

    elif for_var <= 7:

        for i in range(for_var):

            pyautogui.dragRel(240)
            pyautogui.click()
            pyautogui.typewrite(sms_list[sms_list_index])
            time.sleep(0.1)

            sms_list_index += 1

    interval_short()

    # # 인증번호 입력
    # pos_list = pyautogui.locateAllOnScreen(
    #     "images/kakao_input2.png", confidence=0.87)
    # pos_list = list(pos_list)
    # sms_list_index = 0

    # for i in pos_list:

    #     pos = pyautogui.center(i)
    #     pyautogui.moveTo(pos)
    #     pyautogui.click()
    #     # pyautogui.typewrite(sms_list[sms_list_index])
    #     pyautogui.typewrite("1123")
    #     sms_list_index += 1

    # interval_short()

    # 확인 클릭
    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_ok5.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 비밀번호 입력 페이지 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_9.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 비밀번호 클릭 및 입력
    state_update("비밀번호를 입력합니다.")

    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_pw1.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite("abcabc12!")
        time.sleep(0.1)

    interval_short()

    # 비밀번호 확인 클릭 및 입력
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_pw2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite("abcabc12!")
        time.sleep(0.1)

    interval_short()

    # 확인 클릭
    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_ok5.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 프로필 화면 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_5.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 이름 클릭 및 입력
    state_update("이름을 입력합니다.")

    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_name.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite("abcabc12!")
        time.sleep(0.1)

    interval_short()

    # 주소록 친구 자동 추가 해제 클릭
    state_update("주소록 친구 자동 추가를 해제합니다.")

    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_allow9.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 확인 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_ok5.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 기본 이미지로 설정 클릭
    state_update("기본 이미지로 설정합니다.")

    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_image.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 이메일 등록 화면 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label2_6.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 이메일 등록 나중에 하기 클릭
    state_update("이메일 등록을 진행합니다.")

    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_later.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 카톡 홈 화면 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_chat1.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_page_var):
            allow_bool = False

    # 채팅 클릭1
    state_update("오픈채팅방에 진입합니다.")

    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_chat1.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 채팅 클릭2
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_chat2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 새로운 채팅 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_search1.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_short()

    # 오픈채팅 클릭
    page_var = 0
    pos_list = pyautogui.locateAllOnScreen(
        "images/kakao_search2.png", confidence=0.87)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

        page_var += 1

    interval_short()

    # 오픈채팅 리스트 페이지 넘어갔는지 확인
    start_time = datetime.now()
    allow_bool = True

    while allow_bool:

        try:

            pos_list = pyautogui.locateAllOnScreen(
                "images/kakao_label3.png", confidence=0.87)
            pos_list = list(pos_list)

        except TypeError:

            pass

        if len(pos_list) == page_var:
            allow_bool = False

        if datetime.now() - start_time > timedelta(seconds=delay_openchat_var):
            allow_bool = False

    # 오픈채팅 입장
    device = device_var_combobox.get()
    device_count = int(device)

    pyautogui.moveTo(90, 320)
    pyautogui.scroll(-270)
    interval_short()
    pyautogui.click()

    for_var = device_count - 1

    if for_var > 7:

        for i in range(7):

            pyautogui.dragRel(240)
            pyautogui.scroll(-270)
            interval_short()
            pyautogui.click()

        pyautogui.moveTo(90, 660)
        pyautogui.scroll(-270)
        interval_short()
        pyautogui.click()

        for i in range(for_var - 8):

            pyautogui.dragRel(240)
            pyautogui.scroll(-270)
            interval_short()
            pyautogui.click()

    elif for_var <= 7:

        for i in range(for_var):

            pyautogui.dragRel(240)
            pyautogui.scroll(-270)
            interval_short()
            pyautogui.click()

    interval_short()

    state_update("카카오톡 가입이 완료되었습니다.")

# 함수 선언 (셀레니움)
def run_chrome():  # 크롬 실행

    os.chdir('C:\Program Files\Google\Chrome\Application')
    os.system(
        'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')
    return 0


def run_selenium():  # 셀레니움 실행

    global driver

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"

    driver = webdriver.Chrome(
        executable_path=chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)


def check_port():  # 포트 존재여부 확인

    global driver, soup, port_list, country, bool_port

    country = country_list_combobox.get()

    # ip address click
    elem = driver.find_element_by_css_selector(
        'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
    ActionChains(driver).click(elem).perform()
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, "lxml")

    bool_port = False  # 포트 미존재
    rows = soup.find_all("div", {"class": "sx-form__item ip-port"})
    country_lower = country.lower()

    for row in rows:

        row_country = row.find(
            "div", {"class": "ip-port__country"}).get_text().strip().replace(" ", "")

        row_country = row_country.lower()

        if (country_lower == row_country):

            bool_port = True  # 포트 존재

    return bool_port


def get_number():  # 전화번호 가져오기

    global driver, soup, phone_list

    soup = BeautifulSoup(driver.page_source, "lxml")

    phone_list = []
    rows = soup.find("table", {"id": "getNumberTable"}).find_all(
        "input", {"class": "form-control"})

    for row in rows:

        phone_list.append(row["value"])


def get_sms():  # 인증번호 가져오기

    global driver, soup, sms_list

    soup = BeautifulSoup(driver.page_source, "lxml")

    sms_list = []
    rows = soup.find("table", {"id": "getNumberTable"}).find_all("strong")

    for row in rows:

        sms_list.append(row.get_text())


def get_port():  # 포트 가져오기

    global driver, soup, port_list, country, minimum_port

    country = country_list_combobox.get()

    soup = BeautifulSoup(driver.page_source, "lxml")

    port_list = []
    rows = soup.find_all("div", {"class": "sx-form__item ip-port"})
    country_lower = country.lower()

    for row in rows:

        row_country = row.find(
            "div", {"class": "ip-port__country"}).get_text().strip().replace(" ", "")

        row_country = row_country.lower()

        port = row.find(
            "div", {"class": "ip-port__info"}).get_text().strip()

        if (country_lower == row_country):

            port_list.append(row_country)

            port_list.append(port.replace(" ", "").replace("-", ""))

            # make minimum port by port_list
            minimum_port = port_list[1][:5]


def add_phone():  # 전화번호 생성

    global driver, country, device

    country = country_list_combobox.get()
    device = device_var_combobox.get()

    # countries dropdown click
    elem = driver.find_element_by_css_selector(
        '.statusBtn.btn.dropdown-toggle.btn-primary')
    ActionChains(driver).click(elem).perform()

    # countries search click and sendkeys
    elem = driver.find_element_by_css_selector('.form-control.countriesSearch')
    elem.clear()
    ActionChains(driver).click(elem).send_keys(country).perform()
    time.sleep(2)

    # countries choose click
    elem = driver.find_element_by_css_selector('.countryChoose')
    ActionChains(driver).click(elem).perform()

    # service search click and sendkeys
    service = "Kakao"
    elem = driver.find_element_by_id('servicesSearch')
    elem.clear()
    ActionChains(driver).send_keys_to_element(elem, service).perform()
    time.sleep(2)

    # kakaotalk service click
    elem = driver.find_element_by_css_selector(
        '.table.table-hover.table-stripped.table-condensed.table-small.tabbed')
    ActionChains(driver).click(elem).perform()
    time.sleep(0.5)

    # kakaotalk service set
    elem = driver.find_element_by_css_selector('.form-control.numbersToBuy')
    elem.clear()
    ActionChains(driver).click(elem).send_keys(device).perform()
    time.sleep(0.5)

    # kakaotalk service buy
    elem = driver.find_element_by_css_selector(
        '#leftForm > table > tbody > tr.tabbed.cell.info > td.radiotd > label > div > a')
    ActionChains(driver).move_to_element(elem).click().perform()

    time.sleep(2)


def add_port():  # 포트 생성, SMS 사이트와 PROXY 사이트 간의 이름 변환

    global driver, country, device

    country = country_list_combobox.get()
    device = device_var_combobox.get()

    # ip address click
    elem = driver.find_element_by_css_selector(
        'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
    ActionChains(driver).click(elem).perform()

    # add filter click
    elem = driver.find_element_by_css_selector('.ip-port__add-new-text')
    ActionChains(driver).click(elem).perform()

    # country click
    elem = driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.content-mwrap.flex.flex--wrap.targets-container.ip-port-targets > div:nth-child(2) > div > div > div')
    ActionChains(driver).click(elem).perform()

    # country replace
    if country == "Vietnam":

        country = "Viet Nam"

    if country == "Puertorico":

        country = "Puerto Rico"

    # country search click and sendkeys
    elem = driver.find_element_by_css_selector(
        'div.tooltip__inner > div.sx-select__search > input')
    ActionChains(driver).move_to_element(elem).send_keys(country).perform()

    # searched country click
    elem = driver.find_element_by_css_selector(
        'div.tooltip__inner > div.sx-select__list.ps')
    ActionChains(driver).click(elem).perform()

    # number of port set
    elem = driver.find_element_by_css_selector(
        'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.lbl-param-list > div > div > input')
    elem.clear()
    ActionChains(driver).send_keys_to_element(elem, "50").perform()

    # save button click
    elem = driver.find_element_by_css_selector('body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__body > div.sx-tabs__panel.ip-address-tab.is-active > form > div.content-row.sx-form__row.add-filter-container > div.sx-form__row-content.pckg-ip-port__filter-wrap > div.flex.flex--justify.flex--wrap.content-mwrap > button.button.button--04.package__form-btn.margin--t.add-filter-save')
    ActionChains(driver).move_to_element(elem).click().perform()

    time.sleep(2)


# 함수 선언 (GUI-tkinter))
def set_country_list():  # 대륙별 나라 콤보박스 변경

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


def add_set():  # 번호/포트 생성 및 설정 통합

    global country, device, driver, minimum_port
    country = country_list_combobox.get()
    device = device_var_combobox.get()

    run_selenium()

    driver.get("https://sms-activate.ru/en")

    add_phone()

    driver.get("https://dashboard.soax.com/proxy")

    if check_port():  # 포트 존재시

        get_port()  # 포트 가져오기

    else:  # 포트 미존재시

        add_port()  # 포트 생성

        driver.get("https://dashboard.soax.com/proxy")

        # ip address click
        elem = driver.find_element_by_css_selector(
            'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
        ActionChains(driver).click(elem).perform()

        get_port()  # 포트 가져오기

    # 추후 인증번호 가져오기를 위해 페이지 이동
    driver.get("https://sms-activate.ru/en/getNumber")

    print(minimum_port)

    launch_kakao()  # 카카오톡 실행 및 종료

    del_kakao()  # 카카오톡 강제종료 및 데이터 삭제

    del_proxy()  # 프록시 데이터 삭제

    launch_proxy()  # 프록시 실행 및 설정

    get_number()  # 전화번호 가져오기

    launch_sim()  # 디바이스 에뮬레이터 실행 및 설정


def add_set1():  # 번호/포트 생성

    global country, device, driver, minimum_port, state_text
    country = country_list_combobox.get()
    device = device_var_combobox.get()

    run_selenium()

    driver.get("https://sms-activate.ru/en")

    if country_check_var.get() == 1: # 번호 생성 체크시에만 작동

        state_update("번호 생성을 시작합니다.")

        add_phone()

    driver.get("https://dashboard.soax.com/proxy")

    state_update("포트 유효성을 확인합니다.")

    if check_port():  # 포트 존재시

        state_update("포트가 이미 존재합니다.")

        state_update("포트 최소값을 가져옵니다.")

        get_port()  # 포트 가져오기

    else:  # 포트 미존재시

        state_update("포트가 존재하지 않습니다.")

        state_update("포트 생성을 시작합니다.")

        add_port()  # 포트 생성

        driver.get("https://dashboard.soax.com/proxy")

        # ip address click
        elem = driver.find_element_by_css_selector(
            'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
        ActionChains(driver).click(elem).perform()

        state_update("포트 최소값을 가져옵니다.")

        get_port()  # 포트 가져오기

        interval_short()

    # 추후 인증번호 가져오기를 위해 페이지 이동
    driver.get("https://sms-activate.ru/en/getNumber")

    state_update("포트 최소값 : " + minimum_port)


def add_set2():  # 번호/포트 설정

    global country, device, driver, minimum_port
    country = country_list_combobox.get()
    device = device_var_combobox.get()

    run_selenium()

    state_update("번호/포트 설정을 시작합니다.")

    state_update("카카오톡 설정을 시작합니다.")

    launch_kakao()  # 카카오톡 실행 및 종료

    del_kakao()  # 카카오톡 강제종료 및 데이터 삭제

    state_update("프록시 설정을 시작합니다.")

    del_proxy()  # 프록시 데이터 삭제

    launch_proxy()  # 프록시 실행 및 설정

    state_update("번호 리스트를 가져옵니다.")

    get_number()  # 전화번호 가져오기

    state_update("에뮬레이터 설정을 시작합니다.")

    launch_sim()  # 디바이스 에뮬레이터 실행 및 설정

    state_update("국가 선택 후 카카오톡 가입 버튼을 눌러주세요.")


def check_add_set():

    if country_list_combobox.get() == "" or device_var_combobox.get() == "":

        msgbox.showerror("오류", "국가/생성수 설정을 완료하세요.")

    else:

        add_set1()


def state_update(text):
    
    # state_text.insert(END, "[" + str(datetime.now().time())[:8] + "]" + " " + text + "\n")
    # state_text.see(END)

    txt =  "[" + str(datetime.now().time())[:8] + "]" + " " + text
    print(txt)


# GUI-tkinter 구성 및 실행
window = Tk()
window.title("카카오톡 계정생성기 [BETA]")
window.geometry("420x310+0-40")

# 전체 프레임
frame_main = Frame(window)
frame_main.pack()

# 상단 프레임
frame_top = LabelFrame(frame_main, text="설정")
frame_top.pack(fill="x", padx=5, pady=5)

# 상단 대륙 프레임
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

# 상단 국가/생성수 프레임
frame_top2 = LabelFrame(frame_top, text="국가/생성수")
frame_top2.pack(fill="x", padx=5, pady=5)

country_label = Label(frame_top2, text="국가")
country_label.pack(side="left")

country_list_combobox = ttk.Combobox(
    frame_top2, height=20, state="readonly")
country_list_combobox.pack(side="left", fill="x", padx=5, pady=5)
country = country_list_combobox.get()

device_label = Label(frame_top2, text="생성수")
device_label.pack(side="left")

device_var_combobox = ttk.Combobox(
    frame_top2, height=20, state="readonly", values=device_var_list)
device_var_combobox.pack(side="left", fill="x", padx=5, pady=5)
device = device_var_combobox.get()

# 상단 옵션 프레임
frame_delay = LabelFrame(frame_top, text="대기시간(초)")
frame_delay.pack(fill="x", padx=5, pady=5)

delay_page_var_label = Label(frame_delay, text="페이지 전환")
delay_page_var_label.pack(side="left")

delay_page_var_list = ['10', '15', '20', '25', '30']
delay_page_var_combobox = ttk.Combobox(
    frame_delay, height=20, state="readonly", values=delay_page_var_list, width=4)
delay_page_var_combobox.current(2)
delay_page_var_combobox.pack(side="left", fill="x", padx=5, pady=5)
delay_page_var = int(delay_page_var_combobox.get())

delay_sms_var_label = Label(frame_delay, text="SMS 인증")
delay_sms_var_label.pack(side="left")

delay_sms_var_list = ['30', '40', '50', '60', '70', '80', '90']
delay_sms_var_combobox = ttk.Combobox(
    frame_delay, height=20, state="readonly", values=delay_sms_var_list, width=4)
delay_sms_var_combobox.current(3)
delay_sms_var_combobox.pack(side="left", fill="x", padx=5, pady=5)
delay_sms_var = int(delay_sms_var_combobox.get())

delay_openchat_var_label = Label(frame_delay, text="오픈채팅 입장")
delay_openchat_var_label.pack(side="left")

delay_openchat_var_list = ['30', '40', '50', '60', '70', '80', '90']
delay_openchat_var_combobox = ttk.Combobox(
    frame_delay, height=20, state="readonly", values=delay_openchat_var_list, width=4)
delay_openchat_var_combobox.current(1)
delay_openchat_var_combobox.pack(side="left", fill="x", padx=5, pady=5)
delay_openchat_var = int(delay_openchat_var_combobox.get())

# 상단 번호/포트 생성
port_check_var = IntVar()
port_checkbox = Checkbutton(frame_top, text="포트 생성", variable=port_check_var, state="disabled")
port_checkbox.select()
port_checkbox.pack(side="right", padx=5, pady=5)

country_check_var = IntVar()
country_checkbox = Checkbutton(frame_top, text="번호 생성", variable=country_check_var)
country_checkbox.select()
country_checkbox.pack(side="right", padx=5, pady=5)

# 하단 프레임
frame_bottom = LabelFrame(frame_main, text="실행")
frame_bottom.pack(fill="x", padx=5, pady=5)

btn1 = Button(frame_bottom, text="번호/포트 생성",
              command=check_add_set, width=16, bg="#99CCFF")
btn1.pack(side="left", padx=5, pady=5)

# btn2 = Button(frame_bottom, text="포트 생성",
#               command=check_add_set, width=16, bg="#99CCFF")
# btn2.pack(side="left", padx=5, pady=5)

btn3 = Button(frame_bottom, text="번호/포트 설정",
              command=add_set2, width=16, bg="#99CCFF")
btn3.pack(side="left", padx=5, pady=5)

btn4 = Button(frame_bottom, text="카카오톡 가입",
              command=register_kakao_1, width=16, bg="#99CCFF")
btn4.pack(side="left", padx=5, pady=5)

# # 상태창 프레임
# frame_state = Frame(frame_main)
# frame_state.pack()

# state_scrollbar = Scrollbar(frame_state)
# state_scrollbar.pack(side="right", fill="y")

# state_text = Text(frame_state, height=5, yscrollcommand=state_scrollbar.set)
# state_text.pack()

# state_scrollbar.config(command=state_text.yview)

# GUI 실행
window.resizable(False, False)
window.mainloop()

    # state_text.insert(END, str(datetime.now().time())[:8] + " 번호/포트 생성을 시작합니다.\n")
    # state_text.see(END)