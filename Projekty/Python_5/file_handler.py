import json


class FileHandler:
    def __init__(self, magazyn_file, saldo_file, historia_file):
        self.magazyn_file = magazyn_file
        self.saldo_file = saldo_file
        self.historia_file = historia_file
        self.magazyn = self.load_magazyn_file()
        self.historia = self.load_history_file()
        self.saldo = self.load_saldo_file()

    def load_magazyn_file(self):
        with open(self.magazyn_file) as file:
            magazyn = json.load(file)
            return magazyn

    def load_history_file(self):
        with open(self.historia_file) as file:
            historia = json.load(file)
            # return historia
        return historia

    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = file.read().strip()
            return float(saldo)

    def save_magazyn_file(self):
        with open(self.magazyn_file, "w") as file:
            file.write(json.dumps(self.magazyn, indent=6))

    def save_historia_file(self):
        with open(self.historia_file, "w") as file:
            file.write(json.dumps(self.historia, indent=4))

    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(str(self.saldo))


file_handler = FileHandler("magazyn.json", "saldo.txt", "historia.json")


def save_temporary_data(file_handler, magazyn, saldo, historia):
    file_handler.magazyn = magazyn
    file_handler.saldo = saldo
    file_handler.historia = historia
    file_handler.save_magazyn_file()
    file_handler.save_saldo_file()
    file_handler.save_historia_file()