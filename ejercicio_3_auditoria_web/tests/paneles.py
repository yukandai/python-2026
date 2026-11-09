#Test manuales
from clases.panel_solar import PanelSolar
from clases.dispositivo_ecologico import StockInvalidoError

class TestCasesPanel:
    def test_stock_panel(self, panel):
        id_producto = panel.get("id_producto", "")
        nombre = panel.get("nombre", "")
        precio = panel.get("precio", "")
        stock = panel.get("stock", "")
        eficiencia = panel.get("eficiencia", "")
        potencia = panel.get("potencia", "")

        try:
            panel = PanelSolar(id_producto, nombre, precio, stock, eficiencia, potencia)
            es_valido = True
        except StockInvalidoError:
            es_valido = False

        assert es_valido, f"El stock para el producto '{nombre}' debe ser mayor a cero"

