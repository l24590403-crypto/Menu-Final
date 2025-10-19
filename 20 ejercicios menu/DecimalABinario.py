# Estructura de Datos
# Unidad 2
#  de decimal a binario
#victor hugo perusquia cruz 24590403


class DecimalABinario:
    def __init__(self, numero_base_diez):
        self.numero_decimal = numero_base_diez

    def a_binario(self):
        if self.numero_decimal == 0:
            return "0"
        return self._proceso_recursivo_conversion(self.numero_decimal)

    def _proceso_recursivo_conversion(self, numero):
        if numero == 0:
            return ''
        else:
            return self._proceso_recursivo_conversion(numero // 2) + str(numero % 2)

# Ejemplo de uso de la clase:
convertidor = DecimalABinario(10)
representacion_binaria = convertidor.a_binario()
print(representacion_binaria)  