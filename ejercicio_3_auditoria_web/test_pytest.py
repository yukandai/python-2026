# Noviembre 2026 - Cintia Ossandón
import pytest
from clases.panel_solar import PanelSolar
from clases.dispositivo_ecologico import StockInvalidoError

class TestCases:
    #Definimos una lista con los diferentes casos de prueba
    @pytest.mark.parametrize("sensor_data", [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""},
        {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "},
        {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}
    ])

    def test_sensor_id(self, sensor_data):
        # Datos de prueba para simular un sensor
        #sensor = {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
        #sensor = {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""}
        #sensor = {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "}
        #sensor = {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}

        sensor_id = sensor_data.get("sensor_id", "")
        limpio = sensor_id.strip()
        es_valido = (limpio == sensor_id) and (len(limpio) > 0)
        assert es_valido, f"Error: El sensor '{sensor_id}' contiene espacios no deseados."

    #Definimos una lista con los diferentes casos de prueba
    @pytest.mark.parametrize("sensor_data", [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""},
        {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "},
        {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}
    ])

    def test_ubicacion(self, sensor_data):
        # Datos de prueba para simular un sensor
        #sensor = {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
        #sensor = {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""}
        #sensor = {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "}
        #sensor = {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}

        sensor_id = sensor_data.get("sensor_id", "")
        ubicacion = sensor_data.get("ubicacion", "")
        es_valida = len(ubicacion) > 0
        assert es_valida, f"Error: La ubicación del sensor '{sensor_id}' no puede estar vacía."

    #Definimos una lista con los diferentes casos de prueba
    @pytest.mark.parametrize("sensor_data", [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""},
        {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "},
        {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}
    ])

    def test_temperatura(self, sensor_data):
        # Datos de prueba para simular un sensor
        #sensor = {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
        #sensor = {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""}
        #sensor = {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "}
        #sensor = {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}

        sensor_id = sensor_data.get("sensor_id", "")
        temperatura = sensor_data.get("temperatura", "")
        temp = temperatura.strip()
        sin_punto = temp.replace(".", "", 1) # Reemplaza solo el primer punto
        es_valida = sin_punto.isdigit() # Comprobamos que sean dígitos y que tenga al menos un carácter numérico
        assert es_valida, f"Error: La temperatura del sensor '{sensor_id}', contiene caracteres inválidos '{temperatura}'"

    @pytest.mark.parametrize("panel_data", [
       {"id_producto": "P001", "nombre": "PANEL-ULTRA-01", "precio": 250.0, "stock": 40, "eficiencia": 17, "potencia": 1000}, # Válido
       {"id_producto": "P002", "nombre": "PANEL-ULTRA-02", "precio": 260.0, "stock": -5, "eficiencia": 18, "potencia": 1100}  # Inválido (stock negativo)
    ])

    def test_stock_panel(self, panel_data):
        #panel = {"id_producto": "P001", "nombre": "PANEL-ULTRA-01", "precio": 250.0, "stock": 40, "eficiencia": 17, "potencia": 1000} #valido
        #panel = {"id_producto": "P002", "nombre": "PANEL-ULTRA-02", "precio": 260.0, "stock": -5, "eficiencia": 18, "potencia": 1100} #invalido
        
        id_producto = panel_data.get("id_producto", "")
        nombre = panel_data.get("nombre", "")
        precio = panel_data.get("precio", "")
        stock = panel_data.get("stock", "")
        eficiencia = panel_data.get("eficiencia", "")
        potencia = panel_data.get("potencia", "")
        try:
            panel = PanelSolar(id_producto, nombre, precio, stock, eficiencia, potencia)
            es_valido = True
        except StockInvalidoError:
            es_valido = False
        assert es_valido, f"El stock para el producto '{nombre}' debe ser mayor a cero"