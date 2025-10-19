# Estructura de Datos
# Unidad 2
#  suma de listas
#victor hugo perusquia cruz 24590403


class AcumuladorDeListas:
    def __init__(self, conjunto_numeros):
        self.numeros = conjunto_numeros

    def obtener_suma_total(self):
        return self._sumar_recursivamente(self.numeros)

    def _sumar_recursivamente(self, sub_lista):
        if not sub_lista:
            return 0
        else:
            return sub_lista[0] + self._sumar_recursivamente(sub_lista[1:])

# Ejemplo de uso de la clase:
acumulador = AcumuladorDeListas([1, 2, 3, 4, 5,6])
suma_final = acumulador.obtener_suma_total()
print(suma_final)  