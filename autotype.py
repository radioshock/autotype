from time import sleep
from pynput.keyboard import Key, Controller

def type(text):
    print(text)
    for x in text:
        sleep(.1)
        keyboard.type(x)

keyboard = Controller()
text = input()
sleep(3)
type(text)
