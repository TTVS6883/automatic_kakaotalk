from time import time
import pyautogui
import keyboard
import time
import pyperclip


def interval_long():
    time.sleep(6)


def interval_middle():
    time.sleep(2)


def interval_short():
    time.sleep(0.5)


# 카카오
# 멀티 커맨드 활성화/비활성화
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/main0.png'))
pyautogui.moveTo(pos)
pyautogui.click()
interval_short
pyautogui.hotkey('ctrl', '9')
interval_short

# 카카오톡 앱 설정 진입
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao1.png'))
pyautogui.moveTo(pos)
pyautogui.dragRel(3, 0, 0.5, button='left')

interval_short()

# 강제종료 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao2.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 확인 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao3.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 저장소 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao4.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 삭제 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao5.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 확인 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/kakao6.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 메인화면 복귀
pyautogui.press('esc')
interval_short()
pyautogui.press('esc')
interval_short()


# 프록시
# 프록시 실행
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/proxy1.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_long()

# 아래로 스크롤
pyautogui.press('down', 5)
interval_short()

# 멀티 커맨드 활성화/비활성화
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/proxy0.png'))
pyautogui.moveTo(pos)
pyautogui.click()
interval_short
pyautogui.hotkey('ctrl', '9')
interval_short

# 포트 하나씩 열기
pos_list = pyautogui.locateAllOnScreen(
    "macro_kakaotalk/date_version/proxy2.png", confidence=0.98)
pos_list = list(pos_list)

for i in pos_list:
    pos = pyautogui.center(i)
    pyautogui.moveTo(pos)
    pyautogui.click()
    interval_short()

# 입력창 하나씩 클릭
pos_list = pyautogui.locateAllOnScreen(
    "macro_kakaotalk/date_version/proxy3.png", confidence=0.96)
pos_list = list(pos_list)

for i in pos_list:
    pos = pyautogui.center(i)
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.press('backspace', 5)
    pyautogui.typewrite('12345')

# 확인 하나씩 클릭
pos_list = pyautogui.locateAllOnScreen(
    "macro_kakaotalk/date_version/proxy4.png", confidence=0.98)
pos_list = list(pos_list)

for i in pos_list:
    pos = pyautogui.center(i)
    pyautogui.moveTo(pos)
    pyautogui.click()

# 멀티 커맨드 활성화/비활성화
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/proxy0.png'))
pyautogui.moveTo(pos)
pyautogui.click()
interval_short
pyautogui.hotkey('ctrl', '9')
interval_short

# 프록시 실행
pyautogui.press('up', 5)
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/proxy5.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_middle()

# 메인화면 복귀
pyautogui.press('esc')
interval_short()


###################
# 심오퍼레이터 진입
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim1.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_middle()

# IMEI 켜기
pyautogui.press('down', 3)
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim2.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# IMEI RANDOM 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim3.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# Mobile No EDIT 클릭
pyautogui.press('down', 20)
pyautogui.press('left', 1)
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim4.png'))
pyautogui.moveTo(pos)
pyautogui.click()

interval_short()

# 입력창 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim5.png'))
pyautogui.moveTo(pos)
pyautogui.click()

# 기존값 삭제
pyautogui.press('backspace', 20)

interval_short()

# 번호 입력
pyautogui.typewrite('01012345678')

interval_short()

# 확인 클릭
pos = pyautogui.center(pyautogui.locateOnScreen(
    'macro_kakaotalk/date_version/sim6.png'))
pyautogui.moveTo(pos)
pyautogui.click()

pyautogui.typewrite('12345')
