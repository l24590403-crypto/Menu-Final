# Estructura de Datos
# Unidad 2
# Combinaciones
#victor hugo perusquia cruz 24590403

class Combinaciones:
    def __init__(self, conjunto_original):
        self.conjunto = conjunto_original

    def mostrar_combinaciones(self):
        self._construir_combinacion("", self.conjunto)

    def _construir_combinacion(self, combinacion_parcial, remanente):
        if not remanente:
            print(combinacion_parcial)
        else:
            self._construir_combinacion(combinacion_parcial + remanente[0], remanente[1:])
            self._construir_combinacion(combinacion_parcial, remanente[1:])

# Ejemplo de uso de la clase:
procesador = Combinaciones("abc")
procesador.mostrar_combinaciones()