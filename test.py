"""
import pyautogui
f = open("code/binary_search.txt", "r")
pyautogui.write("---\n",interval=1)
c=0
for x in f:
    pyautogui.keyDown('shift')
    for i in range(c):
        pyautogui.press(['tab'])
    pyautogui.keyUp('shift') 
    pyautogui.write(x, interval=0.02)
    c+=1
f.close()
"""
import AI
import re
import pprint
from googletrans import Translator
import os, playsound
import pyautogui
import time
obj = AI.Friday()

trans = Translator()

def t2s(text):
    obj.text2speech(text,lang='th')


import requests
from bs4  import BeautifulSoup
url = "https://news.google.com/rss?hl=th&gl=TH&ceid=TH:th"
web = requests.get(url)
soup = BeautifulSoup(web.text,'html.parser')
findword = soup.find_all("title")
for new in findword:
    new = str(new).split("<title>")[1]
    new = str(new).split("</title>")[0]
    new = str(new).split("-")[0]
    print(new)
    t2s(new)