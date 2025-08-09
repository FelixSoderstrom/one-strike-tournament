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
        while self.current_state == None:
            self._detect_game_state()
            sleep(1)
        self.navigate_menu()


    def navigate_menu(self):
        while not self.running:
            if self.current_state == "main_menu":
                self.p1.from_main_menu_to_character_select()
                self.current_state = "character_select"
            elif self.current_state == "character_select":
                self.p1.navigate_to_character(controller = self.p1.controller, player_position=1)
                self.p2.navigate_to_character(controller = self.p2.controller, player_position=2)


        
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


            
