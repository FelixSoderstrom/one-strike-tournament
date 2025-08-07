import sys
import asyncio
from time import sleep

from src.controller import Controller
from src.screen_capturer import WindowCapture

class GameLoop:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.controller = Controller()
        self.screen_capturer = WindowCapture(title="One Strike")
        self.game_over_detector = self.screen_capturer.detect_game_over

        self.running = False
        self.game_over = False



    def idle_loop(self):
        while True:
            self.game_over = self.game_over_detector()

            if self.game_over:
                print("Game over detected!")

            self.screen = self.screen_capturer.grab()
            sleep(1)

            if self.running:
                asyncio.run(self._active_loop())

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


            
