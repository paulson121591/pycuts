import pyautogui
import time
from pynput import keyboard
import os
import subprocess
import webbrowser




# The key combination to check
COMBINATIONS = [
    {keyboard.KeyCode(char='`')},
    {keyboard.KeyCode(char='`')}
]

# The currently active modifiers
current = set()

def execute():
    action = pyautogui.prompt('This lets the user type in a string and press OK.')
    pyautogui.moveTo(1000, 0, duration=0)

#// ANCHOR actions that are configured for my computer will not work on others 

# ANCHOR this opens the modal in icommand program
    if action == 'mod':
        try:
            mod = pyautogui.locateOnScreen('img/mod.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick) 
            
        except:
            try:
                mod = pyautogui.locateOnScreen('img/model2.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
            except:
                pyautogui.alert('not found')

# ANCHOR this opens the job folder icommand program
    if action == 'open job':
        try:
            mod = pyautogui.locateOnScreen('img/jobfolder.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick) 
            
        except:
            try:
                # FIXME this is not finding the cmd2.png consistently
                mod = pyautogui.locateOnScreen('img/cmd2.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
                time.sleep(1)

                mod = pyautogui.locateOnScreen('img/jobfolder.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
            except:
                try:
                    mod = pyautogui.locateOnScreen('img/icommand.png') 
                    toClick = pyautogui.center(mod)
                    pyautogui.click(toClick) 
                    time.sleep(1)

                    mod = pyautogui.locateOnScreen('img/jobfolder.png') 
                    toClick = pyautogui.center(mod)
                    pyautogui.click(toClick)
                except:
                    pyautogui.alert('not found')
# ANCHOR this opens the design software in icommand program
    if action == 'dgn':
         try:
            mod = pyautogui.locateOnScreen('img/design.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick) 
        
         except:
             pyautogui.alert('not found')

 # ANCHOR this opens the command center in icommand program            

    if action == 'cmd':
        try:
            mod = pyautogui.locateOnScreen('img/icommand.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick) 
            
        except:
            try:
                mod = pyautogui.locateOnScreen('img/cmd2.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
            except:
                pyautogui.alert('not found')  

# ANCHOR this deletes a truss in icommand program                  
    
    if action == 'dlt truss':
            try:
                mod = pyautogui.locateOnScreen('img/trusses.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
                
                mod = pyautogui.locateOnScreen('img/delete.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
    
            except:
                pyautogui.alert('not found')  

# ANCHOR this adds a flat in icommand program                 
    
    if action == 'add flat':
            try:
                mod = pyautogui.locateOnScreen('img/trusses.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
                
                time.sleep(.500) 
                
                mod = pyautogui.locateOnScreen('img/flat.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
                
                mod = pyautogui.locateOnScreen('img/add.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick)

                time.sleep(.500) 
    
                mod = pyautogui.locateOnScreen('img/point1.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick)  

    
            except:
                pyautogui.alert('not found')   

# ANCHOR this this will try to filter and clear filters for batching icommand program
# ANCHOR really just a test to see how much the locate on screen can do 
    if action == 'filter':
        filtTo = pyautogui.prompt('filter to..')
        try:
            mod = pyautogui.locateOnScreen('img/heell.png') 
            toClick = pyautogui.center(mod)
            pyautogui.moveTo(toClick) 
            
            mod = pyautogui.locateOnScreen('img/filter.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick, button = 'right') 
            
            mod = pyautogui.locateOnScreen('img/filterdet.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick)

            time.sleep(1) 

            mod = pyautogui.locateOnScreen('img/value.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick)


            pyautogui.typewrite(filtTo)

            mod = pyautogui.locateOnScreen('img/ok.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick)

            mod = pyautogui.locateOnScreen('img/span.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick)
   
        except:
            try:
                mod = pyautogui.locateOnScreen('img/cmd2.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 

                mod = pyautogui.locateOnScreen('img/heall.png') 
                toClick = pyautogui.center(mod)
                pyautogui.moveTo(toClick) 
                
                mod = pyautogui.locateOnScreen('img/filter.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick, button = 'left') 
                
                mod = pyautogui.locateOnScreen('filterdet.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 

                mod = pyautogui.locateOnScreen('img/value.png') 
                toClick = pyautogui.center(mod)
                pyautogui.click(toClick) 
            except:
                pyautogui.alert('not found')
    if action == "clear":
        try:
            mod = pyautogui.locateOnScreen('img/clear.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick, button = 'right') 

            mod = pyautogui.locateOnScreen('img/clearfilter.png') 
            toClick = pyautogui.center(mod)
            pyautogui.click(toClick) 
        except:
         pyautogui.alert('not found')

# ANCHOR this is the end of icommand specific actions



# ANCHOR 'q' will kill the program
    if action == 'q':
        exit()

# ANCHOR f will open the file explorer
# TODO change this to open .EXE instead of locateOnScreen
# TODO add try except 

    if action == 'f':
        mod = pyautogui.locateOnScreen('img/file.png') 
        toClick = pyautogui.center(mod)
        pyautogui.click(toClick) 

# TODO add try except 
    if action == 'music':
        webbrowser.open('https://music.youtube.com/')
 # TODO add try except    
    if action == 'email':
        os.startfile("outlook")
# TODO add try except 
    if action == 'pdf':
        subprocess.Popen(r'explorer /select,"C:\Users\Itw User\Documents\PDF PRINT OUTS\Notion Junk"')

# TODO add try except 
    if action == 'web':
        subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
        
# TODO add try except     
    if action == 'notion':
        webbrowser.open('https://www.notion.so')

# TODO add try except 
    if action == 'youtube':
        webbrowser.open('https://www.youtube.com')
# TODO add try except 
    if action == 'reddit':
        webbrowser.open('https://www.reddit.com')
# TODO add try except 
    if action == 'steam':
        webbrowser.open('https://steamcommunity.com')

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()





   


