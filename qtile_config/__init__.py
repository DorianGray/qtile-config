import os
import asyncio
from itertools import chain
from . import widgets
from .widget.mixin import KeyMixin
from .layout import (
    floating_layout,
    layouts,
)
from .util.sync import await_sync
from .mouse import mouse
from libqtile import (
    hook,
)
from libqtile.config import (
    Group,
    Screen,
)


__all__ = [
    'groups',
    'layouts',
    'widget_defaults',
    'extension_defaults',
    'screens',
    'keys',
    'mouse',
    'dgroups_key_binder',
    'dgroups_app_rules',
    'follow_mouse_focus',
    'bring_front_click',
    'cursor_warp',
    'floating_layout',
    'auto_fullscreen',
    'focus_on_window_activation',
    'wmname',
]


DISPLAY = os.getenv('DISPLAY', None)
HOME = os.getenv('HOME', None)

groups = [
    Group('Terminal', spawn='alacritty -t Terminal -e tmux-session qtile'),
    Group('Web', spawn='google-chrome'),
]

widget_defaults = dict(
    font='Hack Bold',
    fontsize=36,
    padding=5,
)
extension_defaults = widget_defaults.copy()

# Add widget keys to global keys
keys = list(chain(*(
    w.keys() for w in widgets.__dict__.values() if isinstance(w, KeyMixin)
)))

screens = [
    Screen(
        top=widgets.bar,
        wallpaper='/usr/share/sddm/themes/sugar-candy/Backgrounds/Space.jpg',
        wallpaper_mode='fill',
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = 'smart'
wmname = 'LG3D'


@hook.subscribe.startup_once
@await_sync
async def autostart():
    await asyncio.create_subprocess_exec(
        'compton',
        '--config',
        f'{HOME}/.config/compton/compton.conf',
        '-dbus',
        '-d',
        DISPLAY,
    )
    await asyncio.create_subprocess_exec(
        'xautolock',
        '-time',
        '10',
        '-detectsleep',
        '-locker',
        '/usr/local/bin/xautolocker',
    )
    await asyncio.create_subprocess_exec('unclutter', '-root')
