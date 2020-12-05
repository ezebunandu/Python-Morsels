from math import pi


class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return pi * self.radius ** 2

    @diameter.setter
    def diameter(self, diameter_):
        if diameter_ > 0:
            self.radius = diameter_ / 2
        elif diameter_ < 0:
            raise ValueError("Diameter cannot be negative")

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        elif radius < 0:
            raise ValueError("Radius cannot be negative")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"
