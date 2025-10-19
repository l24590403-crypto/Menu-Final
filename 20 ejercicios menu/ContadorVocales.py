# Estructura de Datos
# Unidad 2
# Contador de vocales
#victor hugo perusquia cruz 24590403

class ContadorVocales:
    def __init__(self, frase_inicial):
        self.frase = frase_inicial

    def obtener_frecuencia_vocalica(self):
        return self._inspeccionar_recursivamente(self.frase)

    def _inspeccionar_recursivamente(self, subcadena):
        if not subcadena:
            return 0

        if subcadena[0].lower() in 'aeiou':
            return 1 + self._inspeccionar_recursivamente(subcadena[1:])
        else:
            return self._inspeccionar_recursivamente(subcadena[1:])

# Ejemplo de uso de la clase:
procesador = ContadorVocales("Recursividad")
total_vocales = procesador.obtener_frecuencia_vocalica()
print(total_vocales)  # Imprime 5