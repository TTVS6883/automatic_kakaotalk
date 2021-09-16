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
import pyautogui
import time

# cmd cd C:\Program Files\Google\Chrome\Application
# cmd chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"

# 변수 선언
global country_list, country, device
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


# 함수 선언 (에뮬레이터)
def interval_short(): # 대기시간 0.5초

    time.sleep(0.5)


def interval_middle(): # 대기시간 3초

    time.sleep(3)


def interval_long(): # 대기시간 6초

    time.sleep(6)


def launch_kakao(): # 카카오톡 실행 및 종료

    # 카카오톡 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # 카카오톡 종료
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def del_kakao(): # 카카오톡 강제종료 및 데이터 삭제

    # 카카오톡 앱 정보 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.dragRel(3, 0, 0.5, button='left')
    interval_short()

    # 강제종료 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_exit.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()
    interval_short()

    # 저장소 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_repository.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 데이터 지우기 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_delete.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_ok2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 홈 화면 복귀
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def del_proxy(): # 프록시 데이터 삭제

    # 프록시 앱 정보 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.dragRel(0, 3, 0.5, button='left')
    interval_short()

    # 저장소 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_repository.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 데이터 지우기 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_delete.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 홈 화면 복귀
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def launch_proxy(): # 프록시 실행 및 설정

    global minimum_port

    # 프록시 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # 1번 에뮬레이터 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_label.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()

    # 하단 스크롤
    pyautogui.press('down', 7)
    interval_short()

    # 호스트 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_host.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 호스트 입력
    pyautogui.typewrite('proxy.soax.com')
    interval_short()

    # 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 하단 스크롤
    pyautogui.press('down', 5)
    interval_short()

    # 포트 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 포트 입력 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_input.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 기본값(3128) 제거
    pyautogui.press('backspace', 10)

    # 멀티커맨드 비활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 포트 입력
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/proxy_port2.png", confidence=0.88)
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
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_port2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 확인 클릭
    pyautogui.press('down')
    pyautogui.press('right')
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_ok1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 상단 스크롤
    pyautogui.press('up', 7)

    # 멀티커맨드 비활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_label.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 프록시 Enable / 광고 나오는 경우 때문에 locateAllOnScreen으로 처리
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/proxy_active.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_middle()

    # 멀티커맨드 활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/proxy_label.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 홈 화면 복귀
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def launch_sim(): # 디바이스 에뮬레이터 실행 및 설정

    global phone_list

    # 디바이스 에뮬레이터 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # IMEI 활성화 / 예외처리
    try: # IMEI 비활성화 상태인 경우

        # IMEI 활성화
        pyautogui.press('down', 3)
        pos = pyautogui.center(pyautogui.locateOnScreen(
            'macro_kakaotalk/date_version/images/sim_active.png', confidence=0.88))
        pyautogui.moveTo(pos)
        pyautogui.click()
        interval_short()

    except TypeError: # IMEI 활성화 상태인 경우

        pass

    # 랜덤 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_random.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 핸드폰 번호 클릭
    pyautogui.press('down', 20)
    pyautogui.press('left', 1)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_edit1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 입력창 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_input.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 기본값 제거
    pyautogui.press('backspace', 25)
    interval_short()

    # 멀티커맨드 비활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_mobile.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 핸드폰 번호 입력
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/sim_mobile.png", confidence=0.88)
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
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_mobile.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 저장 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_save1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 국가 설정 진입
    pyautogui.press('down', 30)
    pyautogui.press('up', 2)
    pyautogui.press('left', 1)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_edit2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 국가 클릭
    pyautogui.press('down', 2)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_country.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def exit_sim(): # 디바이스 에뮬레이터 국가 설정 저장

    # 저장 클릭
    pyautogui.press('tab', 3)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/sim_save2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 홈 화면 복귀
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/home_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()


