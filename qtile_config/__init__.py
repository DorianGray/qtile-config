from .widget.power import Power
from .keybindings import (
    keys,
    mouse,
)
from . import hooks  # noqa: F401
from libqtile import (
    bar,
    layout,
    widget,
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


groups = [
    Group('Terminal', spawn='alacritty -t Terminal -e tmux-session qtile'),
    Group('Web', spawn='google-chrome'),
]

layouts = [
    layout.Max(),
    layout.Tile(),
]

widget_defaults = dict(
    font='Hack Bold',
    fontsize=36,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.TaskList(),
                widget.Spacer(),
                widget.Systray(),
                widget.Clock(format='%H:%M'),
                Power(line_weight=0.1, rotate=0.0),
            ],
            64,
        ),
        wallpaper="/usr/share/sddm/themes/sugar-candy/Backgrounds/Space.jpg",
        wallpaper_mode="fill",
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wname': 'branchdialog'},
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'Steam'},  # Steam
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = 'LG3D'
