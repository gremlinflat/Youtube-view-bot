import webbrowser
import time
import os


#url = "https://www.youtube.com/watch?v=NFShseukuCA"
url = "https://www.youtube.com/watch?v=X0BfWe-trsY"
refresh = input("refresh : ")

#view = input("Enter view : ")
view = 1000
brow = "chrome.exe"

def OpenUrl():
        print("Successfully Viwed. ")
        os.system(" killall -9 " + brow)
        webbrowser.open(url)
        time.sleep(int(refresh))

for i in range(view):
        OpenUrl()
        if(i%20==0):
                os.system("TASKKILL /F /IM chrome.exe")