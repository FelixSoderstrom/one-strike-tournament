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
        