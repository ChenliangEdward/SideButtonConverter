# reference: https://stackoverflow.com/questions/65382769/how-to-detect-what-button-was-clicked-pynput


from pynput import mouse
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

counter = 0


def on_click(x, y, button, pressed):
    # print(button)  # Print button to see which button of mouse was pressed
    global counter
    if button is mouse.Button.x1 and pressed:
        counter += 1
        if counter % 2 != 0:
            keyboard.press(Key.ctrl)
            print("ctrl pressed")
        else:
            keyboard.release(Key.ctrl)
            print("ctrl released")
    if button is mouse.Button.x2 and pressed:
        counter += 1
        if counter % 2 != 0:
            keyboard.press(Key.shift)
            print("shift pressed")
        else:
            keyboard.release(Key.shift)
            print("shift released")


# Collect events until released
print(">> converter started")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
