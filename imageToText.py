import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\TheDarkestMan\OneDrive - kmutnb.ac.th\Desktop\FridayAI\tesseract\tesseract.exe'
from PIL import Image
import autopy
import pyperclip

autopy.bitmap.capture_screen().save('screengrab.png')
img = Image.open('screengrab.png')
text = tess.image_to_string(img, lang='tha+eng')
pyperclip.copy(text)
spam = pyperclip.paste()
#autopy.bitmap.capture_screen().save('screengrab.png')