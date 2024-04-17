from abc import ABC, abstractmethod

# Interfaz para la creación de comida rápida
class ComidaRapida(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Clase base para hamburguesas
class Hamburguesa(ComidaRapida):
    def entregar(self):
        print("Hamburguesa lista para ser entregada")

# Clase que maneja la entrega en mostrador
class Mostrador(ComidaRapida):
    def entregar(self):
        print("Hamburguesa lista para ser retirada en mostrador")

# Clase que maneja la entrega por delivery
class Delivery(ComidaRapida):
    def entregar(self):
        print("Hamburguesa lista para ser enviada por delivery")

# Factory Method para crear instancias de comida rápida
class ComidaFactory:
    def obtener_comida(self, tipo):
        if tipo == "hamburguesa":
            return Hamburguesa()
        elif tipo == "mostrador":
            return Mostrador()
        elif tipo == "delivery":
            return Delivery()
        else:
            return None

# Ejemplo de uso
if __name__ == "__main__":
    factory = ComidaFactory()

    # Pedido de hamburguesa para mostrador
    comida_mostrador = factory.obtener_comida("mostrador")
    comida_mostrador.entregar()

    # Pedido de hamburguesa para delivery
    comida_delivery = factory.obtener_comida("delivery")
    comida_delivery.entregar()

    # Pedido de hamburguesa sin especificar método de entrega
    hamburguesa = factory.obtener_comida("hamburguesa")
    hamburguesa.entregar()
