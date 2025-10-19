# Estructura de Datos
# Unidad 2
#  suma natural
#victor hugo perusquia cruz 24590403

class SumaNatural:
    def __init__(self, numero_tope):
        self.tope = numero_tope

    def obtener_total(self):
        return self._sumar_recursivamente(self.tope)

    def _sumar_recursivamente(self, valor):
        if valor == 1:
            return 1
        else:
            return valor + self._sumar_recursivamente(valor - 1)

# Ejemplo de uso de la clase:
serie = SumaNatural(6)
total = serie.obtener_total()
print(total)  

