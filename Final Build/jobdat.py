import pyautogui
import sys
import os
import pickle

import win32gui
import re
import win32clipboard
import time

#ask user for job number 

#action = pyautogui.prompt('Type to create a new job type load to load a job')

#TODO pull up job in icommand???
#focus window try except to open window 
# collect data from icommand
#tab through using auto gui to get a start location and pyperclip to copy to clipbored and assign vars to them 

#TODO still having issues copying data 
def new ():
     
    from pywinauto.application import Application
    
    jobNumber = pyautogui.prompt('job number')

    app = Application().Connect(title=u'iCommand', class_name='WindowsForms10.Window.8.app.0.201d787_r9_ad1')
    windowsformswindowappdrad = app.iCommand
    windowsformswindowappdrad.SetFocus()
    pyautogui.hotkey("alt", "w", "j")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    try:
        windowsformseditappdrad = windowsformswindowappdrad[u'49']
        windowsformseditappdrad.Select()
        windowsformseditappdrad2 = windowsformswindowappdrad[u'77']
        windowsformseditappdrad2.DoubleClickInput()
    except:
        pyautogui.alert('click in job description and click ok on this message')
        time.sleep(2)
   
    pyautogui.hotkey("ctrl", "a")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)

    try:
        
        win32clipboard.OpenClipboard()
        jobName = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(2)
        win32clipboard.OpenClipboard()
        jobName = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    else:
        pass

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(2)

    pyautogui.hotkey("ctrl", "c")
    try:
        win32clipboard.OpenClipboard()
        salesman = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
      
        time.sleep(1)
        win32clipboard.OpenClipboard()
        salesman = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(2)
    
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        designer = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        designer = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(2)

    pyautogui.hotkey("ctrl", "c")
    
    try:
        win32clipboard.OpenClipboard()
        region = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        region = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass

    pyautogui.hotkey('tab')
    time.sleep(2)

    pyautogui.hotkey("ctrl", "c")
    
    try:
        win32clipboard.OpenClipboard()
        street = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        
        time.sleep(1)
        win32clipboard.OpenClipboard()
        street = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
    pyautogui.hotkey('tab')
    time.sleep(2)

    pyautogui.hotkey("ctrl", "c")
    
    try:
        win32clipboard.OpenClipboard()
        city = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        time.sleep(1)
        win32clipboard.OpenClipboard()
        city = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(2)

    pyautogui.hotkey("ctrl", "c")
    
    try:
        win32clipboard.OpenClipboard()
        zipCode = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        zipCode = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        quotedPrice = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        quotedPrice = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
    from pywinauto.application import Application

    app = Application().Connect(title=u'iCommand', class_name='WindowsForms10.Window.8.app.0.201d787_r9_ad1')
    windowsformswindowappdrad = app.iCommand
    windowsformseditappdrad = windowsformswindowappdrad[u'45']
    windowsformseditappdrad.DoubleClickInput()

    try:
        win32clipboard.OpenClipboard()
        totalPrice = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        totalPrice = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass
        
    pyautogui.hotkey("alt", "w", "c")
    
    
    time.sleep(5)
   
    
    
    windowsformseditappdrad = windowsformswindowappdrad[u'53']
    windowsformseditappdrad.DoubleClickInput()
    pyautogui.hotkey("ctrl", "a")
    time.sleep(2)
    
    pyautogui.hotkey("ctrl", "c")
    try:
        win32clipboard.OpenClipboard()
        customerCode = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
      
        time.sleep(1)
        win32clipboard.OpenClipboard()
        customerCode = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass    
    pyautogui.hotkey('tab')
    time.sleep(2)
    
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        customerName = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        
        time.sleep(1)
        win32clipboard.OpenClipboard()
        customerName = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass   
    windowsformseditappdrad2 = windowsformswindowappdrad[u'25']
    windowsformseditappdrad2.DoubleClickInput()
   
    pyautogui.hotkey("ctrl", "a")
    time.sleep(2)
    
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        billingStreet = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
     
        time.sleep(1)
        win32clipboard.OpenClipboard()
        billingStreet = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass    
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        billingCity = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        
        time.sleep(1)
        win32clipboard.OpenClipboard()
        billingCity = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass    
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey("ctrl", "c")

    try:
        win32clipboard.OpenClipboard()
        billingZip = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
       
        time.sleep(1)
        win32clipboard.OpenClipboard()
        billingZip = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        pass
    else:
        pass


    print (jobName, salesman, region, street, city,  zipCode, quotedPrice, totalPrice,customerCode,customerName,billingStreet,billingCity,billingZip, sep="\n")


    jobNumber= str(jobNumber)
    #save copied info with pickle
    jobInfo = {'Job Name': jobName, 'Salesman': salesman,'Designer':designer,'Region':region,'Street Name':street,'Zip Code':zipCode,'Quoted Price':quotedPrice,'Total Price':totalPrice,'Customer Code':customerCode,'Customer Name':customerName,'Billing Street':billingStreet,'Billing City':billingCity,'Billing Zip':billingZip} 
    pickle.dump( jobInfo, open( jobNumber, "wb") )
    
    print(jobInfo)
    

#load job
def load ():
    jobNumber = pyautogui.prompt('job number')
    jobNumber= str(jobNumber)
    
    jobInfo = pickle.load( open( jobNumber, "rb" ))
    
    print (jobInfo)
    
    


#
#if action == 'new':
#    new()
#if action == 'load':
#    load()