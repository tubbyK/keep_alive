import pyautogui
import time
from pynput import keyboard

class keep_alive():

    def __init__(self, move=100, size_factor=0.8, wait_time=30):
        self.x_pos, self.y_pos = None, None
        self.get_mouse_pos()
        self.move = move
        self.width, self.height = None, None
        self.get_screen_size()
        self.size_factor = size_factor
        self.wait_time = wait_time
        self.keep_going = True

    def run(self):
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()
        while True:
            if self.keep_going:
                self.jitter()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            self.keep_going = False if self.keep_going else True
            print(f'Toggle: {self.keep_going}')

    def get_mouse_pos(self):
        self.x_pos, self.y_pos = pyautogui.position()

    def get_screen_size(self):
        self.width, self.height = pyautogui.size()

    def max_pos(self):
        max_x = int(self.width * self.size_factor)
        max_y = int(self.height * self.size_factor)
        if self.x_pos > max_x:
            self.x_pos = max_x
        if self.y_pos > max_y:
            self.y_pos = max_y

    def jitter(self):
        x_pos_original, y_pos_original = pyautogui.position()
        self.x_pos, self.y_pos = pyautogui.position()
        self.max_pos()
        pyautogui.click(button='right')
        pyautogui.moveTo(self.x_pos - 40, self.y_pos - 40)
        pyautogui.click()
        pyautogui.moveTo(x_pos_original, y_pos_original)
        time.sleep(self.wait_time)

if __name__ == '__main__':
    k = keep_alive()
    k.run()