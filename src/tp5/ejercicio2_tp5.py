# Clase que implementa el iterador
class CharIterator:
    def __init__(self, string, reverse=False):
        self.string = string
        self.reverse = reverse
        self.index = len(string) - 1 if reverse else 0
        self.step = -1 if reverse else 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverse:
            if self.index < 0:
                raise StopIteration
            char = self.string[self.index]
            self.index += self.step
            return char
        else:
            if self.index >= len(self.string):
                raise StopIteration
            char = self.string[self.index]
            self.index += self.step
            return char

# Clase que almacena una cadena de caracteres y proporciona los iteradores
class CharContainer:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CharIterator(self.string)

    def reverse_iterator(self):
        return CharIterator(self.string, reverse=True)

# Ejemplo de uso
if __name__ == "__main__":
    string = "Python"
    container = CharContainer(string)

    print("Recorriendo en sentido directo:")
    for char in container:
        print(char)

    print("\nRecorriendo en sentido inverso:")
    for char in container.reverse_iterator():
        print(char)
