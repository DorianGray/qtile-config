import os
import importlib


__all__ = [
    'set_theme',
    'theme',
]

DEFAULT = os.getenv('THEME_DEFAULT', 'default')

name = None
proxy = None


def _ensure_theme(theme=DEFAULT):
    global name, proxy
    if theme is None:
        theme = DEFAULT
    if name != theme:
        name = theme
        proxy = None
    if proxy is None:
        proxy = importlib.import_module(f'qtile_config.theme.{name}').theme


def set_theme(name):
    return _ensure_theme(name)


class Theme:
    def __getattr__(cls, item):
        _ensure_theme(name or DEFAULT)
        if hasattr(proxy, item):
            return getattr(proxy, item)
        raise AttributeError(item)


theme = Theme()
