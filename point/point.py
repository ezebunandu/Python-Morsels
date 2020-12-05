from numbers import Number


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __mul__(self, scaler):
        if isinstance(scaler, Number):
            x = self.x * scaler
            y = self.y * scaler
            z = self.z * scaler
            return Point(x, y, z)
        else:
            raise TypeError

    def __rmul__(self, scaler):
        if isinstance(scaler, Number):
            return self.__mul__(scaler)
        else:
            raise TypeError

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
