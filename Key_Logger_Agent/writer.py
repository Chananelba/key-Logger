from abc import ABC, abstractmethod


class Writer(ABC):
    def __init__(self):
         pass

    @abstractmethod
    def write(self,data):
        pass
