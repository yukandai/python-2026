# Noviembre 2026 - Cintia Ossandón
from tests.sensores import TestCasesSensor
from tests.paneles import TestCasesPanel

def main():
    try:
        # TEST: sensores
        print("Iniciando validacion de sensores...")

        datos_sensores = [
            {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
            {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""},
            {"sensor_id": "SENSOR-003", "temperatura": "32.1º", "ubicacion": " Planta Baja "},
            {"sensor_id": "SENSOR-004", "temperatura": "1", "ubicacion": "Planta Baja"}
        ]
        
        for sensor in datos_sensores:
            sensor_limpio = True
            try:
                TestCasesSensor().test_sensor_id(sensor) #espacios al comienzo y al final
            except AssertionError as error_test:
                print(f"[FALLO DE VALIDACIÓN]: {error_test}")
                sensor_limpio = False

            try:
                TestCasesSensor().test_ubicacion(sensor) #ubicacion vacia
            except AssertionError as error_test:
                print(f"[FALLO DE VALIDACIÓN]: {error_test}")
                sensor_limpio = False

            try:
                TestCasesSensor().test_temperatura(sensor) #temperatura con caracteres
            except AssertionError as error_test:
                print(f"[FALLO DE VALIDACIÓN]: {error_test}")
                sensor_limpio = False

            if sensor_limpio:
                print(f"El sensor {sensor["sensor_id"]} pasó todas las validaciones correctamente")

        # TEST: paneles solares
        print("\nIniciando validacion de paneles...")

        datos_paneles = [
            {"id_producto": "P001", "nombre": "PANEL-ULTRA-01", "precio": 250.0, "stock": 40, "eficiencia": 17, "potencia": 1000}, #valido
            {"id_producto": "P002", "nombre": "PANEL-ULTRA-02", "precio": 260.0, "stock": -5, "eficiencia": 18, "potencia": 1100}  #invalido
        ]

        for panel in datos_paneles:
            try:
                TestCasesPanel().test_stock_panel(panel) #stock negativo
                print(f"El panel {panel["nombre"]} pasó todas las validaciones correctamente")
            except AssertionError as error_test:
                print(f"[FALLO DE VALIDACIÓN]: {error_test}")

    except Exception as e:
        print(f"Error inesperado al instanciar: {e}")

if __name__ == '__main__':
	main()