def register_kakao_1(): # 디바이스 에뮬레이터 국가 설정 저장, 카카오톡 실행, 권한허용, 회원가입 진입

    # launch_sim() 종료 후 exit_sim()으로 설정 저장 및 홈 화면 복귀
    exit_sim()

    # 카카오톡 실행
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_icon.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # 허용하기 클릭
    pyautogui.press('down', 5)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 전화 걸기 및 관리 허용 클릭
    pyautogui.press('tab', 2)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 기기 사진, 미디어, 파일 액세스 허용 클릭
    pyautogui.press('tab', 2)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 주소록 액세스 허용 클릭
    pyautogui.press('tab', 2)
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(1)

    # 새로운 카카오계정 만들기 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_register.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()


def register_kakao_2(): # 약관동의, 전화번호 확인, 인증번호 전송

    # # 1번 에뮬레이터 이동
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_allow_main.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()

    # 모두 동의합니다 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow3.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 하단 스크롤
    pyautogui.press('down', 10)

    # 선택항목 해제
    pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/images/kakao_allow3_5.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(0.6)

    pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/images/kakao_allow3_6.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(0.6)

    pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/images/kakao_allow3_7.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(0.6)

    # # 만 14세 이상입니다 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_allow3_1.png', confidence=0.8))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # # [필수]카카오계정 약관 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_allow3_2.png', confidence=0.8))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # # [필수]카카오계정 통합서비스 약관 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_allow3_3.png', confidence=0.8))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # # [필수]개인정보 수집 및 이용 동의 클릭
    # pyautogui.press('down', 10)
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_allow3_4.png', confidence=0.8))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_short()

    # 동의하고 계속 진행합니다 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow7.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(10)

    # 전화번호 확인 클릭
    try: # 확인 버튼 나오는 경우

        # 확인 클릭
        pos = pyautogui.center(pyautogui.locateOnScreen(
            'macro_kakaotalk/date_version/images/kakao_ok3.png', confidence=0.88))
        pyautogui.moveTo(pos)
        pyautogui.click()
        interval_short()

    except TypeError: # [필수]16세 이상 이용자입니다 나오는 경우

        # [필수]16세 이상 이용자입니다 클릭
        pos = pyautogui.center(pyautogui.locateOnScreen(
            'macro_kakaotalk/date_version/images/kakao_allow8.png', confidence=0.88))
        pyautogui.moveTo(pos)
        pyautogui.click()
        interval_short()

        # 확인 클릭
        pos = pyautogui.center(pyautogui.locateOnScreen(
            'macro_kakaotalk/date_version/images/kakao_ok5.png', confidence=0.88))
        pyautogui.moveTo(pos)
        pyautogui.click()
        interval_short()

    # 멀티커맨드 비활성화
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_label.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    # 인증번호 전송 확인 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/kakao_ok4.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    interval_middle()

    # # 인증번호 전송 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_ok4.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # interval_middle()

    # 인증요청 제한횟수 초과 예외처리
    try: # 인증요청 제한횟수 나오는 경우

        # 확인 클릭
        pos_list = pyautogui.locateAllOnScreen(
            "macro_kakaotalk/date_version/images/kakao_ok4.png", confidence=0.88)
        pos_list = list(pos_list)

        for i in pos_list:

            pos = pyautogui.center(i)
            pyautogui.moveTo(pos)
            pyautogui.click()

    except TypeError: # 인증요청 제한횟수 없는 경우

        pass
    

