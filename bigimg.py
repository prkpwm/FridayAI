import requests
import json
import time
data = {
    'style': 'photo',
    'noise': '3',
    'x2': '2',
    'input': 'car.jpg'
}

r = requests.post(
    url='https://bigjpg.com/api/task/',
    headers={'X-API-KEY': '1c2232048d5d41248cdd1e3f3d0948ad'},
    data={'conf': json.dumps(data)}
)
res = r.json()
print(res)
'''
time.sleep(180)
r = requests.get(url='https://bigjpg.com/api/task/{}'.format(res['tid']))
response = r.json()
print(response)
if response.status_code == requests.codes.ok:
    with open('screengrab.png', 'wb') as out:
        out.write(response.content)
        print("ลบภาพพื้นหลังเรียบร้อยค่ะ")

else:
    print("Error:", response.status_code, response.text)
    print("ไม่สามารถลบภาพพื้นหลังได้ค่ะ")

'''