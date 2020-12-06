import importlib


__all__ = [
    'set_theme',
]


_name = None
_proxy = None


def set_theme(theme):
    global _name, _proxy
    if theme is None:
        theme = 'default'
    if _name != theme:
        _name = theme
        _proxy = None
    if _proxy is None:
        _proxy = importlib.import_module(f'qtile_config.theme.{_name}').theme


def __getattr__(attr):
    global _name, _proxy
    set_theme(_name)
    if hasattr(_proxy, attr):
        return getattr(_proxy, attr)
    raise AttributeError(attr)
