from collections.abc import Iterable


def deep_flatten(nested_iterable):
    """flatten an iterable of iterables."""
    for item in nested_iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item
