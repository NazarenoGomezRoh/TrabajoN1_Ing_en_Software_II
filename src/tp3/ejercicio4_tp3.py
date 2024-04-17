from abc import ABC, abstractmethod

# Interfaz para la creación de facturas
class Factura(ABC):
    @abstractmethod
    def generar_factura(self, importe):
        pass

# Clase base para facturas
class FacturaBase(Factura):
    def generar_factura(self, importe):
        return f"Factura con importe total: ${importe}"

# Clase para facturas con IVA Responsable
class FacturaIVAResponsable(Factura):
    def generar_factura(self, importe):
        total_con_iva = importe * 1.21  # IVA del 21%
        return f"Factura con importe total (IVA Responsable): ${total_con_iva}"

# Clase para facturas con IVA No Inscripto
class FacturaIVANoInscripto(Factura):
    def generar_factura(self, importe):
        total_sin_iva = importe
        return f"Factura con importe total (IVA No Inscripto): ${total_sin_iva}"

# Clase para facturas con IVA Exento
class FacturaIVAExento(Factura):
    def generar_factura(self, importe):
        return f"Factura con importe total (IVA Exento): ${importe}"

# Factory Method para crear instancias de factura según la condición impositiva
class FacturaFactory:
    def obtener_factura(self, tipo):
        if tipo == "Responsable":
            return FacturaIVAResponsable()
        elif tipo == "No Inscripto":
            return FacturaIVANoInscripto()
        elif tipo == "Exento":
            return FacturaIVAExento()
        else:
            return FacturaBase()

# Ejemplo de uso
if __name__ == "__main__":
    factory = FacturaFactory()

    # Cliente Responsable
    factura_responsable = factory.obtener_factura("Responsable")
    print(factura_responsable.generar_factura(100))

    # Cliente No Inscripto
    factura_no_inscripto = factory.obtener_factura("No Inscripto")
    print(factura_no_inscripto.generar_factura(100))

    # Cliente Exento
    factura_exento = factory.obtener_factura("Exento")
    print(factura_exento.generar_factura(100))

    # Cliente sin especificar condición impositiva
    factura_base = factory.obtener_factura("")
    print(factura_base.generar_factura(100))
