import time
import vgamepad as vg
class Player:
    def __init__(self, bot_data, controller):
        self.action_function = bot_data["action"]
        self.character_select = bot_data["character"]
        self.controller = controller

    def action(self, screen):
        button_states = self.action_function(screen)
        self.controller.press_buttons(button_states)
    
    def character_select(self):
        pass
        
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


    def navigate_to_character(self, controller, player_position):
        target_character = self.character_select()
        moves = self._get_character_navigation(target_character, player_position)
        for move in moves:
            controller.press_buttons({move : True})
            time.sleep(0.05)
            controller.release_buttons({move :False})
            time.sleep(0.05)

        controller.press_button("a")

    def _get_character_navigation(self, target_character, player_position):
        character_positions = {
            "Kenji": (0, 0),
            "Tomoe": (0, 1),
            "Bailong": (0, 2),
            "Oni": (0, 3),
            "Soujirou": (1, 0), 
            "Hangaku": (1, 1),
            "Hinode": (1, 2)
        }
        
        starting_positions = [ 
            (0, 0),
            (1, 0),
        ]

        start_pos = starting_positions[player_position]
        target_pos = character_positions[target_character]

        row_diff = target_pos[0] - start_pos[0]
        col_diff = target_pos[1] - start_pos[1]

        moves = []
        if row_diff > 0:
            moves.extend(["down"] * row_diff)
        if col_diff > 0:
            moves.extend(["right"] * col_diff)
        elif col_diff < 0:
            moves.extend(["left"] * abs(col_diff))

        return moves