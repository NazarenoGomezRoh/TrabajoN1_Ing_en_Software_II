from functools import wraps

# Clase base que permite imprimir, sumar, multiplicar y dividir un número
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print("Valor actual:", self.valor)

    def agregar(self, valor):
        self.valor += valor

# Decorador para sumarle 2 al número
def sumar_dos(func):
    @wraps(func)
    def wrapper(self):
        self.agregar(2)
        func(self)
    return wrapper

# Decorador para multiplicar por 2 el número
def multiplicar_por_dos(func):
    @wraps(func)
    def wrapper(self):
        self.valor *= 2
        func(self)
    return wrapper

# Decorador para dividir por 3 el número
def dividir_por_tres(func):
    @wraps(func)
    def wrapper(self):
        self.valor /= 3
        func(self)
    return wrapper

# Uso del patrón decorator
if __name__ == "__main__":
    numero = Numero(5)

    # Mostrar el número sin agregados
    numero.imprimir()

    # Mostrar el número con los decoradores aplicados
    print("\nAplicando sumar_dos:")
    @sumar_dos
    def mostrar_suma():
        numero.imprimir()

    mostrar_suma()

    print("\nAplicando multiplicar_por_dos:")
    @multiplicar_por_dos
    def mostrar_multiplicacion():
        numero.imprimir()

    mostrar_multiplicacion()

    print("\nAplicando dividir_por_tres:")
    @dividir_por_tres
    def mostrar_division():
        numero.imprimir()

    mostrar_division()