def register_kakao_3(): # 인증번호 입력, 비밀번호 설정, 프로필 설정, 가입 완료

    global sms_list

    # # 멀티커맨드 비활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_input1.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 인증번호 가져오기
    get_sms()

    # 인증번호 입력 (화면 선택 갯수에 따른 인덱스 값 조정방법 생각)
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/kakao_input2.png", confidence=0.88)
    pos_list = list(pos_list)
    sms_list_index = 0

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()
        pyautogui.typewrite(sms_list[sms_list_index])
        sms_list_index += 1

    interval_short()

    # # 인증번호 입력 (화면 선택 갯수에 따른 인덱스 값 조정방법 생각)
    # pos_list = pyautogui.locateAllOnScreen(
    #     "macro_kakaotalk/date_version/images/kakao_input2.png", confidence=0.84)
    # pos_list = list(pos_list)
    # sms_list_index = 0

    # for i in pos_list:

    #     pos = pyautogui.center(i)
    #     pyautogui.moveTo(pos)
    #     pyautogui.click()
    #     pyautogui.typewrite(sms_list[sms_list_index])
    #     sms_list_index += 1

    # interval_short()

    # # 멀티커맨드 활성화
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_white.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # pyautogui.hotkey('ctrl', '9')
    # interval_short()

    # 확인 클릭
    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/kakao_ok5.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    time.sleep(10)

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_ok5.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # time.sleep(10)

    # 멀티커맨드 활성화 / 비밀번호 클릭 및 입력
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_pw1.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()
    pyautogui.typewrite("ehlswkdrnr!!")
    interval_short()

    # 비밀번호 확인 클릭 및 입력
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_pw2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.typewrite("ehlswkdrnr!!")
    interval_short()

    # 멀티커맨드 비활성화 / 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_label2.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    pos_list = pyautogui.locateAllOnScreen(
        "macro_kakaotalk/date_version/images/kakao_ok5.png", confidence=0.88)
    pos_list = list(pos_list)

    for i in pos_list:

        pos = pyautogui.center(i)
        pyautogui.moveTo(pos)
        pyautogui.click()

    time.sleep(10)

    # # 확인 클릭
    # pos = pyautogui.center(pyautogui.locateOnScreen(
    #     'macro_kakaotalk/date_version/images/kakao_ok5.png', confidence=0.88))
    # pyautogui.moveTo(pos)
    # pyautogui.click()
    # time.sleep(10)

    # 멀티커맨드 활성화 / 이름 클릭 및 입력
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_name.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '9')
    interval_short()

    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_name.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.typewrite("abcabc")
    interval_short()

    # 주소록 친구 자동 추가 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_allow9.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 확인 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_ok5.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

    # 기본 이미지로 설정 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_image.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_middle()

    # 이메일 등록 나중에 하기 클릭
    pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_later.png', confidence=0.88))
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short() 


# 함수 선언 (셀레니움)
def run_chrome(): # 크롬 실행

    os.chdir('C:\Program Files\Google\Chrome\Application')
    os.system(
        'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')
    return 0


def run_selenium(): # 셀레니움 실행

    global driver

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "macro_kakaotalk/date_version/chromedriver.exe"
    
    driver = webdriver.Chrome(
        executable_path=chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)


def check_port(): # 포트 존재여부 확인

    global driver, soup, port_list, country, bool_port

    # ip address click
    elem = driver.find_element_by_css_selector(
        'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
    ActionChains(driver).click(elem).perform()
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, "lxml")

    bool_port = False # 포트 미존재
    rows = soup.find_all("div", {"class": "sx-form__item ip-port"})
    country_lower = country.lower()

    for row in rows:

        row_country = row.find(
            "div", {"class": "ip-port__country"}).get_text().strip().replace(" ", "")

        row_country = row_country.lower()

        if (country_lower == row_country):

            bool_port = True # 포트 존재

    return bool_port


def get_number(): # 전화번호 가져오기

    global driver, soup, phone_list

    soup = BeautifulSoup(driver.page_source, "lxml")

    phone_list = []
    rows = soup.find("table", {"id": "getNumberTable"}).find_all(
        "input", {"class": "form-control"})

    for row in rows:

        phone_list.append(row["value"])


def get_sms(): # 인증번호 가져오기

    global driver, soup, sms_list

    soup = BeautifulSoup(driver.page_source, "lxml")

    sms_list = []
    rows = soup.find("table", {"id": "getNumberTable"}).find_all("strong")

    for row in rows:

        sms_list.append(row.get_text())


def get_port(): # 포트 가져오기

    global driver, soup, port_list, country, minimum_port
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


def add_phone(): # 전화번호 생성

    global driver, country, device

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


