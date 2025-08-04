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
        self.screen_capturer = WindowCapture(title="Discord")

        self.running = False
        self.game_over = False



    def idle_loop(self):
        while True:
            if self.game_over:
                print("Game state is over. Exiting...")
                sys.exit()

            self.screen = self.screen_capturer.grab()
            print(self.screen)
            print("One screen was put through")
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


            
