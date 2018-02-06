import pyautogui
from time import sleep
import webbrowser

def launch_files():
	#pyautogui.moveTo(36,112, duration=2)
	pyautogui.click(35,112,button='left')

def get_pos_color():
	x,y=pyautogui.position()
	(r,g,b)=pyautogui.screenshot().getpixel((x,y))
	coord="("+str(x).rjust(5)+str(y).rjust(5)+")"+"rgb:("+str(r).rjust(3)+","+str(g).rjust(3)+","+str(b).rjust(3)+")"
	return coord


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform")
sleep(5)

(x,y,w,h)=pyautogui.locateOnScreen("form_fill.png")
x,y=pyautogui.center((x,y,w,h))
pyautogui.click(x,y+160,button="left");pyautogui.typewrite('monty',0.25)
pyautogui.moveRel(0,70,duration=0.5);pyautogui.click();pyautogui.typewrite('no worries',0.25)
pyautogui.moveRel(0,65,duration=0.5);pyautogui.click();pyautogui.moveRel(0,25,duration=0.5);pyautogui.click();
pyautogui.moveRel(20,70,duration=0.5);pyautogui.click();
pyautogui.moveRel(0,78,duration=0.5);pyautogui.click();pyautogui.typewrite('blah blah',0.25)
sleep(1);pyautogui.scroll(-3);pyautogui.moveRel(-65,0,duration=0.5);pyautogui.click();



