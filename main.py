import os
import pprint
import re
import time
import requests
import autopy
import playsound
import pyautogui
import pyperclip
import pytesseract as tess
from google_trans_new import google_translator
from PIL import Image

import AI

obj = AI.Friday()
trans = google_translator()
tess.pytesseract.tesseract_cmd = r'C:\Users\TheDarkestMan\OneDrive - kmutnb.ac.th\Desktop\FridayAI\tesseract\tesseract.exe'


def t2s(text):
    obj.text2speech(text, lang='th')


t2s('สวัสดีค่ะ,ฉันเป็นผู้ช่วยส่วนตัวคุณค่ะ')

while True:
    status, command = obj.hot_word_detect(lang='th')
    if status:
        for i in range(3):
            res = obj.mic_input(lang='th')
            if re.search('การค้นหาแบบทวิภาค|binary search|binary', res):
                f = open("code/binary_search.txt", "r")
                c = 0
                for x in f:
                    pyautogui.keyDown('shift')
                    for i in range(c):
                        pyautogui.press(['tab'])
                    pyautogui.keyUp('shift')
                    time.sleep(0.01)
                    pyautogui.write(x, interval=0.02)
                    c += 1
                f.close()
                t2s("เรียบร้อยค่ะ")
                break

            if re.search('การเรียงแบบรวดเร็ว|quick sort|quick sorted|quick exhaust', res):
                f = open("code/quick_sort.txt", "r")
                c = 0
                for x in f:
                    pyautogui.keyDown('shift')
                    for i in range(c):
                        pyautogui.press(['tab'])
                    pyautogui.keyUp('shift')
                    pyautogui.write(x, interval=0.02)
                    c += 1
                f.close()
                t2s("เรียบร้อยค่ะ")
                break

            if re.search('link list|linked list', res):
                f = open("code/Linked_list.txt", "r")
                c = 0
                for x in f:
                    pyautogui.keyDown('shift')
                    for i in range(c):
                        pyautogui.press(['tab'])
                    pyautogui.keyUp('shift')
                    pyautogui.write(x, interval=0.02)
                    c += 1
                f.close()
                t2s("เรียบร้อยค่ะ")
                break

            if re.search("ตอนนี้อุณหภูมิเท่าไหร่", res):
                city = res.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                t2s(weather_res)
                break

            if re.search('ตอนนี้เวลาเท่าไหร่', res):
                time = obj.tell_me_time()
                t2s(time)
                break

            if re.search('อ่านข่าว', res):
                import requests
                from bs4 import BeautifulSoup
                url = "https://news.google.com/rss?hl=th&gl=TH&ceid=TH:th"
                web = requests.get(url)
                soup = BeautifulSoup(web.text, 'html.parser')
                findword = soup.find_all("title")
                for new in findword:
                    new = str(new).split("<title>")[1]
                    new = str(new).split("</title>")[0]
                    new = str(new).split("-")[0]
                    print(new)
                    t2s(new)
                break

            if re.search('วันนี้วันที่เท่าไหร่', res):
                date = obj.tell_me_date()
                print(date)
                trans = trans.translate(date, lang_tgt='th')
                t2s(trans)
                break

            if re.search('เปิด', res):
                domain = res.split(' ')[-1]
                open_result = obj.website_opener(domain)
                print(open_result)
                t2s("เปิดเรียบร้อยค่ะ")
                break

            if re.search('ทำอะไรได้บ้าง', res):
                ans = "I can do lots of things"
                ans = ans.replace('"', "'")
                trans = trans.translate(ans, lang_tgt='th')
                t2s(trans)
                break

            if re.search('เขียนคำว่า', res):
                print(res)
                domain = res.split(' ')[-1]
                t2s(domain)
                pyautogui.write(domain, interval=0.16)
                t2s("เรียบร้อยค่ะ")
                break

            if re.search('แปลงภาพ', res):
                autopy.bitmap.capture_screen().save('screengrab.png')
                img = Image.open('screengrab.png')
                text = tess.image_to_string(img, lang='tha+eng')
                pyperclip.copy(text)
                spam = pyperclip.paste()
                t2s("แปลงภาพเรียบร้อยค่ะ")
                break

            if re.search('แปลภาษา', res):
                ans = pyperclip.paste()
                trans = google_translator()
                trans = trans.translate(ans, lang_tgt='th')
                pyperclip.copy(trans)
                spam = pyperclip.paste()
                t2s(trans)
                break

            if re.search('ลบภาพพื้นหลัง', res):
                response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': open('screengrab.png', 'rb')},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': 'Q4apeR4eXK5XgDdhDBLMy76r'},
                )
                if response.status_code == requests.codes.ok:
                    with open('screengrab.png', 'wb') as out:
                        out.write(response.content)
                        t2s("ลบภาพพื้นหลังเรียบร้อยค่ะ")
                else:
                    print("Error:", response.status_code, response.text)
                    t2s("ไม่สามารถลบภาพพื้นหลังได้ค่ะ")
                break
    else:
        continue
