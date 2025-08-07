class Player:
    def __init__(self, action_function, controller):
        self.action_function = action_function
        self.controller = controller

        def action(self, screen):
            button_states = self.action_function(screen)
            self.controller.set_buttons(button_states)