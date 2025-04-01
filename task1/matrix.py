from tensor import Tensor


class Matrix(Tensor):
    def __init__(self, dimensions, data):
        if len(dimensions) != 2:
            raise ValueError("Dimensions mismatch")

        self._rows: int = dimensions[0]
        self._columns: int = dimensions[1]
        if len(data) != self._rows * self._columns:
            raise ValueError("Data size mismatch")

        super().__init__(dimensions, data)

    def conv_rc2i(self, r: int, c: int) -> int:
        r = r % self._rows
        c = c % self._columns
        return r * self._columns + c

    def conv_i2rc(self, i: int) -> tuple[int, int]:
        i = i % len(self.data)
        return divmod(i, self._columns)

    def __str__(self):
        max_len = max(len(str(item)) for item in self.data)
        lines = []
        for r in range(self._rows):
            row_values = [str(self.data[self.conv_rc2i(r, c)]).rjust(max_len) for c in range(self._columns)]
            lines.append("  ".join(row_values))
        return "[\n" + "\n".join(lines) + "\n]"

    def __getitem__(self, index):
        if any([isinstance(index, t) for t in [int, list, slice]]):
            if isinstance(index, int):
                i = self.conv_rc2i(index, 0)
                return Matrix((1, self._columns), self.data[i:i+self._columns])

            new_rows = []

            if isinstance(index, list):
                new_rows = [r % self._rows for r in index]

            if isinstance(index, slice):
                new_rows = range(*index.indices(self._rows))

            new_data = [self.data[i * self._columns:(i + 1) * self._columns] for i in new_rows]

            return Matrix((len(new_rows), self._columns), [num for row in new_data for num in row])

        if isinstance(index, tuple):
            row_index, column_index = index

            def get_indexes(idx, size):
                if isinstance(idx, int):
                    res = [idx % size]
                elif isinstance(idx, slice):
                    res = range(*idx.indices(size))
                elif isinstance(idx, list):
                    res = [j % size for j in idx]
                else:
                    raise TypeError("Invalid index type")
                return res

            new_rows = get_indexes(row_index, self._rows)
            new_columns = get_indexes(column_index, self._columns)

            return Matrix((len(new_rows), len(new_columns)), [self.data[r * self._columns + c] for r in new_rows for c in new_columns])

        raise TypeError("Invalid index type")
