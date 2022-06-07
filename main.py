# reference: https://stackoverflow.com/questions/65382769/how-to-detect-what-button-was-clicked-pynput
import winsound

from pynput import mouse
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

counter_shift = 0
counter_ctrl = 0
frequency_press = 2000  # Set Frequency To 2500 Hertz
frequency_release = 1500  # Set Frequency To 1500 Hertz
duration = 180  # Set Duration To 200 ms == 1 second


def on_click(x, y, button, pressed):
    # print(button)  # Print button to see which button of mouse was pressed
    global counter_ctrl
    if button is mouse.Button.x1 and pressed:
        counter_ctrl += 1
        if counter_ctrl % 2 != 0:
            keyboard.press(Key.ctrl)
            winsound.Beep(frequency_press, duration)
            print("ctrl pressed")
        else:
            keyboard.release(Key.ctrl)
            winsound.Beep(frequency_release, duration)

            print("ctrl released")
    global counter_shift
    if button is mouse.Button.x2 and pressed:
        counter_shift += 1
        if counter_shift % 2 != 0:
            keyboard.press(Key.shift)
            winsound.Beep(frequency_press, duration)
            print("shift pressed")

        else:
            keyboard.release(Key.shift)
            winsound.Beep(frequency_release, duration)

            print("shift released")


# Collect events until released
print(">> converter started")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
