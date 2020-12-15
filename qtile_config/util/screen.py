from libqtile.config import Screen
from libqtile import qtile
from .. import theme


__all__ = [
    'generate',
]


def generate(widgets):
    screens = []
    while len(screens) < len(qtile.conn.pseudoscreens):
        screens.append(Screen(
            top=widgets.bar,
            wallpaper=theme.wallpaper.url,
            wallpaper_mode=theme.wallpaper.mode,
        ))
    return screens
