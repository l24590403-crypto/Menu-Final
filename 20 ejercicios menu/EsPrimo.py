# Estructura de Datos
# Unidad 2
#  es primo
#victor hugo perusquia cruz 24590403

class Es_Primo:
    def __init__(self, valor_a_evaluar):
        self.valor = valor_a_evaluar

    def es_numero_primo(self):
        return self._validar_recursivamente(self.valor, 2)

    def _validar_recursivamente(self, numero_evaluado, divisor_actual):
        if numero_evaluado <= 2:
            return numero_evaluado == 2
        
        if numero_evaluado % divisor_actual == 0:
            return False
        
        if divisor_actual * divisor_actual > numero_evaluado:
            return True
            
        return self._validar_recursivamente(numero_evaluado, divisor_actual + 1)

# Ejemplo de uso de la clase:
analizador = Es_Primo(13)
print(analizador.es_numero_primo())  

analizador_dos = Es_Primo(15)
print(analizador_dos.es_numero_primo())  