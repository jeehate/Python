import cv2
import pytesseract
from gtts import gTTS
import os
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App) :
    def build(self) :

        language = 'en'

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        img = cv2.imread('testImage.png')

        result = pytesseract.image_to_string(img)
        print(result)

        myobj = gTTS(text=result, lang=language, slow=False)
        myobj.save("testSpeech.mp3")
        os.system("start testSpeech.mp3")

if __name__ == '__main__' :
    app = MainApp()
    app.run()
