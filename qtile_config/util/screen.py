from libqtile.config import Screen
from .. import theme


__all__ = [
    'generate',
]


def generate(widgets):
    return [
        Screen(
            top=widgets.bar,
            wallpaper=theme.wallpaper.url,
            wallpaper_mode=theme.wallpaper.mode,
        ),
    ]
