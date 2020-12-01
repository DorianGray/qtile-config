__all__ = [
    'hex2rgb',
]


def hex2rgb(s):
    s = s.lstrip('#')
    return tuple(float(int(s[i:i+2], 16)) for i in (0, 2, 4))
