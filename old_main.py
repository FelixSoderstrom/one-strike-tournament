import random 
import time
from PIL import Image
import numpy as np
import vgamepad as vg 
img = Image.open("/home/jayb/projects/onestrike/image.png")


gp1 = vg.VX360Gamepad()
gp2 = vg.VX360Gamepad()




matrix = np.array(img)
port = 1

def controller(matrix, port):
    gp1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gp1.update()
    return True 
    
while True:
    # press A on both
    gp1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gp2.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gp1.update()
    gp2.update()

    time.sleep(0.2) # release A on both
    gp1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gp2.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

    gp1.update()
    gp2.update()

    time.sleep(0.2)

    gp1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gp2.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    gp1.update()
    gp2.update()

    time.sleep(0.2)

    # release A on both
    gp1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gp2.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

    gp1.update()
    gp2.update()

    time.sleep(0.2)

    gp1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    gp2.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    gp1.update()
    gp2.update()

    time.sleep(0.2)

    # release A on both
    gp1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    gp2.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

    gp1.update()
    gp2.update()

    time.sleep(0.2)
