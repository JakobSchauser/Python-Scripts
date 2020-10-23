from pynput.keyboard import Key,Controller
import time
keyboard = Controller()



st = "Fredes mor"
n = 10
t = 0.5
    

for i in range(n):
    keyboard.type(st)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(t)
