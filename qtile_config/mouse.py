from libqtile.lazy import lazy
from libqtile.config import (
    Drag,
    Click,
)
from .util.key import MOD


__all__ = [
    'mouse',
]


# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD],
        'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click(
        [MOD],
        'Button2',
        lazy.window.bring_to_front(),
    ),
]
