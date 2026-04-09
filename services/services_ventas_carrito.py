class Carrito:
    def __init__(self):
        self.items = {}

    def agregar(self, codigo, nombre, cantidad, precio):
        # Aseguramos tipos de datos
        precio = float(precio)
        cantidad = int(cantidad)

        if codigo in self.items:
            self.items[codigo]["cantidad"] += cantidad
            # Recalculamos subtotal basándonos en la nueva cantidad
            self.items[codigo]["subtotal"] = self.items[codigo]["cantidad"] * precio
        else:
            self.items[codigo] = {
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": cantidad * precio
            }

    def obtener_total(self):
        """Devuelve la suma de todos los subtotales."""
        return sum(item["subtotal"] for item in self.items.values())

    def vaciar(self):
        self.items = {}

    def eliminar_producto(self, codigo):
        if codigo in self.items:
            del self.items[codigo]