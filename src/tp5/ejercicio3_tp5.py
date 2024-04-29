# Clase observable
class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, event_id):
        for observer in self.observers:
            observer.update(event_id)

# Clase observadora
class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, event_id):
        if event_id == self.observer_id:
            print(f"¡El ID {event_id} coincide con el ID de esta clase {self.observer_id}!")

# Clases con ID específicos
class ClassA(Observer):
    def __init__(self):
        super().__init__("ABCD")

class ClassB(Observer):
    def __init__(self):
        super().__init__("EFGH")

class ClassC(Observer):
    def __init__(self):
        super().__init__("WXYZ")

class ClassD(Observer):
    def __init__(self):
        super().__init__("QRST")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear observable
    observable = Observable()

    # Crear instancias de clases observadoras
    class_a = ClassA()
    class_b = ClassB()
    class_c = ClassC()
    class_d = ClassD()

    # Suscribir clases observadoras al observable
    observable.add_observer(class_a)
    observable.add_observer(class_b)
    observable.add_observer(class_c)
    observable.add_observer(class_d)

    # Emitir 8 IDs, asegurándose de que al menos cuatro coincidan con los IDs de las clases implementadas
    ids = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST", "UVWX", "YZAB", "WXYZ"]
    for event_id in ids:
        observable.notify_observers(event_id)
