class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._factorial_cache = {}
        return cls._instance

    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("El factorial solo está definido para números enteros no negativos.")
        if n in self._factorial_cache:
            return self._factorial_cache[n]
        if n == 0:
            result = 1
        else:
            result = n * self.calculate_factorial(n - 1)
        self._factorial_cache[n] = result
        return result

# Ejemplo de uso
factorial_calculator = FactorialCalculator()
print(factorial_calculator.calculate_factorial(5))  # Salida: 120
print(factorial_calculator.calculate_factorial(3))  # Salida: 6
