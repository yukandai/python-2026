from clases.dispositivo_ecologico import DispositivoEcologico

class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha_tecnica = super().generar_ficha_tecnica()
        ficha_tecnica.update({"Eficiencia": self.eficiencia, "Potencia" : self.potencia_w})
        return ficha_tecnica