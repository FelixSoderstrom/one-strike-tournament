import time
from PIL import Image
import numpy as numpy
import vgamepad as vg


class Controller:
    def __init__(self, gamepad_id=1):
        self.gp = vg.VX360Gamepad()
        self.id = gamepad_id
        
        self.button_map =  {
                "left": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
                "right": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
                "a": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
                "b": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
                "L": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                "R": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
                }                


    def press_buttons(self, button_states):
        for name, state in button_states.items():
            btn = self.button_map[name]
            if state:
                self.gp.press_button(btn)
            else:
                self.gp.press_button(btn)
        self.gp.update()


