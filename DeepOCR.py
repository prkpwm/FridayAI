import requests
 
url = "https://api.aiforthai.in.th/panyapradit-ocr"
 
files = {'uploadfile':open('Capture.jpg', 'rb')}
 
headers = {
    'Apikey': "a3QiBLIRTLbCbfGAvJ0v8JoagvKaa4U6",
    }
 
response = requests.post(url, files=files, headers=headers)
 
print(response.json())