import asyncio
import functools


__all__ = [
    'await_sync',
]


def await_sync(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return asyncio.get_event_loop().run_until_complete(result)
        return result

    return wrapper
