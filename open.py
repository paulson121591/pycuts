import os
import sys
import subprocess
import pyautogui
import shutil

job= 'PS19368'
file= job +' Order.pdf'


#os.rename(r'C:\Users\Itw User\Desktop\code\\'+file,'O:\Jobs\PS19368\Order\\'+file)
shutil.move(r'C:\Users\Itw User\Desktop\code\\'+file,'O:\Jobs\\'+job+'\Order\\'+file)


#subprocess.Popen(r'explorer /select,"O:\Jobs\"'+file+"\Order")
pyautogui.alert('did it work?')
