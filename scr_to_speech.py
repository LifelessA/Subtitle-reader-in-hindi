import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"Tesseract-OCR//tesseract.exe"

import cv2

import threading
import numpy as np
import pyttsx3,pyautogui

from googletrans import Translator


class Scr_To_Speech:
    v,nv,wr = ["a",1,2],["a"],[]
    def __init__(self):
        self.work()
        
    

    def work(self):
        self.c=0
        self.co = 0
        width,height = GetSystemMetrics(0),GetSystemMetrics(1) # 0 Define the width of window and 1 is Define height of window
        while True:
            scr_img = ImageGrab.grab(bbox=(0,0,width,height)) # This is grab image of window
            arr_img = np.array(scr_img) # It convert image in to array form
            color_img = cv2.cvtColor(arr_img,cv2.COLOR_BGR2RGB) # This command fetch right color of an image
            fr=color_img[870:1200,0:1990] # This is define new windows size 
            kernal = np.ones((4,4), np.uint8) # It is not importen now
            ig = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY) # This command convet color image into black and white image
            ig2 = cv2.blur(ig,(2,2),3) # This command makes image blur
            ig2 = cv2.blur(ig,(2,2),3) # Again in I am blur the image 
            _,it = cv2.threshold(ig2, 220, 255, cv2.THRESH_BINARY_INV) # This command conver image into white color to black and all another color into white
            cv2.imshow("output_2", it) # This command show finale image
            self.co = self.co+1
            if (self.c%5==0):
                #f(frame)
                #f(it)
                threading.Thread(target=self.f,args=(it,)).start()
        
            #say()
            self.c+=1
            if cv2.waitKey(1) & 0xFF == ord('q'): # In the middle of programing running if we press q button it will break the loop and close the window
                break
    
    def ind(self,x,y):
        dic = {}
        c=0
        for i in x:
            dic[c]= i
            c+=1
        l = len(dic)
        dic[l-(l+l)] = dic[0]
        co=1
        for j in range(1,l):
            dic[j-(j+j)] = dic[l-co]
            co+=1 
        # print(dic)
        return dic[y]
    
    def f(self,x):
        #cc = set(self.wr)
        
        
        text = tess.image_to_string(x)
        
        print(len(self.v),len(self.nv))
        
        if text == "":
            print("ok")
        else:
            if text == self.v[-1]:
                
                print("False")
            else:
                print("text =",text,"==>","v[-1] =",self.v[-1])
                #v.pop(0)
                #print("v[-1] =",v[-1])
                #print(v)
                self.v.append(text)
                try:
                    self.speak(self.tran(text))
                except Exception:
                    self.v.remove(text)
    
    def speak(self,audio):  #here audio is var which contain text
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        #print(voices)
        engine.setProperty('voice',voices[1].id)
        engine.setProperty('rate',265)
        engine.say(audio)
        engine.runAndWait()

    def tran(self,x):
        translatr = Translator()
        if "Okey" == x:
            tra = translatr.translate("ok", dest="hi")
        tra = translatr.translate(str(x), dest="hi")
        #print(tra.text)
        return tra.text
    


    
        