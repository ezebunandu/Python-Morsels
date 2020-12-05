from collections.abc import Set


class OrderedSet(Set):
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        yield from self.elements

    def __len__(self):
        return len(self.elements)

    def __contains__(self, ele):
        return ele in self.elements
