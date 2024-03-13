class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            mensaje_rec = f"Mensaje: {self.mensaje}, dimension: {self.dimension}, maximo: {self.maximo}"
            return mensaje_rec