import json
from writer import Writer


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