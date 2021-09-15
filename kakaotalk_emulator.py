from time import time
import pyautogui
import keyboard
import time
import pyperclip


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


launch_exit_kakao()
del_kakao()
del_proxy()
launch_proxy()
launch_sim()
