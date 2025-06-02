import json

class FileHandler:
    def __init__(self, lista_produktow_file, hist_operacji_file, saldo_file):
        self.lista_produktow_file = lista_produktow_file
        self.hist_operacji_file = hist_operacji_file
        self.saldo_file = saldo_file
        self.lista_produktow = self.load_lista_produktow_file()
        self.hist_operacji = self.load_hist_operacji_file()
        self.saldo = self.load_saldo_file()

    def load_lista_produktow_file(self):
        with open(self.lista_produktow_file) as file:
            lista_produktow = json.load(file)
            return lista_produktow

    def load_hist_operacji_file(self):
        with open(self.hist_operacji_file) as file:
            hist_operacji = json.load(file)
        return hist_operacji

    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = json.load(file)
            return float(saldo)

    def save_lista_produktow_file(self):
        with open(self.lista_produktow_file, "w") as file:
            file.write(json.dumps(self.lista_produktow, indent=4))  #indent=4 format zapisu w json z 4 spacjami bardziej czytelny

    def save_hist_operacji_file(self):
        with open(self.hist_operacji_file, "w") as file:
            file.write(json.dumps(self.hist_operacji, indent=4))

    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(json.dumps(self.saldo, indent=4))

file_handler = FileHandler("lista_produktow.json", "hist_operacji.json", "saldo.txt")