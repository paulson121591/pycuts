import pyautogui
import sys
import os
import pickle

import win32gui
import re
import win32clipboard
import time

from pywinauto.application import Application
app = Application().Connect(title=u'iCommand', class_name='WindowsForms10.Window.8.app.0.201d787_r9_ad1')
windowsformswindowappdrad = app.iCommand
windowsformswindowappdrad.SetFocus()


windowsformswindowbappdrad = windowsformswindowappdrad[u'77']
windowsformswindowbappdrad.SetFocus()


pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")

win32clipboard.OpenClipboard()
jobName = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad2 = windowsformswindowappdrad[u'28']
windowsformswindowbappdrad2.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)



pyautogui.hotkey("ctrl", "c")

win32clipboard.OpenClipboard()
salesman = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad3 = windowsformswindowappdrad[u'68']
windowsformswindowbappdrad3.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
designer = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad4 = windowsformswindowappdrad[u'58']
windowsformswindowbappdrad4.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
region = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad5 = windowsformswindowappdrad[u'60']
windowsformswindowbappdrad5.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
street = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad6 = windowsformswindowappdrad[u'23']
windowsformswindowbappdrad6.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")

win32clipboard.OpenClipboard()
city = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


windowsformswindowbappdrad7 = windowsformswindowappdrad[u'15']
windowsformswindowbappdrad7.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
zipCode = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
time.sleep(2)

windowsformswindowbappdrad8 = windowsformswindowappdrad[u'56']
windowsformswindowbappdrad8.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
quotedPrice = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformswindowbappdrad9 = windowsformswindowappdrad[u'38']
windowsformswindowbappdrad9.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)
pyautogui.hotkey("ctrl", "c")

win32clipboard.OpenClipboard()

date = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

windowsformseditappdrad = windowsformswindowappdrad[u'43']
windowsformseditappdrad.SetFocus()
pyautogui.hotkey("ctrl", "a")
time.sleep(2)

pyautogui.hotkey("ctrl", "c")
win32clipboard.OpenClipboard()
totalPrice = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()