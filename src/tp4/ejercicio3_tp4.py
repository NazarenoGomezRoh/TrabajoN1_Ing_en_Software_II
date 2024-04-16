from abc import ABC, abstractmethod

# Componente base: Pieza
class Pieza(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Hoja: representa una pieza individual
class PiezaSimple(Pieza):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Pieza simple: {self.nombre}")

# Composite: representa un conjunto de piezas
class ConjuntoPiezas(Pieza):
    def __init__(self, nombre):
        self.nombre = nombre
        self.piezas = []

    def agregar_pieza(self, pieza):
        self.piezas.append(pieza)

    def mostrar(self):
        print(f"Conjunto de piezas: {self.nombre}")
        for pieza in self.piezas:
            pieza.mostrar()

# Crear las piezas individuales
pieza1 = PiezaSimple("Pieza 1")
pieza2 = PiezaSimple("Pieza 2")
pieza3 = PiezaSimple("Pieza 3")
pieza4 = PiezaSimple("Pieza 4")

# Crear los conjuntos de piezas
subconjunto1 = ConjuntoPiezas("Subconjunto 1")
subconjunto1.agregar_pieza(pieza1)
subconjunto1.agregar_pieza(pieza2)
subconjunto1.agregar_pieza(pieza3)
subconjunto1.agregar_pieza(pieza4)

subconjunto2 = ConjuntoPiezas("Subconjunto 2")
subconjunto2.agregar_pieza(pieza1)
subconjunto2.agregar_pieza(pieza2)
subconjunto2.agregar_pieza(pieza3)
subconjunto2.agregar_pieza(pieza4)

subconjunto3 = ConjuntoPiezas("Subconjunto 3")
subconjunto3.agregar_pieza(pieza1)
subconjunto3.agregar_pieza(pieza2)
subconjunto3.agregar_pieza(pieza3)
subconjunto3.agregar_pieza(pieza4)

# Mostrar la estructura del ensamblado
ensamblado_principal = ConjuntoPiezas("Producto principal")
ensamblado_principal.agregar_pieza(subconjunto1)
ensamblado_principal.agregar_pieza(subconjunto2)
ensamblado_principal.agregar_pieza(subconjunto3)
ensamblado_principal.mostrar()
