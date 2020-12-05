import contextlib


class ExceptionInfo:
    exception = None
    traceback = None


@contextlib.contextmanager
def suppress(*exception_types):
    info = ExceptionInfo()
    try:
        yield info
    except exception_types as e:
        info.exception = e
        info.traceback = e.__traceback__
        contextlib.suppress(exception_types)
