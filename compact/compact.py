from itertools import groupby


def compact(iterable):
    return (item for item, group in groupby(iterable))
