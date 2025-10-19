# Estructura de Datos
# Unidad 2
#  suma de digitos
#victor hugo perusquia cruz 24590403

class SumaDigitos:
    def __init__(self, cifra_completa):
        self.numero_completo = cifra_completa

    def obtener_total(self):
        return self._acumular_recursivamente(self.numero_completo)

    def _acumular_recursivamente(self, remanente):
        if remanente == 0:
            return 0
        else:
            return remanente % 10 + self._acumular_recursivamente(remanente // 10)

# Ejemplo de uso :
agregador = SumaDigitos(12345)
total_digitos = agregador.obtener_total()
print(total_digitos)  