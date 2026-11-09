import json
from clases.panel_solar import PanelSolar

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializar = []
        for dispositivo in lista_dispositivos:
            datos_dispositivo = {
                "id_producto": dispositivo.id_producto,
                "nombre": dispositivo.nombre,
                "precio": f"${float(dispositivo.precio):.2f}",
                "stock": dispositivo.stock
            }

            if isinstance(dispositivo, PanelSolar):
                datos_dispositivo["eficiencia"] = dispositivo.eficiencia
                datos_dispositivo["potencia"] = dispositivo.potencia_w

            datos_serializar.append(datos_dispositivo)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializar, archivo, indent=4, ensure_ascii=False)