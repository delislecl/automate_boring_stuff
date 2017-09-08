import pyautogui

#Screen size
pyautogui.size()

#Mouse position
pyautogui.position()

#Move mouse
pyautogui.moveTo(10,10)

#Move mouse
pyautogui.moveTo(10,10, duration=1.5)

#More relative
pyautogui.moveRel(200,0, duration =1.5)

#Click
pyautogui.click(275,34)
pyautogui.rightClick(275,34)

#See coordinates in real time (run in Ipython)
pyautogui.displayMousePosition()

#test

#Write text (interval time between caracters)
pyautogui.click(137,159)
pyautogui.typewrite("Hello world!", interval=0.2)
pyautogui.typewrite(['a','b','c'], interval=0.2)
pyautogui.hotkey('ctrl','o')

#Screenshots
pyautogui.screenshot("screenshot_example.png")
pyautogui.locateOnScreen("calc.png")
pyautogui.locateCenterOnScreen("calc.png")
pyautogui.moveTo(1105,433)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("calc.png"))