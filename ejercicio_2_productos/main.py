# Noviembre 2026 - Cintia Ossandón
from clases.gestor_inventario import GestorInventario
from clases.dispositivo_ecologico import StockInvalidoError
from clases.panel_solar import PanelSolar

def main():
    inventario_prueba = []

    print("--- Cargando catálogo de productos ---")

    # Producto válido
    try:
        d1 = PanelSolar("P001", "PANEL-ULTRA-01", 250.0, 40, 17, 1000)
        inventario_prueba.append(d1)
        print("Dispositivo 1 creado con éxito.")
    except StockInvalidoError as e:
        print(f"Error inesperado al crear p1: {e}")

    # Producto inválido
    try:
        d2 = PanelSolar("P002", "PANEL-ULTRA-02", 260.0, -1, 18, 1000)
        inventario_prueba.append(d2)
    except StockInvalidoError as e:
        print(f"✅ Captura controlada exitosa: {e}")

    print("\n--- Mostrando catálogo de productos ---")
    for disp in inventario_prueba:
        print(disp.generar_ficha_tecnica())

    # Exporta productos a JSON
    archivo_salida = "catalogo_ecologico.json"
    GestorInventario.guardar_catalogo_json(inventario_prueba, archivo_salida)
    print(f"Inventario de productos válidos exportado correctamente a '{archivo_salida}'.")

if __name__ == '__main__':
	main()