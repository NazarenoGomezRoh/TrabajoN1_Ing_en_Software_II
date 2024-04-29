import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.mementos = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.mementos.insert(0, memento)  # Agrega el nuevo memento al principio de la lista
        if len(self.mementos) > 4:
            self.mementos.pop()  # Recorta la lista si excede los 4 estados almacenados

    def undo(self, steps_back=0):
        if steps_back < len(self.mementos):
            memento = self.mementos[steps_back]
            self.file = memento.file
            self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps_back=0):
        writer.undo(steps_back)

if __name__ == '__main__':
    os.system("cls")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca al <undo> para recuperar el estado anterior")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar dos estados anteriores")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
