from collections import deque


def tail(iterable, n):
    """Returns the last n items of a given iterable."""
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
