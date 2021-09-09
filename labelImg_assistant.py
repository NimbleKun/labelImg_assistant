from pywinauto.keyboard import send_keys
import threading
import time
import pynput
from pynput import mouse
from pynput.mouse import Button, Controller


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False


def action(*add):
    print("开始")
    while True:
        try:
            with mouse.Listener(
                    on_click=on_click) as listener:
                listener.join()
                print("click done")
                time.sleep(0.2)
                time.sleep(0.3)
                # 点击下一张
                mouse2 = Controller()
                before_pos_x, before_pos_y = mouse2.position
                mouse2.position = (81, 266)
                mouse2.click(pynput.mouse.Button.left)
                mouse2.position = (before_pos_x, before_pos_y)
                # 画框
                send_keys('w')

        except Exception as e:
            print(e)


debug = False
if debug == False:
    thread = threading.Thread(target=action)
    thread.start()
else:
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()