import os
import math
import pyautogui
import time


qty = 1
trussDesc = 0
type = 'comn'
span = 9
pitch = 2
time.sleep(3)

for p in range (3,14):
    pitch = pitch+1
    print(pitch)
    if pitch == 13:
        pitch = 3
    for x in range (10,41):
        span = span+1
        if span == 41:
            span = 10
        print(span)
        trussDesc=trussDesc+1
        
        slope = pitch*100/12
        decSpan= (span/2)*12
        rise = decSpan*(slope/100)
        rise = rise / 12
        
        if rise > 12:
            capHt = rise - 12
            capDec = capHt*12
            capSpan= capDec/(slope/100)
            capSpan = capSpan/12
            capSpan = capSpan*2
            capSpan= round(capSpan,2)
            
            pyautogui.typewrite(str(qty))
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(span))
            pyautogui.hotkey('tab')
            pyautogui.typewrite('B'+str(trussDesc))
            pyautogui.hotkey('tab')
            pyautogui.typewrite('HIPS')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(pitch)+'//12')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('esc')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            
            
            pyautogui.typewrite(str(qty))
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(capSpan))
            pyautogui.hotkey('tab')
            pyautogui.typewrite('C'+str(trussDesc))
            pyautogui.hotkey('tab')
            
            pyautogui.typewrite('COMN')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(pitch))
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('esc')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            
            
            
            
            
            
            
            
        else:
            cap = 'no cap'
        
            pyautogui.typewrite(str(qty))
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(span))
            pyautogui.hotkey('tab')
            pyautogui.typewrite('T'+str(trussDesc))
            pyautogui.hotkey('tab')
            pyautogui.typewrite('COMN')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.typewrite(str(pitch))
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('esc')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            
   
        
        
        


            
            
            
            
            
            
            
