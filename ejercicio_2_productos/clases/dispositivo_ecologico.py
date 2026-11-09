class StockInvalidoError(Exception):
    """Excepción lanzada cuando el stock es menor a cero"""
    pass

class DispositivoEcologico:
    def __init__(self, id_producto, nombre, precio, stock) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f"El stock para el producto '{self.id_producto}' debe ser mayor a cero")
        self.__stock = valor

    def generar_ficha_tecnica(self):
        return {
            "Producto": self.id_producto,
            "Nombre": self.nombre,
            "Precio": f"${float(self.precio):.2f}",
            "Stock": self.stock
        }