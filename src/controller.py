import time
from inputs import get_gamepad
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
        self.button_states = {
            "left": False,
            "right": False,
            "a": False,
            "b": False,
            "L": False,
            "R": False
        }

    def press_buttons(self, button_states):
        for name, state in button_states.items():
            btn = self.button_map[name]
            if state != self.button_states[name]:
                if state:
                    self.gp.press_button(btn)
                else:
                    self.gp.release_button(btn)
                self.button_states[name] = state
        self.gp.update()

    def read(self):
        held = [k for k, v in self.button_states.items() if v]
        print("Held buttons:", held)
    
    def test_press_button(self, button):
        if button in self.button_map:
            self.gp.press_button(self.button_map[button])
            self.button_states[button] = True
            self.gp.update()
        else:
            print(f"Button {button} not recognized.")

    def test_release_button(self, button):
        if button in self.button_map:
            self.gp.release_button(self.button_map[button])
            self.button_states[button] = False
            self.gp.update()
    