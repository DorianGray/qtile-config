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
    Match,
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
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(title='branchdialog'),
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Steam'),  # Steam
    Match(title='Steam'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = 'LG3D'
