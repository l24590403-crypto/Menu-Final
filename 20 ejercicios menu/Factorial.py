# Estructura de Datos
# Unidad 2
#  Factorial
#victor hugo perusquia cruz 24590403


class Factorial:

    def __init__(self, numero_inicial):
        self.numero = numero_inicial

    def ejecutar_calculo(self):
        return self._proceso_recursivo(self.numero)

    def _proceso_recursivo(self, num):
        if num == 1:
            return 1
        else:
            return num * self._proceso_recursivo(num - 1)


# Ejemplo de uso de la clase:
calculadora = Factorial(6)
resultado = calculadora.ejecutar_calculo()
print(resultado)  