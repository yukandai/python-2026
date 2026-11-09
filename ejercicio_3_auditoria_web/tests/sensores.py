import pytest

class TestCasesSensor:
    def test_sensor_id(self, sensor):
        sensor_id = sensor.get("sensor_id", "")
        limpio = sensor_id.strip()
        es_valido = (limpio == sensor_id) and (len(limpio) > 0)
        assert es_valido, f"Error: El sensor '{sensor_id}' contiene espacios no deseados."

    def test_ubicacion(self, sensor):
        sensor_id = sensor.get("sensor_id", "")
        ubicacion = sensor.get("ubicacion", "")
        es_valida = len(ubicacion) > 0
        assert es_valida, f"Error: La ubicación del sensor '{sensor_id}' no puede estar vacía."

    def test_temperatura(self, sensor):
        sensor_id = sensor.get("sensor_id", "")
        temperatura = sensor.get("temperatura", "")
        temp = temperatura.strip()
        sin_punto = temp.replace(".", "", 1) # Reemplaza solo el primer punto
        es_valida = sin_punto.isdigit() # Comprobamos que sean dígitos y que tenga al menos un carácter numérico
        assert es_valida, f"Error: La temperatura del sensor '{sensor_id}', contiene caracteres inválidos '{temperatura}'"