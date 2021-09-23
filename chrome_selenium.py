import os

chrome_path_txt = 'chrome_path.txt'

file = open(chrome_path_txt, 'r', encoding='UTF8')
chrome_path = file.readline()
chrome_path = str(chrome_path).replace('\\\\', '\\')

os.chdir(chrome_path)
os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')