from ctypes import sizeof
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

pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/kakao_label2_4.png', confidence=0.88))
pyautogui.moveTo(pos)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey("alt", "f4")
time.sleep(1)
pos = pyautogui.center(pyautogui.locateOnScreen(
        'macro_kakaotalk/date_version/images/exit.png', confidence=0.88))
pyautogui.moveTo(pos)
pyautogui.click()
