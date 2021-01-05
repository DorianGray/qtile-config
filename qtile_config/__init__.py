import os
import asyncio
import libqtile

from . import util
from . import theme
from . import widgets
from .mouse import mouse
from .group import groups
from .layout import (
    floating_layout,
    layouts,
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
THEME = os.getenv('THEME', None)

theme.set_theme(THEME)
widget_defaults = theme.widget_defaults
extension_defaults = theme.extension_defaults

keys = util.key.generate(widgets)
screens = util.screen.generate(widgets)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = 'smart'
wmname = 'LG3D'


@libqtile.hook.subscribe.screen_change
def screen_change(ev):
    libqtile.qtile.cmd_restart()


@libqtile.hook.subscribe.startup_once
async def startup_once():
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
