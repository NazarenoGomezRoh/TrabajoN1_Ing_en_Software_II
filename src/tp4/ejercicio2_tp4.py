from abc import ABC, abstractmethod

# Abstracción
class Lamina:
    def __init__(self, tren_laminador):
        self._tren_laminador = tren_laminador

    @abstractmethod
    def producir_lamina(self):
        pass

# Implementaciones de las láminas
class Lamina05(Lamina):
    def producir_lamina(self):
        print("Produciendo lámina de 0.5\" de espesor y 1.5 metros de ancho.")
        self._tren_laminador.producir_lamina()

class Lamina15(Lamina):
    def producir_lamina(self):
        print("Produciendo lámina de 0.5\" de espesor y 1.5 metros de ancho.")
        self._tren_laminador.producir_lamina()

# Implementaciones de los trenes laminadores
class TrenLaminador(ABC):
    @abstractmethod
    def producir_lamina(self):
        pass

class TrenLaminador5(TrenLaminador):
    def producir_lamina(self):
        print("Produciendo lámina de 5 metros.")

class TrenLaminador10(TrenLaminador):
    def producir_lamina(self):
        print("Produciendo lámina de 10 metros.")

# Uso del patrón Bridge
if __name__ == "__main__":
    # Seleccionar el tipo de lámina y tren laminador
    lamina = Lamina15(TrenLaminador5())  # Por ejemplo, lámina de 1.5 metros con tren laminador de 5 metros
    lamina.producir_lamina()
