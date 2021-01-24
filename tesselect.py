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

    return pressed  # Stop mouse_listener when pressed is False


def tesselect():
    # Collect events until released
    with mouse.Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()

    if top_left < bot_right:  # Compare x and y of top_left and bot_right
        img = ImageOps.grayscale(ImageGrab.grab(bbox=(*top_left, *bot_right)))
        pyperclip.copy(pytesseract.image_to_string(img).strip())


with keyboard.GlobalHotKeys({"<ctrl>+<alt>+t": tesselect}) as keyboard_listener:
    keyboard_listener.join()