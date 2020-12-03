import os
import asyncio
from types import SimpleNamespace
from .widget import (
    Power,
    Bar,
)
from .layout import (
    floating_layout,
    layouts,
)
from .keybindings import (
    keys,
    mouse,
)
from .util.sync import await_sync
from libqtile import (
    widget,
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

widgets = SimpleNamespace(
    group_box=widget.GroupBox(),
    prompt=widget.Prompt(),
    task_list=widget.TaskList(),
    spacer=widget.Spacer(),
    systray=widget.Systray(),
    clock=widget.Clock(format='%H:%M'),
    power=Power(line_weight=0.1, rotate=0.0),
)

screens = [
    Screen(
        top=Bar(
            [
                widgets.group_box,
                widgets.prompt,
                widgets.task_list,
                widgets.spacer,
                widgets.systray,
                widgets.clock,
                widgets.power,
            ],
            64,
        ),
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
async def _autostart():
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
