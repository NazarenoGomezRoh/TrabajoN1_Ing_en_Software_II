import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.memories = {"M1": "1300", "M2": "1420", "M3": "1480", "M4": "1550"}  # Memorizadas para AM
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan(self):
        super().scan()
        self.scan_memories()

    def scan_memories(self):
        print("Memorias de AM:")
        for label, frequency in self.memories.items():
            print(f"Sintonizando... Memoria {label}: {frequency}")

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.memories = {"M1": "87.5", "M2": "92.3", "M3": "99.7", "M4": "105.5"}  # Memorizadas para FM
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan(self):
        super().scan()
        self.scan_memories()

    def scan_memories(self):
        print("Memorias de FM:")
        for label, frequency in self.memories.items():
            print(f"Sintonizando... Memoria {label}: {frequency}")

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate  # Inicialmente en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2  # Repetir dos veces

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
