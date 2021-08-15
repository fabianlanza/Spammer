import pyautogui, time
from colored import fg, bg, attr

green = fg("green")
reset = attr("reset")

print(green + ''' 
 _   _                                     
| \ | |                                    
|  \| | ___  _ __ ___   ___ _ __ ___ _   _ 
| . ` |/ _ \| '_ ` _ \ / _ \ '__/ __| | | |
| |\  | (_) | | | | | |  __/ | | (__| |_| |
\_| \_/\___/|_| |_| |_|\___|_|  \___|\__, |
                                      __/ |
                                     |___/ '''+ reset)
print(green + "Created by: Fabian"+ reset)
print(green + "Close This Console to stop the spam"+ reset)
time.sleep(5)
f = open("Beemovie", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


  








            
