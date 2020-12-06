from itertools import chain


__all__ = [
    'MOD',
    'CONTROL',
    'SHIFT',
    'ALT',
    'generate',
]


MOD = 'mod4'
CONTROL = 'control'
SHIFT = 'shift'
ALT = 'mod1'


class KeyMixin:
    def keys(self):
        pass


def generate(widgets):
    return list(chain(*(
        w.keys() for w in widgets.__dict__.values() if isinstance(w, KeyMixin)
    )))
