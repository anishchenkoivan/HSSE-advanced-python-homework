class Tensor:
    def __init__(self, dimensions: int | tuple[int, ...], data):
        self._dimensions = dimensions
        self._data = data

    @property
    def dimensions(self) -> int:
        return self._dimensions

    @property
    def data(self):
        return self._data

    def __str__(self):
        return str(self._data)