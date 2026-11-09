# Noviembre 2026 - Cintia Ossandón

# Punto A
def limpiar_registro_sensor(registro_raw):
    registro_limpio = {}

    sensor_id_raw = registro_raw.get("sensor_id", "")
    registro_limpio["sensor_id"] = sensor_id_raw.strip()

    temperatura_raw = registro_raw.get("temperatura", "0")
    
    #TODO: llamar a una funcion q reemplace todo lo q no sea numero
    temperatura_clean1 = temperatura_raw.replace("C", "").strip()
    temperatura_clean2 = temperatura_clean1.replace("F", "").strip()
    temperatura_clean3 = temperatura_clean2.replace("º", "").strip()
    
    registro_limpio["temperatura"] = float(temperatura_clean3)

    ubicacion_raw = registro_raw.get("ubicacion", "")
    if ubicacion_raw is None or str(ubicacion_raw).strip() == "":
        registro_limpio["ubicacion"] = "Área No Asignada"
    else:
        registro_limpio["ubicacion"] = str(ubicacion_raw).strip()

    return registro_limpio

# Punto B
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    if not lista_sensores_limpios:
        return [], 0.0

    lista_sensores_alerta = []
    temperatura_total = 0.0

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
        temperatura_total += temperatura

    promedio_temperatura = temperatura_total / len(lista_sensores_limpios)

    return lista_sensores_alerta, promedio_temperatura

def main():
    datos_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "20.0F", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "32.1º", "ubicacion": "Planta Baja"}
    ]

    datos_normalizados = []

    print("--- PASANDO POR LA ETAPA DE SANITIZACIÓN ---")
    sensores_limpios = [limpiar_registro_sensor(r) for r in datos_crudos]
    for m in sensores_limpios:
        datos_normalizados.append(m)

    print("--- Nuevo diccionario ---")
    print(datos_normalizados)

    print("\n--- GENERANDO REPORTE CONSOLIDADO ---")
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral_temperatura=40.0)
    print(f"Sensores en Alerta (> 40.0º): {alertas}")
    print(f"Promedio de Temperatura Global: {promedio} º")

if __name__ == '__main__':
	main()