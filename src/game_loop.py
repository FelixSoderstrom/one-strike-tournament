import sys
import asyncio
import time
from time import sleep

from src.screen_capturer import WindowCapture

class GameLoop:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.screen_capturer = WindowCapture(title="One Strike")
        self.game_over_detector = self.screen_capturer.detect_game_over

        self.running = False
        self.game_over = False
        self.current_state = None 

    def _detect_game_state(self):
        if self.screen_capturer.detect_main_menu():
            self.current_state = "main_menu"
        elif self.screen_capturer.detect_character_select():
            self.current_state = "character_select"
        elif self.screen_capturer.detect_game_over():
            self.current_state = "game_over"

    def idle_loop(self):
        print("idle loop")
        while self.current_state == None:
            print("idle loooooop")
            self._detect_game_state()
            sleep(1)
        self.navigate_menu()


    def navigate_menu(self):
        if self.current_state == "main_menu":
            self.p1.from_main_menu_to_character_select()
        elif self.current_state == "character_select":
            self.p1.from_character_select_to_game()
        elif self.current_state == "game_over":
            self.p1.from_game_over_to_main_menu()


        
    async def _active_loop(self):
        await asyncio.gather(
            self._refresh_screen(),
            self._take_input()
        )

    
    async def _refresh_screen(self):
        while True:
            self.screen = self.screen_capturer.grab()
            self.analyze_screen()
            if self.game_over:
                print("Game state is over. Exiting...")
                break
            await asyncio.sleep(0.1)

    
    async def _take_input(self):
        while True:
            self.p1.action(self.screen)
            self.p2.action(self.screen)
            await asyncio.sleep(0.1)


            

class CharacterSelector:
    @staticmethod
    def navigate_to_character(self, target_character, controller, player_position):
        moves = CharacterSelector._get_character_navigation(target_character, player_position)
        for move in moves:
            controller.press_button(move)
            time.sleep(0.05)
            controller.release_button(move)
            time.sleep(0.05)

        controller.press_button("a")


    @staticmethod
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
        
        starting_positions = {
            "p1": (0, 0),
            "p2": (1, 0),
        }

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