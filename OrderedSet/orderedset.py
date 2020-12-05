from collections import OrderedDict


class OrderedSet:
    """A set-like object that maintains the order of insertion"""

    def __init__(self, iterable):
        self.elements = OrderedDict()
        for item in iterable:
            self.elements[item] = 1

    def __iter__(self):
        yield from self.elements.keys()

    def __len__(self):
        return len(self.elements.keys())

    def __contains__(self, ele):
        return ele in self.elements.keys()

    def add(self, ele):
        self.elements[ele] = 1

    def discard(self, ele):
        if ele in self.elements.keys():
            self.elements.pop(ele)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return tuple(self) == tuple(other)
        elif isinstance(other, set):
            return list(self.elements.keys()) == list(other)

    def __getitem__(self, i):
        return list(self.elements.keys())[i]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.elements.keys()})"
