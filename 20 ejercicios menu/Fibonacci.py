# Estructura de Datos
# Unidad 2
#  Fibonacci
#victor hugo perusquia cruz 24590403

class Fibonacci:
    def __init__(self, indice_deseado):
        self.indice = indice_deseado

    def obtener_valor(self):
        return self._proceso_recursivo(self.indice)

    def _proceso_recursivo(self, posicion):
        if posicion == 0 or posicion == 1:
            return posicion
        else:
            return self._proceso_recursivo(posicion - 1) + self._proceso_recursivo(posicion - 2)

# Ejemplo de uso de la clase:
calculadora = Fibonacci(6)
valor_fibonacci = calculadora.obtener_valor()
print(valor_fibonacci)  