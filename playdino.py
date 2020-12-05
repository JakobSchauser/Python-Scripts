from pynput.keyboard import Key,Controller
import PIL
import time
keyboard = Controller()



st = "Fredes mor"

n = 10
t = 0.5
    

keyboard.type(st)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(t)
