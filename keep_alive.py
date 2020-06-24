import pyautogui
import time
import threading as th
import keyboard

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
        th.Thread(target=self.key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
        while self.keep_going:
            print('still running...')
            self.jitter()
            time.sleep(self.wait_time)

    def key_capture_thread(self, key='esc'):
        a = keyboard.read_key()
        print(a)
        if key in a:
            self.keep_going = False

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
        self.x_pos, self.y_pos = pyautogui.position()
        self.max_pos()
        pyautogui.click(button='right')
        pyautogui.moveTo(self.x_pos - 40, self.y_pos - 40)
        pyautogui.click()
        time.sleep(self.wait_time)
        self.x_pos += self.move
        self.y_pos += self.move
        self.max_pos()
        pyautogui.moveTo(self.x_pos, self.y_pos)
        pyautogui.click(button='right')
        pyautogui.moveTo(self.x_pos - 40, self.y_pos - 40)
        pyautogui.click()

if __name__ == '__main__':
    k = keep_alive()
    k.run()