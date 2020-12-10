from collections import UserString

class FuzzyString(UserString):
    """A class which acts like a string but does comparisons
    in a case-insensitive way."""

    def __repr__(self):
        return f"'{self.data}'"

    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.data.lower() == other.data.lower()
        elif isinstance(other, str):
            return self.data.lower() == other.lower()
        else:
            raise NotImplementedError