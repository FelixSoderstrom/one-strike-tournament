
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
