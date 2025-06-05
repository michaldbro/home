import csv

class FileHandler:
    def __init__(self, input_file1, output_file1, transform1):
        self.input_file = input_file1
        self.output_file = output_file1
        self.ldata = self.load()
        self.transform = transform1
        self.new = self.do_transform()

    def load(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            temp = []
            for row in reader:
                temp_row = []
                for dane in row:
                    temp_row.append(dane)
                temp.append(temp_row)
        return temp

    def save(self):
        with open(self.output_file, 'w+', newline='') as file:
            writer = csv.writer(file)
            for row in self.new: #self.ldata:
                writer.writerow(row)

    def do_transform(self):
        lista_list = []
        for czesc_listy in self.transform:
            lista_list.append(czesc_listy.split(','))
        #lista_list = [czesc_listy.split(',') for czesc_listy in self.transform]
        return lista_list
