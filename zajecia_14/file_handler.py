import json

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_file()

    def read_file(self):
        with open(self.file) as file:
            return json.load(file)

    def write_file(self, new_data):
        self.data.append(new_data)
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data, indent=4))

    def search_in_file(self, opad, city):
        for opad_mm in self.data:
            if opad_mm.get("rain") == opad and opad_mm.get("city") == city:
               return opad_mm