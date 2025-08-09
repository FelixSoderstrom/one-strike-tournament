
import platform
import subprocess
import mss
from PIL import Image
import numpy as np

class WindowCapture():
    def __init__(self, title):
        self.title = title
        self.sct = mss.mss()

        system = platform.system()
        if system == "Windows":
            import pygetwindow as gw
            win = gw.getWindowsWithTitle(title)
            if not win:
                raise Exception(f"Window with title '{title}' not found")
            win = win[0]
            self.bbox = {"top": win.top, "left": win.left, "width": win.width, "height": win.height}

        elif system == "Linux":
            self.bbox = self.get_window_bbox_linux(title)

        else:
            raise NotImplementedError(f"Unsupported OS: {system}")
    
    def detect_red_pixel(self, img, x, y, threshold=250):
        """
        Detects if there is a red pixel in the image.
        Returns True if a red pixel is found, otherwise False.
        """
        pixel_rgb = img[y, x]  # For pixel at (x, y)
        r, g, b = [int(v) for v in pixel_rgb]
        if abs(r - 255) + abs(g - 0) + abs(b - 0) < threshold:
            return True
    
    def detect_purple_pixel(self, img, x, y, threshold=20):
        pixel_rgb = img[y, x]  # For pixel at (x, y)
        r, g, b = [int(v) for v in pixel_rgb]
        if abs(r - 95) + abs(g - 0) + abs(b - 122) < threshold:
            return True
    def detect_yellow_pixel(self, img, x, y, threshold=20):
        pixel_rgb = img[y, x]  # For pixel at (x, y)
        r, g, b = [int(v) for v in pixel_rgb]
        if abs(r - 228) + abs(g - 255) + abs(b - 0) < threshold:
            return True
    
    def detect_white_pixel(self, img, x, y, threshold=20):
        pixel_rgb = img[y, x]  # For pixel at (x, y)
        r, g, b = [int(v) for v in pixel_rgb]
        if abs(r - 255) + abs(g - 255) + abs(b - 255) < threshold:
            return True
        else:
            return False
    
    def detect_orange_pixel(self, img, x, y, threshold=20):
        pixel_rgb = img[y, x]  # For pixel at (x, y)
        r, g, b = [int(v) for v in pixel_rgb]
        if abs(r - 255) + abs(g - 102) + abs(b - 0) < threshold:
            return True
        else:
            return False
        
    def detect_character_select(self):
        img = self.grab()
        if self.detect_white_pixel(img, 1020, 240): #Shirt on the longsword guy
            if self.detect_red_pixel(img, 1080, 330): #Red hat
                if self.detect_orange_pixel(img, 1100, 859): #Question mark
                    print("Character select detected!")
                    return True
        return False
    
    def detect_main_menu(self):
        white_pixels= [[650, 10], [980, 10], [1300,10]]
        img = self.grab()
        for pixel in white_pixels:
            if not self.detect_white_pixel(img, pixel[0], pixel[1]):
                return False
        print("Main menu detected!")
        return True

    def detect_game_over(self):
        yellow_pixels = [[540, 190], [1040, 470], [1570,700]]
        purple_pixels = [[600, 175], [970, 520], [1540,730]]
        img = self.grab()
        for pixel in yellow_pixels:
            if not self.detect_yellow_pixel(img, pixel[0], pixel[1]):
                return False
            print("All yellow pixels detected!")
            for pixel in purple_pixels:
                if not self.detect_purple_pixel(img, pixel[0], pixel[1]):
                    return False
        print("Round over!")
        return True

    def detect_round_over(self):
        pixels_of_interest = [[530, 400], [1380, 270], [970,370]]
        img = self.grab()
        for pixel in pixels_of_interest:
            if not self.detect_red_pixel(img, pixel[0], pixel[1]):
                return False
        print("Game Over detected at all pixels")
        return True

    def get_window_bbox_linux(self, title):
        # get window ids matching title
        out = subprocess.check_output(f"xdotool search --name '{title}'", shell=True).decode().strip()
        win_ids = out.split('\n')
        if not win_ids or win_ids == ['']:
            raise Exception(f"Window with title '{title}' not found")

        win_id = win_ids[0]


        geom_out = subprocess.check_output(f"xdotool getwindowgeometry {win_id}", shell=True).decode()
        lines = geom_out.strip().split('\n')

        pos_line = lines[1]  # e.g. "Position: 10,20 (screen: 0)"
        pos_str = pos_line.split("Position: ")[1].split(" ")[0]  # "10,20"
        pos = pos_str.split(",")

        size_str = lines[2].split()[-1]  # e.g. "800x600"
        size = size_str.split("x")

        x, y = int(pos[0]), int(pos[1])
        w, h = int(size[0]), int(size[1])
        return {"top": y, "left": x, "width": w, "height": h}

    def grab(self):
        shot = self.sct.grab(self.bbox)
        img = Image.frombytes("RGB", shot.size, shot.rgb)
        return np.array(img)
