# Estructura de Datos
# Unidad 2
# Contador  de caracteres
#victor hugo perusquia cruz 24590403

class ContarCaracter:
    def __init__(self, frase_completa):
        self.frase = frase_completa

    def obtener_conteo(self, caracter_buscado):
        return self._inspeccionar_recursivamente(self.frase, caracter_buscado)

    def _inspeccionar_recursivamente(self, subcadena, target):
        if not subcadena:
            return 0
        
        if subcadena[0] == target:
            return 1 + self._inspeccionar_recursivamente(subcadena[1:], target)
        else:
            return self._inspeccionar_recursivamente(subcadena[1:], target)

# Ejemplo de uso de la clase:
analizador = ContarCaracter("banana")
print(analizador.obtener_conteo("a"))  # Imprime 3