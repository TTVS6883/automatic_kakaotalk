import os

os.chdir('C:\Program Files\Google\Chrome\Application')
os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTemp"')