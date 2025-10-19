# Estructura de Datos
# Unidad 2
#  Potencias
#victor hugo perusquia cruz 24590403

class OperacionExponencial:
    def __init__(self, numero_base, numero_exponente):
        self.base = numero_base
        self.exponente = numero_exponente

    def obtener_resultado(self):
        return self._multiplicar_recursivamente(self.base, self.exponente)

    def _multiplicar_recursivamente(self, base_val, exp_val):
        if exp_val == 0:
            return 1
        else:
            return base_val * self._multiplicar_recursivamente(base_val, exp_val - 1)

# Ejemplo de uso de la clase:
operacion = OperacionExponencial(2, 3)
resultado_final = operacion.obtener_resultado()
print(resultado_final)  