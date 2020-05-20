
import pyautogui

width, height = pyautogui.size()
print(width, height)

print("==== controlling mouse ====")
pyautogui.position()
#move at position x,y
pyautogui.moveTo(50, 50, duration = 1.5)
#move by relative to pixels
pyautogui.moveRel(200, 0, duration = 2)
#clicking position
pyautogui.click(200,50)
pyautogui.doubleClick(200,50)
pyautogui.rightClick(200,50)

#from cmd run beloww to get mouse position
#pyautogui.displyMousePosition()

print("==== controlling keyboard ====")
pyautogui.click(200, 200); pyautogui.typewrite("Hello World!", interval = 0.1)

pyautogui.click(200, 200); pyautogui.typewrite('a', 'b', 'left', 'left', 'x', 'y')

#all keyboard keys
pyautogui.KEYBOARD_KEYS

pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')

print("==== screenshots & image recognition ====")

pyuautogui.screenshot("exampl.png")
pyautogui.locateOnScreen()
pyautogui.locateCenterOnScreen()

