import time


def runtime(func):

    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        dt_ms = (time.perf_counter() - start) * 1000
        print(f"Runtime: {dt_ms:.2f} ms")
        return ret

    return wrapped
