import time
import vgamepad as vg
class Player:
    def __init__(self, action_function, controller):
        self.action_function = action_function
        self.controller = controller

    def action(self, screen):
        button_states = self.action_function(screen)
        self.controller.press_buttons(button_states)
    
    def character_select(self):
        """
        Get character choice from contribution and navigate to it
        """
        character_choice = self.action_function.character_select()
        # TODO: Navigate to character based on starting position and choice
        return character_choice
        
    def from_main_menu_to_character_select(self):
        time.sleep(1)
        self.controller.press_buttons({"up": True})
        time.sleep(0.5)
        self.controller.press_buttons({"up": False})
        time.sleep(0.5)
        self.controller.press_buttons({"up": True})
        time.sleep(0.5)
        self.controller.press_buttons({"up": False})
        time.sleep(0.5)
        self.controller.press_buttons({"up": True})
        time.sleep(0.5)
        self.controller.press_buttons({"up": False})
        time.sleep(0.5)
        self.controller.press_buttons({"up": True})
        time.sleep(0.5)
        self.controller.press_buttons({"up": False})
        time.sleep(0.5)
        self.controller.press_buttons({"down": True})
        time.sleep(0.5)
        self.controller.press_buttons({"down": False})
        time.sleep(0.5)
        self.controller.press_buttons({"a": True})
        time.sleep(0.5)
        self.controller.press_buttons({"a": False})
        time.sleep(0.5)
        self.controller.press_buttons({"a": True})
        time.sleep(0.5)
        self.controller.press_buttons({"a": False})
        time.sleep(0.5)
        self.controller.press_buttons({"a": True})
        time.sleep(0.5)
        self.controller.press_buttons({"a": False})
        time.sleep(0.5)
        
    
    def from_unknown_screen_to_main_menu(self):
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 
        time.sleep(0.05)
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 