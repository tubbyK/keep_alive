import time
from pynput import keyboard

class keepAlive():
    def __init__(self, wait_time=60):
        self.keep_alive = False
        self.wait_time = wait_time

    def listen(self):
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # toggle keep alive state
            self.toggle_state()

    def toggle_state(self):
        self.keep_alive = not self.keep_alive
        if self.keep_alive:
            print('Keeping Windows from Locking')
        else:
            print('Letting Windows Lock')

    def do_action(self):
        keyboard.Controller().press(keyboard.Key.media_volume_mute)
        keyboard.Controller().press(keyboard.Key.media_volume_mute)
        time.sleep(self.wait_time)


if __name__ == '__main__':
    k = keepAlive()
    k.listen()
    k.toggle_state()

    while True:
        if k.keep_alive:
            k.do_action()