def add_port(): # 포트 생성, SMS 사이트와 PROXY 사이트 간의 이름 변환

    global driver, country, device

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


# 함수 선언 (GUI-tkinter))
def set_country_list(): # 대륙별 나라 콤보박스 변경

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


def add_btn1(): # 전화번호 생성

    global country, device, driver
    country = country_list_combobox.get()
    device = device_var_combobox.get()

    run_selenium()

    driver.get("https://sms-activate.ru/en")
    add_phone()


def add_btn2(): # 포트 생성

    global country, device, minimum_port, driver
    country = country_list_combobox.get()
    device = device_var_combobox.get()

    run_selenium()

    driver.get("https://dashboard.soax.com/proxy")

    if check_port(): # 포트 존재시

        get_port() # 포트 가져오기

        driver.get("https://sms-activate.ru/en/getNumber") # 추후 인증번호 가져오기를 위해 페이지 이동

    else: # 포트 미존재시

        add_port() # 포트 생성

        driver.get("https://dashboard.soax.com/proxy")

        # ip address click
        elem = driver.find_element_by_css_selector(
        'body > div.page__wrapper.page__wrapper--with-subbar.packages > div.page__main-content.package > div.package__sect-twice > section:nth-child(1) > div.panel > div > div.sx-tabs__header > div:nth-child(2)')
        ActionChains(driver).click(elem).perform()

        get_port() # 포트 가져오기
        
        driver.get("https://sms-activate.ru/en/getNumber") # 추후 인증번호 가져오기를 위해 페이지 이동


def run_ld(): # 전화번호/포트 설정

    launch_kakao() # 카카오톡 실행 및 종료

    del_kakao() # 카카오톡 강제종료 및 데이터 삭제

    del_proxy() # 프록시 데이터 삭제

    launch_proxy() # 프록시 실행 및 설정

    get_number() # 전화번호 가져오기

    launch_sim() # 디바이스 에뮬레이터 실행 및 설정


# GUI-tkinter 구성 및 실행
window = Tk()
window.title("카카오톡 계정생성기 [BETA]")
window.geometry("420x300+0-40")

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

country_list_combobox = ttk.Combobox(
    frame_top2, height=20, width=28, state="readonly")
country_list_combobox.pack(side="left", fill="x", padx=5, pady=5)
country = country_list_combobox.get()

device_var_combobox = ttk.Combobox(
    frame_top2, height=20, state="readonly", values=device_var_list)
device_var_combobox.pack(side="left", fill="x", padx=5, pady=5)
device = device_var_combobox.get()

# 하단 프레임
frame_bottom = LabelFrame(frame_main, text="실행")
frame_bottom.pack(fill="x", padx=5, pady=5)

frame_bottom1 = LabelFrame(frame_bottom, text="번호/포트 생성 및 설정")
frame_bottom1.pack(fill="x", padx=5, pady=5)

btn2 = Button(frame_bottom1, text="번호 생성", command=add_btn1, width=16)
btn2.pack(side="left", padx=5, pady=5)

btn3 = Button(frame_bottom1, text="포트 생성", command=add_btn2, width=16)
btn3.pack(side="left", padx=5, pady=5)

btn4 = Button(frame_bottom1, text="번호/포트 설정", command=run_ld, width=16)
btn4.pack(side="left", padx=5, pady=5)

frame_bottom2 = LabelFrame(frame_bottom, text="카카오톡 가입")
frame_bottom2.pack(fill="x", padx=5, pady=5)

btn5 = Button(frame_bottom2, text="가입 1단계", command=register_kakao_1, width=16)
btn5.pack(side="left", padx=5, pady=5)

btn6 = Button(frame_bottom2, text="가입 2단계", command=register_kakao_2, width=16)
btn6.pack(side="left", padx=5, pady=5)

btn7 = Button(frame_bottom2, text="인증번호 입력",
              command=register_kakao_3, width=16)
btn7.pack(side="left", padx=5, pady=5)

# GUI 실행
window.resizable(False, False)
window.mainloop()