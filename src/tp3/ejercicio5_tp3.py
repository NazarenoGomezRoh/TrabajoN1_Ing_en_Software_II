import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------



#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class AlasAvion:
   size = None

class TurbinasAvion:
   horsepower = None

class BodyAvion:
   shape = None
   
class TrenAterrizaje:
    type = None


class DirectorAvion:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Luego el tren de aterrizaje
      tren = self.__builder.getTren()
      avion.setTren(tren)
      
      # Dos turbinas
      i = 0
      while i < 2:
        turbinas = self.__builder.getTurbinas()
        avion.setTurbina(turbinas)
        i += 1
      
      # Finalmente (2) alas
      i = 0
      while i < 2:
        alas = self.__builder.getAlas()
        avion.attachAlas(alas)
        i += 1
      
      
      # Retorna el vehiculo completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__alas = list()
      self.__turbinas = list()
      self.__body = None
      self.__tren= None

   def setBody(self, body):
      self.__body = body

   def attachAlas(self, alas):
      self.__alas.append(alas)

   def setTurbina(self, turbinas):
      self.__turbinas.append(turbinas)

   def setTren(self, tren):
        self.__tren = tren

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print("Turbinas:")
      for turbina in self.__turbinas:
            print("  - Horsepower: %d" % (turbina.horsepower))
      print("Alas:")
      for alas in self.__alas:
            print("  - Size: %d" % (alas.size))
      print("Tren de aterrizaje: %s" % (self.__tren.type))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class BuilderAvion:
	
      def getAlas(self): pass
      def getTurbinas(self): pass
      def getBody(self): pass
      def getTren(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un avion
#* Establece instancias para tomar alas, turbinas y chasis
#* estableciendo las partes específicas que (en un Avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(BuilderAvion):
   
   def getAlas(self):
      alas = AlasAvion()
      alas.size = 30  # Tamaño genérico para ejemplo
      return alas
   
   def getTurbinas(self):
      turbinas = TurbinasAvion()
      turbinas.horsepower = 500  # Potencia genérica para ejemplo
      return turbinas
   
   def getBody(self):
      body = BodyAvion()
      body.shape = "Airbus A320"  # Modelo genérico para ejemplo
      return body
   
   def getTren(self):
        tren = TrenAterrizaje()
        tren.type = "Convencional"  # Tipo genérico para ejemplo
        return tren
    
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():
    avionBuilder = AvionBuilder()
    director = DirectorAvion()
    director.setBuilder(avionBuilder)
    avion = director.getAvion()
    avion.specification()
   
#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("cls")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")

   main()
