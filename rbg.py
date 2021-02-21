#Q4apeR4eXK5XgDdhDBLMy76r
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('car.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Q4apeR4eXK5XgDdhDBLMy76r'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)