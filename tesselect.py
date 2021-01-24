import pyperclip
import pytesseract
from PIL import ImageGrab, ImageOps
from pynput import keyboard, mouse

top_left = bot_right = (0, 0)  # Set top_left and bot_right to (0, 0)


def on_click(x, y, button, pressed):
    if pressed:
        global top_left
        top_left = (x, y)
    else:
        global bot_right
        bot_right = (x, y)

    return pressed  # Stop the listener when pressed is False


# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

img = ImageGrab.grab(bbox=(top_left[0], top_left[0], bot_right[0], bot_right[0]))
img = ImageOps.grayscale(img)

pyperclip.copy(pytesseract.image_to_string(img).strip())
