# Interfaz para definir el comportamiento de las clases que manejan números
class Handler:
    def handle_request(self, number):
        pass

# Clase base para implementar las cadenas de responsabilidad
class BaseHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def pass_to_next(self, number):
        if self.next_handler:
            self.next_handler.handle_request(number)
        else:
            print(f"Número no consumido: {number}")

# Clase que maneja números primos
class PrimeHandler(BaseHandler):
    def handle_request(self, number):
        if self.is_prime(number):
            print(f"Número primo consumido: {number}")
        else:
            self.pass_to_next(number)

    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Clase que maneja números pares
class EvenHandler(BaseHandler):
    def handle_request(self, number):
        if number % 2 == 0:
            print(f"Número par consumido: {number}")
        else:
            self.pass_to_next(number)

# Clase principal para probar el patrón
if __name__ == "__main__":
    # Crear instancias de los manejadores
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    # Configurar la cadena de responsabilidad
    prime_handler.set_next_handler(even_handler)

    # Probar con números del 1 al 100
    for i in range(1, 101):
        prime_handler.handle_request(i)
